homens = mulher_menor20 = mais18 = 0
print('-='*30)
print(f'{"CADASTRO DE PESSOAS":^60}')
print('-='*30)
while True:
    idade = int(input('Idade: '))
    while True:
        sexo = str(input('Sexo[M/F]: ')).strip().upper()
        if sexo not in ['M', 'F', 'MASCULINO', 'FEMININO']:
            print('Valor Inválido! Tente novamente.')
        else:
            break
    if idade >= 18:
        mais18 += 1
    if sexo in ['F', 'FEMININO'] and idade < 20:
        mulher_menor20 += 1
    if sexo in ['M', 'MASCULINO']:
        homens += 1
    print('-='*30)
    while True:
        op = str(input('Deseja continuar[S/N]: ')).strip().upper()
        if op not in ['S', 'SIM', 'N', 'NAO', 'NÃO']:
            print('Valor Inválido! Tente novamente.')
        else:
            break
    print('-='*30)
    if op not in ['S', 'SIM']:
        break
print(f'Total de pessoas com mais de 18 anos: {mais18}')
print(f'Total de homens cadastrados: {homens}')
print(f'Total de mulheres com menos de 20 anos: {mulher_menor20}')
print('Programa Finalizado.')
