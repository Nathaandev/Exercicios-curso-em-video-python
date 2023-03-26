altura=float(input('Insire sua altura: '))
peso=float(input('Insire seu peso: '))
IMC = peso / altura**2
if IMC<18.5:
    print('Seu IMC é {:.2f}, Você está abaixo do peso!'.format(IMC))
elif 18.5<IMC  <=25:
    print('Seu IMC é {:.2f}, Você está no peso ideal!'.format(IMC))
elif 25<IMC <=30:
    print('Seu IMC é {:.2f}, Você está sobrepeso!'.format(IMC))
elif 30<IMC <=40:
    print('Seu IMC é {:.2f}, você tem obesidade!' .format(IMC))
elif IMC>40:
    print('Seu IMC é {:.2f}, você tem obesidade mórbida, se mata seu inútil' .format(IMC))
