nota50 = nota20 = nota10 = nota1 = 0
cedulas = [50, 20, 10, 1]
print('='*50)
print(f'{"CAIXA ELETRÔNICO":^50}')
print('='*50)
saque = float(input('Quanto você deseja sacar? R$'))
while True:
    if saque - cedulas[0] >= 0:
        nota50 += 1
        saque -= cedulas[0]
    elif saque - cedulas[1] >= 0:
        nota20 += 1
        saque -= cedulas[1]
    elif saque - cedulas[2] >= 0:
        nota10 += 1
        saque -= cedulas[2]
    elif saque - cedulas[3] >= 0:
        nota1 += 1
        saque -= cedulas[3]
    if saque == 0:
        break
print(f'Cédulas de R$50: {nota50}\n' if nota50 != 0 else '', end='')
print(f'Cédulas de R$20: {nota20}\n' if nota20 != 0 else '', end='')
print(f'Cédulas de R$10: {nota20}\n' if nota10 != 0 else '', end='')
print(f'Cédulas de R$1: {nota1}\n' if nota1 != 0 else '', end='')
