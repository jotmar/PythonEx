from random import randint
victory = 0

print('='*50)
print(f'{"PAR OU ÍMPAR":^50}')
print('='*50)
while True:
    pc = randint(1, 10)
    while True: 
        escolha = str(input('Qual você escolhe?[P/I]: ')).strip().upper()
        if escolha not in ['P', 'PAR', 'I', 'IMPAR', 'ÍMPAR']:
            print('Valor Inválido! Tente novamente.')
        else:
            break 
    num = int(input('Qual número vai jogar? '))
    if (pc + num) % 2 == 0:
        resul = ['P', 'PAR']
        resul_text = 'Par'
    else:
        resul = ['I', 'IMPAR', 'ÍMPAR']
        resul_text = 'Ímpar'
    print('-='*30)
    print(f'Você jogou {num} e o computador {pc} e o total foi {num + pc} portanto deu {resul_text}')
    if escolha in resul:
        print('\033[32mVocê Ganhou! Continue jogando...\033[m')
        victory += 1
    else:
        print('\033[31mVocê perdeu!\033[m')
        break
    print()
print(f'Total de vitórias: {victory}')
