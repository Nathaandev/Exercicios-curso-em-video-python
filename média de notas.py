nota1=int(input('Qual foi sua nota na primeira prova? '))
nota2=int(input('Qual foi sua nota na segunda prova? '))
nota= (nota1 + nota2) /2
if nota<5.0:
    print('Sinto muito, você foi reprovado.')
elif 5.0 <= nota <= 6.9:
    print('Você está de recuperação.')
elif nota>6.9:
    print('Aprovado!!')
