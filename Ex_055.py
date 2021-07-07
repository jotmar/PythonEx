maior_peso = 0
menor_peso = 99999
for c in range(1, 6):
    peso = float(input('Qual é o seu peso atual? '))
    if peso > maior_peso:
        maior_peso = peso
    if peso < menor_peso:
        menor_peso = peso

print(f'O maior peso lido foi: {maior_peso}')
print(f'O menor peso lido foi: {menor_peso}')
