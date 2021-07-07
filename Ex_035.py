print('Crie um triângulo!')
l1 = int(input('Medida do primeiro lado: '))
l2 = int(input('Medida do segundo lado: '))
l3 = int(input('Medida do terceiro lado: '))
if l1 > l2 + l3 or l2 > l1 + l3 or l3 > l2 + l1:
    print('Não é possivel formar um triângulo!')
else:
    print('É possivel criar um triângulo!')
