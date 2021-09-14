from random import randint
from time import sleep
cont = 1
jogadores = {'jogador1':randint(1, 6), 'jogador2':randint(1,6), 'jogador3':randint(1, 6), 'jogador4':randint(1, 6)}

print('='*30)
print(f'{"Jogadores Sorteados":^30}')
print('='*30)
for jogador, v in jogadores.items():
    print(f'    O {jogador} tirou {v}')
    sleep(1)
print('='*30)
print(f'{"Ranking dos Jogadores":^30}')
print('='*30)
for i in sorted(jogadores, key=jogadores.get, reverse=True):
    print(f'    {cont}⁰ lugar: {i} com {jogadores[i]}')
    cont += 1
    sleep(1)
