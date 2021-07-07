from math import sqrt, pow
catoposto = float(input('Qual é o comprimento do cateto oposto? '))
catadjacente = float(input('Qual é o comprimento do catero adjacente? '))
print(f'O comprimento da hipotenusa é {sqrt(pow(catadjacente, 2) + pow(catoposto, 2)):.2f}')
