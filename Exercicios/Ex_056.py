menor_twenty = 0
mais_velho = ''
mais_velho_idade = 0
media_idade = 0
print('='*30)
for c in range(4):
    nome = str(input('Qual é o seu nome? ')).strip()
    idade = int(input('Quantos anos você tem? '))
    print("""[1] Masculino
[2] Feminino""")
    sexo = int(input('Qual é o seu sexo? '))
    media_idade += idade
    if idade > mais_velho_idade and sexo == 1:
        mais_velho_idade = idade
        mais_velho = nome
    if sexo == 2 and idade < 20:
        menor_twenty += 1
    print('='*30)
if mais_velho == '':
    mais_velho = 'Nenhum'
print(f"""Média de Idade do grupo: {media_idade / 4:.0f}
Homem mais velho: {mais_velho}
Quantas mulheres menores de 20 anos: {menor_twenty}
""")
