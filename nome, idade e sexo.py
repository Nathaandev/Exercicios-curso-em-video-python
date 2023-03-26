idades = []
cont = 0
mais_velho = 0
homens = []
nomevelho = 0

for c in range(1,5):
    nome=input((f'Insira o nome da {c}° pessoa: '))
    idade=int(input(f'Insira a idade da {c}° pessoa: '))
    idades.append(idade)
    sexo=input((f'Insira o sexo da {c}° pessoa M/F: '))
    if sexo == 'M':
        if c == 1:
            mais_velho = idade
            nomevelho = nome
        if sexo in 'Mm' and idade > mais_velho:
            mais_velho = idade
            nomevelho = nome


    if sexo == 'F':
        if idade<20:
            cont = cont + 1
