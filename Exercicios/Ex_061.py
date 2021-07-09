p1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
cont = 0
while cont != 10:
    print(f'{p1}', end=', ')
    p1 += r
    cont += 1
print('Aqui estão os 10 primeiros termos')
