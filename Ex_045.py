from time import sleep
from random import randint
pc = randint(0, 2)
lista = ['PEDRA', 'PAPEL', 'TESOURA']
print('='*30)
print(f'\033[32m{"JOKENPÔ":^30}\033[m')
print('='*30)
print("""
[1] PEDRA
[2] PAPEL
[3] TESOURA
""")
op = int(input('Qual vai jogar? ')) - 1
if op >= 0 and op <= 2:
    print()
    print('O jogo vai começar...')
    print('='*30)
    sleep(1.5)
    print('\033[1mJO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!\033[m')
    print('='*30)
    if pc == op:
        sit = '\033[33mEMPATE!\033[m'
    elif pc == 0 and op == 2 or pc == 1 and op == 0 or pc == 2 and op == 1:
        sit = '\033[31mVOCÊ PERDEU!\033[m'
    elif op == 0 and pc == 2 or op == 1 and pc == 0 or op == 2 and pc == 1:
        sit = '\033[32mVOCÊ GANHOU!\033[m'
    print(f'O COMPUTADOR ESCOLHEU {lista[pc]}')
    print(f'VOCÊ ESCOLHEU {lista[op]}')
    print(f'PORTANTO, {sit}')
else:
    print('Opção Inválida!')
