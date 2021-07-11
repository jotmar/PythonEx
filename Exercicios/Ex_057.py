while True:
    sexo = str(input('Qual é o seu sexo?[M/F]')).upper()
    if sexo == 'M' or sexo == 'F':
        break
    else:
        print('Valor inválido! por favor tente novamente.')
print('Sexo Registrado com sucesso!')
