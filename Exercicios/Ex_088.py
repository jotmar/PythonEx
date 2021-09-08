from random import randint
from time import sleep
jogo = list()
print('='*40)
print(f'{"JOGO DA MEGA SENA":^40}')
print('='*40)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'{f" SORTEANDO {quant} JOGOS ":=^40}')
sleep(1.5)
for c in range(0, quant):
    for c2 in range(0, 6):
        n = randint(1, 61)
        while n in jogo:
            n = randint(1, 60)
        jogo.append(n)
    jogo.sort()
    print(f'Jogo {c+1}: {jogo}')
    sleep(1)
    jogo.clear()
print(f'{" BOA SORTE! ":=^40}')
