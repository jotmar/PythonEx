seq = int(input('Digite o tamanho da sequência de fibonacci: ')) - 1
start = 1
ant = 0
ant2 = 0
print('0', end=', ' )
while seq != 0:
    print(f'{start}', end=', ')
    ant = start
    start += ant2
    ant2 = ant
    seq -= 1
    if seq == 0:
        print('PAUSE...')
        seq += int(input('Deseja mostrar mais quantos elementos da sequência? '))
print('Programa Finalizado!')
