matriz = [[], [], []]
par = coluna3 = 0
for c in range(0, 3):
    for c2 in range(0, 3):
        n = int(input(f'Digite um valor para [{c}, {c2}]'))
        matriz[c].append(n)
        if n % 2 == 0:
            par += n
        if c2 == 2:
            coluna3 += n
print('='*40)
for c in range(0, 3):
    print(f'[ {matriz[c][0]} ][ {matriz[c][1]} ][ {matriz[c][2]} ]')
print('='*40)
print(f"""A soma dos valores pares: {par}
A soma dos valores da terceira coluna: {coluna3}
O maior valor da segunda linha é {max(matriz[1])}""")
