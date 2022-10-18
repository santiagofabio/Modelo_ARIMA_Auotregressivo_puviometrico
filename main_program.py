from cProfile import label
from re import L
from tkinter import Label
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams
from sklearn import datasets
from tratamento_dataset import tratamento_dataset 
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import kpss
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from testa_hipotese_kpss import testa_hipotese_kpss
from testa_hipotese_shapiro_wilk import testa_hipotese_shapiro_wilk
import scipy.stats as stats
from statsmodels.tsa.arima.model import ARIMA
from estudo_modelo_ar import estudo_modelo_ar
from estudo_media_movel import estudo_media_movel
import seaborn as sns

rcParams['figure.figsize'] =[15,6]
alpha =0.05 # Significancia 

#Tratamento de dados faltantes e tipos
data_set_bruto =pd.read_csv('Chuva_Mensal.csv', sep=';')
print(f'{data_set_bruto.head()}')
tratamento_dataset(data_set_bruto)
del data_set_bruto

#--------------------Configuração base de dados--------------------
data_set =pd.read_csv('data_set_tratado.csv')
data_set =data_set.drop(columns='Ano')
data_set_array =data_set.values

data_set_list =list(data_set_array.flatten())
indice =pd.date_range('1985', periods=len(data_set_list), freq='M')

serie_tempora_chuva =pd.Series(data_set_list,index=indice )
serie_tempora_chuva.plot(label ='Preciptação chuvosa')
plt.xlabel('Ano')
plt.ylabel('Preciptação de chuvosa em mm')
plt.title("Preciptação chovosa ao longo dos anos")
plt.legend(loc ='best')
plt.savefig('serie_temporal_estudada.png', dpi =300, format ='png')
plt.show()
#--------------------------------------------------------------------

#--------------Estudo média movel------------------------------------
estudo_media_movel(serie_tempora_chuva)
#--------------------------------------------------------------------


#Decomposição da serie, a fim de analisar tendência, sazonalidade e resíduos.
serie_decomposta = seasonal_decompose(serie_tempora_chuva,model = "additive" )
serie_decomposta.plot()
plt.title('Série decomposta pelo método aditivo')
plt.savefig('serie_temporal_decomposta.png', dpi =300, format ='png')
plt.show()


#-------------Teste de Normalidade da Serie Original-----------------------
#Teste de Shapiro-Wilk
alfa =0.05
print('Teste de Shapiro-Wilk ao nivel de significancia {:.3f}'.format(alfa))
statistic,value_p =stats.shapiro(serie_tempora_chuva)
print('Estatistica do teste: {:.6f} '.format(statistic))
print('p-valor: {:.6f} '.format(value_p))
testa_hipotese_shapiro_wilk(value_p, alpha)
#-----------------------------------------------------------------------------




#-----------------Traformação raiz cubica sobre a serie
serie_tempora_chuva_raiz_cubica = serie_tempora_chuva**(1/3)
stats.probplot(serie_tempora_chuva_raiz_cubica, dist ='norm',plot =plt)
plt.title("Nomral QQ plt Serie Raiz Cubica")
plt.savefig('nomral_qq_plt_serie_raiz_cubica.png', dpi =300, format ='png')
plt.show()

#-----------------Teste de Estacionáridade------------------------------------
#Teste de Shapiro-Wilk 
print('Teste de Shapiro-Wilk ao nivel de significancia {:.3f}'.format(alpha))
statistic,value_p =stats.shapiro(serie_tempora_chuva)
print('Estatistica do teste: {:.6f} '.format(statistic))
print('p-valor: {:.6f} '.format(value_p))
testa_hipotese_shapiro_wilk(value_p, alpha)

#Teste KPSS
kpss_stat,p_value,lags, crit  = kpss(serie_tempora_chuva_raiz_cubica)
print('Estatistica kpss: {:.6f}'.format(kpss_stat))
print('Estatistica p_value: {:.6f}'.format(p_value))
#chave = significancia, valor  = valor_critico
testa_hipotese_kpss(p_value,crit,alpha )
#-------------------------------------------------------------------------------

#---------------------Autocorrelação Serie Cubica--------------------------------------------
# Se os pontos estão fora do intervalo de confiança, então eles 
# são autocorrelacionados
plot_acf(serie_tempora_chuva_raiz_cubica, lags =20)
plt.title("Autocorrelação Residuos Serie Raiz Cubica")
plt.legend(loc ='best')
plt.xlabel('lags')
plt.ylabel('autocorrelatio')
plt.savefig('parcial_autocorrelacao_raiz_cubica_modelo_ar.png', dpi =300, format ='png')
plt.show()


plot_pacf(serie_tempora_chuva_raiz_cubica, lags =20)
plt.title("Parcial Autocorrelação Raiz Cubica")
plt.legend(loc ='best')
plt.xlabel('lags')
plt.ylabel('autocorrelatio')
plt.savefig('parcial_autocorrelacao_raiz_cubica_modelo_ar.png', dpi =300, format ='png')
plt.show()
#-------------------------------------------------------------------------------
estudo_modelo_ar(serie_tempora_chuva, serie_tempora_chuva_raiz_cubica)


#-------------------------Modlo ARIMA-------------------------------------------
    #Autorregressivo (AR): indica que a variável é regressada em seus valores anteriores. 
    #Integrado (I): indica que os valores de dados foram substituídos com a diferença 
    # entre seus valores e os valores anteriores (diferenciação).
    #Média móvel (MA): Indica que o erro de regressão é uma combinação linear dos
    # termos de erro dos valores passados.
    #Codificação: (p, d, q)
    #Parâmetro d só pode ser inteiro
    # p = ordem da autorregressão.
    # d = grau de diferenciação.
    # q = ordem da média móvel.(Combinação linear de erros passados)