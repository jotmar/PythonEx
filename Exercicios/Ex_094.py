cadastrados = list()
dados = dict()
media = 0
while True:
    dados['nome'] = str(input('Nome: ')).strip()
    dados['sexo'] = str(input('Sexo[M/F]: ')).strip()
    while dados['sexo'] not in 'MmFf':
        print('Opção Inválida! Tente novamente.')
        dados['sexo'] = str(input('Sexo[M/F]: ')).strip()
    dados['idade'] = int(input('Idade: '))
    media += dados['idade']
    cadastrados.append(dados.copy())
    op = str(input('Deseja continuar?[S/N] ')).strip()
    while op not in 'SsNn':
        print('Opção Inválida! Tente novamente.')
        op = str(input('Deseja continuar?[S/N] ')).strip()
    if op in 'Nn':
        break

print('='*60)
print(f'Total de pessoas cadastradas: {len(cadastrados)}')
print(f'Média de idade do grupo: {media / len(cadastrados)}')
print(f'Mulheres do grupo: ', end='')
for p in cadastrados:
    if p['sexo'] in 'Ff':
        print(p['nome'], end=' ')
print()
print('Lista de pessoas que estão acima da média:')
print('=' * 60)
for p in cadastrados:
    if p['idade'] > (media / len(cadastrados)):
        for k, v in p.items():
            print(f'{k} = {v};', end=' ')
        print()
print('=' * 60)
