def estudo_media_movel(serie_tempora_chuva):
     import matplotlib.pyplot as plt
     from matplotlib.pylab import rcParams
     media_movel = serie_tempora_chuva.rolling(window=6)
     media_movel =media_movel.mean()
     plt.plot(serie_tempora_chuva, label ='Serie Real')
     plt.plot(media_movel, label ='Média movel 6 meses', color ='red')
     plt.xlabel('Ano')
     plt.ylabel('Preciptação de chuvosa em mm')
     plt.legend(loc ='best')
     plt.title('Média movel semestral')
     plt.savefig('media_movel_serie_temporal.png', dpi =300, format ='png')
     plt.show()
     return(0)