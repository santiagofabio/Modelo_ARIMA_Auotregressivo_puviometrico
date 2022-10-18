def testa_hipotese_shapiro_wilk(value_p, alpha):
     #Shapiro-Wilk test
     # The Shapiro-Wilk test 
     # tests the null hypothesis that the data was drawn from a normal distribution.This function returns a test statistic and a corresponding p-value.
     # the alternative hypothesiss the data not was draw from a normal distribution
     # If the p-value is below a certain significance level,
     # then we have sufficient evidence to say that the sample data 
     # does not come from a normal distribution 
     print(f'Resultado Shapiro-Wilk test:')
     if value_p>alpha:
         print(f'Os dados da serie se distribuem normalmente')
     else:
         print(f'Não temos evidência de uma distribuição normal')

     print(f'---------------------------')
    
     return(0)
