import random


print('''Vamos jogar pedra, papel ou tesoura, escolha um desses 
1 | Pedra
2 | Papel
3 | Tesoura''')
escolhas= ['pedra', 'papel', 'tesoura']
escolha=int(input(''))
ad=random.choice (escolhas)
if escolha == 1 and ad == 'papel':
        print('você escolheu Pedra e eu escolhi papel, papel vence pedra, eu venci essa!')
if escolha == 1 and ad == 'pedra':
        print('Nós escolhemos os mesmos, vamos de novo!')
if escolha == 1 and ad == 'tesoura':
        print('Você escolheu pedra e eu escolhi tesoura, tesoura vence pedra, você venceu essa!')
if escolha == 2 and ad =='papel':
        print('Nos escolhemos o mesmo, vamos de novo!')
if escolha == 2 and ad =='tesoura':
        print('Você escolheu papel e eu escolhi tesoura, tesoura ganha de papel, eu venci essa!')
if escolha == 2 and ad == 'pedra':
        print('Você escolheu papel e eu escolhi pedra, papel ganha de pedra, eu venci essa!')
if escolha == 3 and ad == 'pedra':
        print('você escolheu tesoura e eu escolhi pedra, pedra ganha de tesoura, eu venci essa!')
if escolha == 3 and ad == 'papel':
        print('Você escolheu tesoura e eu escolhi papel, tesoura ganha de papel, você venceu essa!')
if escolha == 3 and ad == 'tesoura':
        print('Nós escolhemos o mesmo, vamos de novo!')
