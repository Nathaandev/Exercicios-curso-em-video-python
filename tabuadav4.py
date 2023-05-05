def tabuada(num, fim):
    for c in range(1,fim+1):
        tab = num * c
        print(f'{num} x {c} = {tab}')

n = int(input('Escolha um número: '))
f = int(input('Você quer uma tabuada de {n} até onde? '))
tabuada(n,f)

