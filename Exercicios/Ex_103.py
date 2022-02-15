def ficha(nome='<desconhecido>:', gols=0):
    if nome == '':
        nome = '<desconhecido>'
    if gols.isnumeric() == False:
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

n = str(input('Nome do Jogador: ')).strip()
g = str(input('Número de gols: ')).strip()
ficha(n, g),
