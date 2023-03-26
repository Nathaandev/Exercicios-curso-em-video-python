import os
sair = 5
escolha = 0
n1=int(input('Escolha um número: '))
n2=int(input('Escolha outro número: '))

print('''Selecione uma das opções.
 1 | Somar
 2 | Maior
 3 | Multiplicar
 4 | Novos números
 5 | Sair do programa   ''')

while escolha != 5:
    escolha=int(input(': '))
    if escolha == 1:
        print(f'Você escolheu somar \n a soma de {n1} + {n2} é = {n1+n2}')
            
    if escolha == 2 and n1>n2 :
        print(f'Entre {n1} e {n2}, o maior valor é {n1}')
    if escolha == 2 and n2>n1:
        print(f'entre {n1} e {n2}, o maior valor é {n2}')

   
    if escolha == 3:
        print(f'Você escolheu multiplicar. \n {n1} x {n2} é = {n1 * n2}')
       
    if escolha == 4:
        print('Você escolheu inserir novos números.')
        n1=int(input('Insire o novo valor: '))
        n2=int(input('Insire o outro novo valor: '))
        print('''Selecione uma das opções.
 1 | Somar
 2 | Maior
 3 | Multiplicar
 4 | Novos números
 5 | Sair do programa   ''')


    if escolha == 5:
        print('Finalizando...')
     

