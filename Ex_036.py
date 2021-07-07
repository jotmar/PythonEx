print('\033[33m=\033[m'*30)
print(f'\033[32m{"Empréstimo":^30}\033[m')
print('\033[33m=\033[m'*30)

vcasa = float(input('Qual o valor da casa? '))
sal = float(input('Quanto você recebe de salário? '))
years = int(input('Em quantos anos deseja pagar a casa? '))
vparcela = vcasa / (years*12)
limite = sal * 30 / 100
#O valor da parcela não pode exceder 30% do salário.
if vparcela < limite:
    print('Foi um prazer fazer empréstimos com você! Obrigado volte sempre.')
else:
    print(f'Infelizmente o empréstimo não pode ser concluído, pois \no valor da parcela R${vparcela:.2f} excede 30% do seu salário R${limite:.2f}')
