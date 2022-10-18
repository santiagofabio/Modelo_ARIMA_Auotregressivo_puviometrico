def estudo_modelo_ar(serie_temporal_chuva, serie_temporal_chuva_raiz_cubica): 
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
     import seaborn as sns
     rcParams['figure.figsize'] =[15,5]
     alpha =0.05 # Significancia
     
     
     #-------------Modelo AR------------------------------
     #Encontrar menor valor de AIC
     modelo_ar =ARIMA(serie_temporal_chuva_raiz_cubica, order =(1,0,0))
     resultado =modelo_ar.fit()
     print(f'{resultado.summary()}')
     #-----------------------------------------------------------------------------
     
     
     #-------------Analise dos residuos do modelo AR------------------------------
     residuos=resultado.resid
     print('Média residuos {:.5f}'.format(residuos.mean()))
     print('Devio padrão {:.5f}'.format(residuos.std()))
     residuos.plot(label ='Resíduos')
     plt.title('Resíduos Modelo-AR')
     plt.show()
     #-----------------------------------------------------------------------------


     #---------Normalidade dos residuos--------------------------------------------
     stats.probplot(residuos, dist ="norm", plot =plt)
     plt.title("Nomral QQ plot Resíduos Modelo AR")
     plt.savefig('nomral_qq_plot_residuos_modelo_ar.png', dpi =300, format ='png')
     plt.show()
     
     statistic,value_p =stats.shapiro(serie_temporal_chuva)
     testa_hipotese_shapiro_wilk(value_p, alpha)
     sns.displot(residuos, kde=True)
     #-----------------------------------------------------------------------------
     
     
     #---------Diagramas de Autocorrelação---------------------------------------
     plot_acf(residuos, lags =20)
     plt.title("Autocorrelação Resíduos- Modelo-AR")
     plt.xlabel('lags')
     plt.ylabel('autocorrelation')
     plt.savefig('autocorrelacao_residuos_modelo_ar.png', dpi =300, format ='png')
     plt.show()

     plot_pacf(residuos, lags =20,label ='Resíduos')
     plt.title("Parcial Autocorrelação Residuos Modelo-AR")
     plt.xlabel('lags')
     plt.ylabel('autocorrelatio')
     plt.savefig('parcial_autocorrelacao_residuos_modelo_ar.png', dpi =300, format ='png')
     plt.show()
     #-----------------------------------------------------------------------------
     
    
     plt.plot(serie_temporal_chuva_raiz_cubica, label ='Série Real')
     plt.plot(serie_temporal_chuva_raiz_cubica-residuos, color ='red', label ='Residuos')
     plt.savefig('estudo_residuos_serie_modelo_ar.png', dpi =300, format ='png')
     plt.legend(loc ='best')
     plt.show()

     #-----------------------Previsao via Modelo AR------------------------------

     resultado.fittedvalues 
     previsao = resultado.predict(start=431 , end =443)
     print(f'{previsao}')
     previsao2= resultado.forecast(12) 
     plt.plot(serie_temporal_chuva_raiz_cubica, color ='green', label ='Série Real')
     plt.plot(previsao, color ='blue', label ='Previsao')
     plt.plot(serie_temporal_chuva_raiz_cubica-residuos, color ='black', label ='Residuos')
     plt.legend(loc ='best')
     plt.savefig('previsao_serie_cubica.png', dpi =300, format ='png')
    
     plt.show()

     #Retornando a escala original
     
     pd.concat([serie_temporal_chuva_raiz_cubica**3,previsao**3 ]).plot()
     plt.legend(loc ='best')
     plt.xlabel('Anos')
     plt.ylabel("Precipitação pluviometrica")
     plt.title('Previsao de precipiação pluviometrica')
     plt.show()
     return(0)
