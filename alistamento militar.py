nascimento=int(input('Em que ano você nasceu? '))
idade= 2023 - nascimento
alistamento= 18
faltam= idade - alistamento
ano=2023 - faltam
if idade < alistamento:
    print('Quem nasceu em {} terá seu alistamento em {}!' .format(nascimento, ano) )

elif idade == alistamento :
    print('Quem nasceu em {} tem que se alistar agora! ' .format(ano))

elif idade > alistamento:
    print('Já passou sua hora de se alistar há {} anos, em {}!' .format(idade-alistamento, ano))
