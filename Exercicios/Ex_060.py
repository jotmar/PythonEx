print('='*30)
print(f'{"Cálculo do fatorial":^30}')
print('='*30)
num = int(input('Número para calcular seu fatorial: '))
fatorial = num
while num != 1:
    print(f'{num} x ', end='')
    num -= 1
    fatorial *= num
print(f'1 = {fatorial}')
