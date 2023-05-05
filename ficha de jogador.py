def ficha(nome='', gols=0):
    if nome == "":
        nome = '<desconhecido>'
    if gols == "":
        gols = 0
    print(f'O jogador {nome} fez {gols} gols no campeonato.')


n = input('Qual o nome do jogador? ')
g = input('Quantos gols o jogador fez? ')

ficha(n, g)
