mais_barato = float('inf')
nome_barato = None
contador = 0
total = 0
mais_1000 = 0
while True:
    
    nome = input('Digite o nome de um produto: ')
    preço = float(input('Digite o preço de um produto: '))
    if preço > 1000:
        mais_1000 += 1
    total += preço
    contador += 1  
    if contador == 0:
        mais_barato = preço
        nome_barato = nome
    continuar = input('Quer continuar? S/N ').lower()
    if continuar not in ('s', 'n'):
        print('Digite apenas S ou N.')
        break
    if continuar == 'n':
        print('Fechando programa...')
        break
    if continuar == 's':
        print('Continuando...')
    if preço < mais_barato:
        mais_barato = preço
        nome_barato= nome
print(f'O mais barato foi {nome_barato}, custando R${mais_barato}.\nO total gasto na compra foi de R${total}\n{mais_1000} produtos custam mais que R$1000.')    
