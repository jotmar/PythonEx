from datetime import datetime
ano = int(str(datetime.today())[:4])
pessoa = dict()
pessoa['nome'] = str(input('Digite seu nome: '))
pessoa['idade'] = ano - int(input('Ano de nascimento: '))
pessoa['ctps'] = int(input('Carteira de trabalho (0 = não tem): '))
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = pessoa['idade'] + (35 - (ano - pessoa['contratação']))
print('='*60)
print(f'{pessoa}')
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')
