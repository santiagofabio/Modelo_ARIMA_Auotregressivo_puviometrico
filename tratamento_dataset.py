def tratamento_dataset(data_set):
     import pandas as pd
            
     data_set = data_set.apply(lambda x:x.str.replace(',','.') )

     #Tratamento de valores faltantes
     data_set['Janeiro']=pd.to_numeric(data_set['Janeiro'].str.replace('---','305.79'))
     data_set['Fevereiro']=pd.to_numeric(data_set['Fevereiro'].str.replace('---','249.3'))
     data_set['Março']=pd.to_numeric(data_set['Março'].str.replace('---','227.97'))
     data_set['Abril']=pd.to_numeric(data_set['Abril'].str.replace('---','93.64'))
     data_set['Maio']=pd.to_numeric(data_set['Maio'].str.replace('---','86.67'))
     data_set['Junho']=pd.to_numeric(data_set['Junho'].str.replace('---','59.66'))
     data_set['Julho']=pd.to_numeric(data_set['Julho'].str.replace('---','54.6'))
     data_set['Agosto']=pd.to_numeric(data_set['Agosto'].str.replace('---','27.85'))
     data_set['Setembro']=pd.to_numeric(data_set['Setembro'].str.replace('---','83.8'))
     data_set['Outubro']=pd.to_numeric(data_set['Outubro'].str.replace('---','139.89'))
     data_set['Novembro']=pd.to_numeric(data_set['Novembro'].str.replace('---','145.04'))
     data_set['Dezembro']=pd.to_numeric(data_set['Dezembro'].str.replace('---','236.04'))
     print(f'{data_set.dtypes}')
     data_set=data_set.drop([36,37])
     data_set.to_csv('data_set_tratado.csv', index =False)    
     return(0)
     