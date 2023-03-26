num=int(input('Escolha um número: '))
num2=int(input('Escolha mais um número: '))
print('''Escolha um sinal
1 | Adição
2 | Subtração
3 | Multiplicação
4 | Divisão
5 | Potencialização
6 | Porcentagem''')
escolha=int(input(' '))
op=print('Sua opção foi {}' .format(escolha))
if escolha == 1:
    print('A soma entre {} e {} é: {}' .format(num, num2, num + num2))

if escolha == 2:
    print('A subtração de {} e {} é: {}' .format(num, num2,num-num2))

if escolha == 3:
    print('A multiplicação de {} e {} é: {}' .format(num,num2,num*num2))

if escolha== 4:
    print('A divisão de {} e {} é: {}' .format(num,num2,num/num2))

if  escolha==5:
    print('A potência de {} ao {} é: {}' .format(num,num2,num**num2))

if escolha==6:
    print(' {}% de {} é: {}' .format(num,num2, num2*num/100))
