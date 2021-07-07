print('Crie um triângulo!\n')
l1 = float(input('Qual o tamanho do primeiro lado? '))
l2 = float(input('Qual o tamanho do segundo lado? '))
l3 = float(input('Qual o tamanho do terceiro lado? '))
if l1 > l2 + l3 or l2 > l1 + l3 or l3 > l2 + l1:
    print('Não é possivel criar um triângulo!')
elif l1 == l2 and l2 == l3:
    print('É possivel criar um triângulo Equilátero!')
elif l1 == l2 or l2 == l3 or l1 == l3:
    print('É possível criar um triângulo Isós4celes!')
elif l1 != l2 and l1 != l3 and l2 != l3:
    print('É possivel criar um triângulo Escaleno!')
