cont = 0
cont2 = 0
for c in range(1, 8):
    ano=int(input('Digite seu ano de nascimento: '))
    ano_atual = 2023
    idade = ano_atual - ano
    if idade<21:
       cont =  cont + 1
    elif idade>21:
        cont2 = cont2 + 1
print('{} Pessoas ainda não atingiram a maioridade e {} são maiores de idade.'.format(cont, cont2))
