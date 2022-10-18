from pyparsing import alphas


def testa_hipotese_kpss(p_value,crit, alpha):
     #Estacionaridade 
     #----------------------Teste KPSS--------------- 
     #H0: = 0 (o modelo não possui raiz unitária, a série é estacionária);
     #H1: > 0 (o modelo possui raiz unitária, a série não é estacionária). 
     # Value_p > alpha, Deve-se aceitar H0
     print(f'Resultado KPSS teste:')
     for chave, valor in crit.items():
     #print('{} :{:.4} '.format(chave, valor))
         if p_value>alpha: 
             print('Ao nivel de significancia {:.5f} e valor critico {:.5f} a serie é estacionaria'.format( alpha ,valor))
             print('Value_p {:.5f}'.format( p_value ))
         else: 
              print('Não ha evidencia  de estacionaridade ao nivel de significancia {:.5f} e valor critico {:.5f}'.format( alpha ,valor))
              print('Value_p {:.5f}'.format( p_value ))

     return(0)