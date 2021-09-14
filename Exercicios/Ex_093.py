dados = dict()
dados['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
dados['gols'] = []
dados['total'] = 0
for partida in range(1, partidas + 1):
    gols = int(input(f'Quantos gols na partida {partida}? '))
    dados['gols'].append(gols)
    dados['total'] += gols
print('='*60)
print(dados)
print('='*60)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}.')
print('='*60)
print(f'O jogador {dados["nome"]} jogou {partidas} partidas.')
for i, g in enumerate(dados['gols']):
    print(f'     => Na partida {i+1}, fez {g} gols.')
print(f'Foi um total de {dados["total"]} gols.')
