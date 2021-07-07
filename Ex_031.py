km = float(input('Qual é a distância da viagem em km? '))
if km <= 200:
    print(f'O total a ser pago na viagem é de R${km * 0.50:.2f}')
else:
    print(f'O total a ser pago na viagem é de R${km * 0.45:.2f}')
