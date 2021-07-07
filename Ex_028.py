from random import randint
n1 = randint(0, 5)
print('='*30)
print(f"{'Adivinhação':^30}")
print('='*30)
escolha = int(input('Estou pensando em um número de 0 a 5 que número é este? '))
if escolha == n1:
    print('Parabéns você acertou!!!')
else:
    print('Que pena, você errou.')
