ano = int(input('Em que ano você nasceu? '))
idade = 2021 - ano

if idade < 18:
    print(f'Ainda faltam {18 - idade} anos para você se alistar.')
elif idade == 18:
    print(f'Está na hora de você se alistar!')
elif idade > 18:
    print(f'Já se passaram20 {idade - 18} anos desde seu alistamento.')
