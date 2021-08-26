from random import randint
#maior = menor = 0
random_num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))


#for c, n in enumerate(random_num):
#    if c == 0:
#        maior = menor = n
#    if n > maior:
#        maior = n
#    if n < menor:
#        menor = n


print('Os valores sorteados foram: ', end='')
for n in random_num:
    print(n, end=' ')
print()
print(f"""Maior número: {max(random_num)}
Menor número: {min(random_num)}
""")
