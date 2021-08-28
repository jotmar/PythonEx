from abc import abstractproperty


numbers = list()
pares = list()
impares = list()
while True:
    num = int(input('Digite um valor: '))
    numbers.append(num)
    op = str(input('Deseja continuar?[S/N] '))
    while op not in 'SsNn':
        print('Valor inválido! Tente novamente.')
        op = str(input('Deseja continuar?[S/N] '))
    if op in 'Nn':
        break
for n in numbers:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print('='*40)
print(f"""Lista completa: {numbers}
Lista dos números pares: {pares}
Lista dos números ímpares: {impares}""")
