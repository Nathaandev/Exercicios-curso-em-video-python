import random
usuário = 0
computador = random.randint(1,10)

vitória = 0
while True:
    escolha = int((input('''Escolha ímpar ou par 
1 | ímpar
2 | par
''')))
    if escolha not in (1 , 2):
        print('Apenas 1 e 2 são válidos.')
        continue
    
    if escolha == 2:
        print('Você escolheu Par.')
        print('Eu escolho ímpar.')
        usuário = int(input('Escolha um número: '))
        
        print(f'{usuário} e {computador}.')
        
        if escolha == 2 and usuário + computador in (0,2,4,6,8,10,12,14,16,18,20):
            print(f'{usuário + computador} é um número par, você escolheu par e eu impar, você ganhou.')
            vitória+= 1
        if escolha == 2 and usuário + computador in (1,3,5,7,9,11,13,15,17,19):
            print(f'{usuário + computador} é um número ímpar, como eu escolhi ímpar e você escolheu par, eu ganhei.')
            break
    if escolha == 1:
        print('Você escolheu ímpar')
        print('Eu escolho par')
        usuário = int(input(('Escolha um número: ')))       
        print(f'{usuário} e {computador}.')       
        if escolha == 1 and usuário + computador in (1,3,5,7,9,11,13,15,17,19):
            print(f'{usuário + computador} é um número ímpar, como você escolheu ímpar e eu escolhi par, você ganhou.')
            vitória += 1
        if escolha == 1 and usuário + computador  in (0,2,4,6,8,10,12,14,16,18,20):
            print(f'{usuário + computador} é um número par, como você escolheu ímpar e eu escolhi par, eu venci.')
            break

print(f'Fim. você obteve {vitória} vitórias consecutivas.')

