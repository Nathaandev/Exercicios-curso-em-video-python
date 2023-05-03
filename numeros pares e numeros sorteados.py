import random
numeros = []
pares = []
def sorteia():
    for c in range(1,6):      
        numeros.append(random.randint(1,10))
    print(f'Os numeros sorteados foram {numeros}')
def somapar():
    for c in numeros:
        if c % 2 == 0:
            pares.append(c)
    print(f'Os números pares são: {pares} e a soma deles é {sum(pares)}', end=' ')
        

sorteia()
somapar()

