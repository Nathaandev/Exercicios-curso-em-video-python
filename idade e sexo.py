menores_de_20 = 0
homens = 0
mais_18 = 0
while True:
    idade=int(input('Digite a idade de uma pessoa: '))
    sexo=input('Digite o sexo de uma pessoa (M/F) : ').lower()
    if sexo not in ('m', 'f'):
        print('Digite M para masculino e F para feminino.')
        break
    continuar=input('Quer continuar? (S/N) ').lower()
    if continuar not in('n', 's'):
        print('Use n ou s.')
        break
    if continuar == 'n':
        break
    if sexo == 'f' and idade<20:
        menores_de_20 += 1
    if sexo == 'm':
        homens += 1
    if idade>18:
        mais_18 += 1
print(f'''{mais_18} pessoas tem mais de 18 anos.\n{homens} homens foram cadastrados.\n{menores_de_20} mulheres tem menos de 20 anos.''')
