aluguel = int(input('Quantos dias aluguados? '))
km = float(input('Quantos km rodados? '))
print(f'O total a pagar é R${(aluguel * 60) + (km * 0.15):.2f}')
