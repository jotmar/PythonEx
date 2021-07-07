import datetime
ano = int((str(datetime.datetime.now()))[:4])
maior = 0
menor = 0
nas = 0
idade = 0
for c in range(1, 8):
    nas = int(input('Em que ano você nasceu? '))
    if (ano - nas) >= 18:
        maior += 1
    else:
       menor += 1
print(f'Existem {menor} menores de idade e {maior} maiores de idade')
