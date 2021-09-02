pessoas = []
dados = []
maior = menor = c = 0
while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    if c == 0:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
    dados.append(nome)
    dados.append(peso)
    pessoas.append(dados[:])
    dados.clear()
    c += 1
    op = str(input('Deseja continuar?[S/N] '))
    while op not in 'sSnN':
        print('Opção inválida! Tente novamente.')
        op = str(input('Deseja continuar?[S/N] '))
    if op in 'Nn':
        break
print('='*40)
print(f'Total de pessoas cadastradas: {len(pessoas)}')
print(f'O maior peso foi de {maior:.1f}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso foi de {menor:.1f}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
print()
