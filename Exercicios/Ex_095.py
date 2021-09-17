cadastrados = list()
dados = dict()
code = 0
while True:
    dados['code'] = code
    dados['nome'] = str(input('Nome do Jogador: ')).strip()
    partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    dados['gols'] = []
    dados['total'] = 0
    for p in range(0, partidas):
        gols = int(input(f'Quantos gols na partida {p+1}? '))
        dados['gols'].append(gols)
        dados['total'] += gols
    cadastrados.append(dados.copy())
    code += 1
    op = str(input('Deseja continuar?[S/N] ')).strip()
    while op not in 'SsNn':
        print('Opção Inválida. Tente novamente.')
        op = str(input('Deseja continuar?[S/N] ')).strip()
    if op in 'Nn':
        break
    print('='*60)
print('='*60)
print(f'{"code":<5}{"nome":<15}{"gols":<25}{"total"}')
print('='*60)
for p in cadastrados:
    print(f'{str(p["code"]):>4} {str(p["nome"]):<15}{str(p["gols"]):<25}{(p["total"])}')
print('='*60)
while True:
    jogador = int(input('Mostrar dados de qual jogador? '))
    while jogador < 0 and jogador != 999 or jogador > len(cadastrados) and jogador != 999:
        print(f'Não existe jogador com o código {jogador}! Tente novamente.')
        jogador = int(input('Mostrar dados de qual jogador? '))
    if jogador == 999:
        break
    print(f'-- LEVANTAMENTO DO JOGADOR {cadastrados[jogador]["nome"]}:')
    for i, g in enumerate(cadastrados[jogador]['gols']):
        print(f'   No jogo {i+1} fez {g} gols.')
    print('='*60)
print(f'{"<<<ENCERRADO>>>":^60}')
