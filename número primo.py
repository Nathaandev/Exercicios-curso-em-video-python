n=int(input('Escolha um numero: '))
cont = 0
for c in range (2, n):
    print(f'{c}', end=(' '))
    if n % c == 0:
        
        print(f'Multíplo de {c}')
        cont = cont + 1
if cont == 0:
    print(' Este número é um número primo!')
elif cont>=1:
    print('Este nao é um número primo.')
