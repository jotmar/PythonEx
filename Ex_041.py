print('='*30)
print(f'{"Escola de Natação":^30}')
print('='*30)

idade = 2021 - int(input('Em que ano você nasceu? '))

if idade <= 9:
    print('Sua classificação é MIRIM')
elif idade <= 14:
    print('Sua classifcação é INFANTIL')
elif idade <= 19:
    print('Sua classificação é JÚNIOR')
elif idade <= 20:
    print('Sua classificação é SÊNIOR')
elif idade > 20:
    print('Sua classificação é MASTER')
