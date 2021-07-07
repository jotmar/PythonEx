p1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
print(p1, end=', ')
for c in range(1, 10):
    p1 += r
    print(p1, end=', ')
print('Acabou!')