km=float(input('Quantos km você rodou? '))

dias=float(input('Por quantos dias você usou o carro? '))

diaria=60*dias

rodado=15*km

total=diaria+rodado


print('Você rodou por {} dias, então são {} Reais da diária, você rodou {} km, então, são {} reais pelos quilômetros andados, no total, o aluguel fica {} Reais. ' .format(dias, diaria, km, rodado, total))
