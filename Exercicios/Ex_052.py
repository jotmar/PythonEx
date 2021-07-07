a = int(input('Digite um número inteiro: '))
tot = 0
for c in range(1, a+1):
    if a % c == 0:
        tot += 1
        print('\033[32m', end=' ')
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print('\033[m')
if tot != 2:
    print(f'O número {a} foi dividido {tot} vezes, portanto não é Primo')
else:
    print(f'O número {a} é Primo')
