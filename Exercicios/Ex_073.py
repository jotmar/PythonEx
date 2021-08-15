#Com base nos dados do dia 15/08/2021

times = ('Atlético-MG', 'Palmeiras', 'Fortaleza', 'Bragantino', 'Flamengo', 'Atlético-PR', 'Ceará SC', 'Bahia', 'Santos', 'Corinthians', 'Atlético-GO', 'Juventude', 'Internacional', 'São Paulo', 'Fluminense', 'Sport', 'Cuiabá', 'América-MG', 'Grêmio', 'Chapecoense')

print('Cinco primeiros colocados:')
print(times[:5])
print('='*30)
print('Quatro últimos colocados:')
print(times[-4:])
print('='*30)
print('Times em ordem alfabética:')
print(sorted(times))
print('='*30)
print('Posição da Chapecoense:')
print(f'{times.index("Chapecoense") + 1}º Colocado.')
