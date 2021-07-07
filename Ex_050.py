cont = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c}º número: '))
    if n % 2 == 0:
        cont += n
print()
print(f'A soma dos números pares resulta em {cont}')
