itens = ('Pão', 0.50, 'Suco', 1.25, 'Caderno', 23, 'Borracha', 2, 'Bicicleta', 1099, 'Torradeira', 250.30)
print('='*45)
print(f"{'LISTAGEM DE PREÇOS':^45}")
print('='*45)
for pos, i in enumerate(itens):
    if pos % 2 == 0:
        print(f'{itens[pos]:.<30}R${itens[pos+1]:>13.2f}')
print('='*45)
