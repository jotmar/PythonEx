numbers = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numbers:
        numbers.append(n)
    else:
        print('Número Duplicado! Não irei adicionar.')
    op = str(input('Deseja continuar?[S/N] '))
    while op not in 'SsNn':
        print('Digite uma opção válida.')
        op = str(input('Deseja continuar?[S/N] '))
    if op in 'Nn':
        break
numbers.sort()
print('=' * 40)
print(f'Você digitou os seguintes valores: {numbers}')
