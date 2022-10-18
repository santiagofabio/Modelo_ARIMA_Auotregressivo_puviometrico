
#Modelo da séries temporais - ARIMA
 **ARIMA:** Modelos autorregressivos integrados e de médias móveis 
 **Objetivo:** Implementação do modelo autorregressivo  de series temporais diposnível na biblioteca __statsmodels.tsa.arima.model__,  a fim de se determinar precipitação chuvosa.

 ## Modelos Uitlizados
 **Autorregressivo(AR):**  indica que a variável é regressada em seus valores anteriores. 
 
 **Parâmetros ARIMA (p, d, q):**
    - p = ordem da autorregressão.
    - d = grau de diferenciação.
    - q = ordem da média móvel.(Combinação linear de erros passados)


### Série temporal estudada
1. Série temporal
![serie_temporal_estudada](serie_temporal_estudada.png )
1.1 Média movel sete dias serie temporal.
![media_movel_serie_temporal](media_movel_serie_temporal.png )
1.2 Série tempora decomposta.
![serie_temporal_decomposta](serie_temporal_decomposta.png )

2. Transformação raíz cubica sobre a série
2.1 Série transformada
![serie_raiz_cubica](serie_raiz_cubica.png )
2.2  Quantile-Quantile Plot -Série raíz cúbica
![nomral_qq_plt_serie_raiz_cubica](nomral_qq_plt_serie_raiz_cubica.png) 
2.3  Autocorrelation Function -Série raíz cúbica
![autocorrelacao_raiz_cubica](autocorrelacao_raiz_cubica.png) 
2.4 Partial Autocorrelation Function-Série raíz cúbica
![parcial_autocorrelacao](parcial_autocorrelacao.png )

3. Aplicação Modelo Autoregressivo
3.1 Estudo dos resíduos
![residuos_modelo_ar](residuos_modelo_ar.png)

3.2 Quantile-Quantile Plot-Rediduo -Modelo AR
![Quantile-Quantile Plot-Rediduo Série raíz cúbica](nomral_qq_plot_residuos_modelo_ar.png) 

3.3 Autocorrelation Function-Resíduos -Modelo AR.
![nomral_qq_plt_serie_raiz_cubica](autocorrelacao_residuos_modelo_ar.png)

3.4. Partial Autocorrelation Function -Resíduos- -Modelo AR.
![Parcial autocorreção residuos](parcial_autocorrelacao_residuos_modelo_ar.png)

4 Resultados

4.1 Série e resíduos
![seire_e_residuos](seire_e_residuos.png)


4.1 Previsão.
![previsao_final](previsao_final.png)