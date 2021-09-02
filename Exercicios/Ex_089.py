alunos = list()
boletim = ['a', []]
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    boletim[0] = nome
    boletim[1].append(nota1)
    boletim[1].append(nota2)
    alunos.append(boletim[:])
    boletim = ['a', []]
    op = str(input('Deseja continuar?[S/N] '))
    while op not in 'SsNn':
        print('Opção inválida! Tente novamente.')
        op = str(input('Deseja continuar?[S/N] '))
    if op in 'Nn':
        break
print('='*40)
print(f'{"No.":<6}{"NOME":<15}MÉDIA')
for aluno in alunos:
    print(f'{alunos.index(aluno):<6}{aluno[0]:<15}{(aluno[1][0] + aluno[1][1]) / 2:>5.1f}')
print('='*40)
while True:
    index = int(input('Mostrar notas de qual aluno?(999 Interrompe) '))
    while index > len(alunos) - 1 and index != 999:
        print('Opção Inválida! Tente novamente.')
        index = int(input('Mostrar notas de qual aluno?(999 Interrompe) '))
    if index == 999:
        break
    print(f'Notas de {alunos[index][0]} são {alunos[index][1]}')
    print('='*40)
