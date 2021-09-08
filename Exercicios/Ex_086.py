matriz = [[], [], []]
for c in range(0, 3):
    for c2 in range(0, 3):
        n = int(input(f'Digite um valor para [{c}, {c2}]: '))
        matriz[c].append(n)
print('='*30)
for c in range(0, 3):
    print(f'[{matriz[c][0]:^5}][{matriz[c][1]:^5}][{matriz[c][2]:^5}]')
