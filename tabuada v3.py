
while True :
    n = int(input('Escolha um número: '))
    if n < 0:
        print('Não digite um valor negativo.')
        break
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
