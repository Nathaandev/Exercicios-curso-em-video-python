n = 0
cont = soma = 0
while n != 999:
    n = int(input('Digite um número (999 para parar): '))   
    if n == 999:
        break
    cont += 1
    soma += n
    
print(f'Você digitou 999 que é o ponto de parada.\nA soma dos números digitados é {soma}.\n Você digitou {cont} números.')

