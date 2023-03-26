n = 0
cont = 0
maior = 0
menor = 0
soma = 0
continuar = 0
while continuar != 'N':
    n = int(input('Escolha um numero inteiro: '))
    if n > maior:
        maior = n
    if menor == 0 or menor > n:
        menor = n
    soma += n
    cont += 1
    continuar = input('Deseja continuar (S/N)? ').upper()
    while continuar != 'S' and continuar != 'N':
        print('Opção inválida. Por favor, digite S ou N.')
        continuar = input('Deseja continuar (S/N)? ').upper()
    
print(f'Voce digitou {cont} numeros')
print('A media entre os numeros digitados e {:.2f}'.format(soma / cont))
print(f'O maior numero e o {maior} e o maior e o {menor}.')

