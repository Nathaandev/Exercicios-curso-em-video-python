maior = 0
menor = 0
for c in range(0,5):
    peso=float(input('Digite o Peso: ' .format(c)))
    if peso > maior:
        maior = peso
    if menor == 0 or menor > peso:
        menor = peso
print('O maior peso foi {} e o menor foi {}.' .format(maior, menor))
