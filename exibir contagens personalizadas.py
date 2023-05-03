from time import sleep
def contador(i, f, p):
    for c in range(1, 11, 1):
        print(c,  end=' ')
        
    print('FIM')
    for r in range(10, 0, -2):
        print(r, end=' ')
        
    print('FIM')
    for t in range(i, f+1, -p):
        print(f'{t}', end=' '  )
        
    print('FIM')
        


i = int(input('Onde irá começar? '))
f = int(input('Onde irá terminar? '))
p = int(input('De quantos em quantos irá pular? '))
if p == 0:
    p = 1
contador(i,f,p)
