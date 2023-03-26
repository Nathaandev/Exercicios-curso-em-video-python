primeira = int(input('Insire a primeira razão: '))
razao = int(input('Insire a razão: '))
c = 1
termo = primeira
while c <= 10:
    print(f'{termo} ->', end=' ')
    termo = termo + razao
    c = c + 1
print('Fim.')
