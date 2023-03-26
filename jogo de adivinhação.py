import random
conta = 0
programa=random.randint(0,10)
num = 0
while num != programa:
    num=int(input('Escolha um número: '))
    conta = conta + 1
    if num==programa:
        print('parabéns! nós dois pensamos no número {}!' .format(programa))
    else:
         print('Você errou! eu não pensei no número {}, tente de novo.' .format(num))
print(f'Você conseguiu após {conta} tentativas.')
