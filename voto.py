def voto(a):
    idade = 2023 - a
    if idade < 18:
        print('NÃO VOTA.')
    if  70 > idade >= 18 :
        print('VOTO OBRIGATÓRIO')
    if idade >= 70:
        print('VOTO OPCIONAL.')

ano = int(input('Qual seu ano de nascimento: '))
voto(ano)

