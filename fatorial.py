
n=int(input('Digite um numero para calcular seu fatorial: '))
c = n 
f = 1
print(f'Calculando {n}! =  ', end='')
while c > 0 :
    
    print(f'{c}', end='')
    print(' x ' if c >= 1 else ' = ', end='')  
    f =f * c
    c = c - 1 
print(f'{f}', end='')
   


    
