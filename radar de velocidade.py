carro=float(input('Tem um radar por perto, qual a velocidade do carro? '))

if carro > 80:
    multa=(carro-80) *7
    print('Você foi multado e terá que pagar uma multa de {:.2f} R$!' .format(multa))
    
else: 
    print('Tenha um bom dia!')
