from random import randint
from time import sleep


def sorteio(lista):
    print('Sorteando valores para a lista... ', end='')
    for n in range(0, 5):
        rand = randint(1, 10)
        print(rand, end=' ', flush=True)
        sleep(0.5)
        lista.append(rand)
    print('PRONTO!')


def SomaPar(lista):
    par = 0
    for v in lista:
        if v % 2 == 0:
            par += v
    print(f'Somando os valores pares de {lista}, temos {par}')


numeros = list()
print('='*50)
sorteio(numeros)
SomaPar(numeros)
