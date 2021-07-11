p1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
cont = 10
while cont != 0:
    print(f'{p1}')
    p1 += r
    cont -= 1
    if cont == 0:
        cont += int(input('Deseja contar mais quantos termos? '))
print('A PA acabou!')
