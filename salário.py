salario=float(input('Qual o seu salário atual? '))
a1 = salario*10 / 100
a2 = salario*15 / 100

if salario >= 1250:
    final = a1 + salario
    print('Seu aumento de salário será de {} R$ e ficará {} R$! '.format(a1, final) )

else:
    final = a2 + salario
    print('Seu aumento de salário será de {} R$ e ficará {} R$! ' .format(a2, final))
