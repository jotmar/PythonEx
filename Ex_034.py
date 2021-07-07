sal = float(input('Quanto você recebe? R$'))
if sal > 1250:
    print(f'Você recebeu um aumento e agora seu salário é de R${sal + (sal / 100 * 10):.2f}')
else:
    print(f'Você recebeu um aumento e agora seu salário é de R${sal + sal /100 * 15:.2f}')
