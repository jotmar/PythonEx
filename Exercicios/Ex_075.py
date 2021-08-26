n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))
n4 = int(input('Quarto número: '))
numbers = (n1, n2, n3, n4)
times9 = numbers.count(9)
pares = 0
print(f'O número 9 apareceu {times9} vezes.')
if 3 in numbers:
    first3 = numbers.index(3)
    print(f'O número 3 apareceu pela primeira vez na posição {first3 + 1}')
else:
    print('O número 3 não apareceu nenhuma vez.')
print('Os valores pares digitados foram: ', end='')
for n in numbers:
    if n % 2 == 0:
        print(n, end=' ')
        pares += 1
print('' if pares != 0 else 'Nenhum')
