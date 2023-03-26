num=int(input('Escolha um número inteiro: '))
print('''Escolha uma das bases para conversão 
1 | Converter para BINÁRIO
2 | Converter para OCTAL
3 | Converter para HEXADECIMAL''')
op=int(input(' ' ))
print(('Sua opção foi {}' .format(op)))

if op == 1:
    print('O numero {} convertido para binário é {}' .format(num, bin(num)[2:]))

elif op == 2:
    print('O número {} convertido para octal é {}' .format(num, oct(num)[2:]))

elif op == 3:
    print('O número {} convertido para hexadecimal é {} ' .format(num, hex(num)[2:]))

else: 
    print('Opção invalida, use 1, 2 ou 3.')
