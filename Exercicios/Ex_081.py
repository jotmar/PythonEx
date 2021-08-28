numbers = list()
while True:
    n = int(input('Digite um valor: '))
    numbers.append(n)
    op = str(input('Deseja continuar?[S/N] '))
    while op not in 'SsNn':
        print('Valor inválido! Tente Novamente.')
        op = str(input('Deseja continuar?[S/N] '))
    if op in 'Nn':
        break
numbers.sort(reverse=True)
print('='*40)
print(f"""Quantidade de números digitados: {len(numbers)}
Lista ordenada de forma decrescente: {numbers}""")
if 5 in numbers:
    print('O número 5 foi digitado nas posições: ', end='')
    for pos, n in enumerate(numbers):
        if n == 5:
            print(f'{pos}... ', end='')
    print()
else:
    print('O número 5 não está na lista.')
