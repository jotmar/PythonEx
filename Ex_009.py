print('='*30)
print(f'{"Tabuada":^30}')
print('='*30)
n1 = int(input('Qual é o número da Tabuada? '))
cont = 1
print('&'*30)
while cont != 11:
    print(f"{f'{n1} X {cont} = {n1 * cont}': ^30}")
    cont += 1
print('&'*30)
