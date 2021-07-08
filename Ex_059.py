from time import sleep
from typing import Optional
while True:
    print('='*30)
    n1 = int(input('Primeiro número: '))
    n2 = int(input('Segundo número: '))
    print('='*30)
    print()
    print("""O que deseja fazer?

[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa

""")
    while True:
        option = int(input('Qual é a sua escolha? '))
        print()
        if option > 5 and option < 1:
            print('Valor Inválido! Por favor tente novamete.')
        else:
            break
    if option == 1:
        print(f'A soma entre {n1} e {n2} resulta no número {n1 + n2}')
    elif option == 2:
        print(f'O produto dos fatores {n1} e {n2} é {n1 * n2}')
    elif option == 4:
        print('Escolha os números novamente')       
    elif option == 5:
        print('Encerrando...')
        sleep(2.5)
        break
