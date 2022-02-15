def ajuda(comando):
    help(comando)


def format_linha(txt, cor='35'):
    print(f'\033[{cor}m')
    print('=' * (len(txt) + 4))
    print(f'  {txt}')
    print('=' * (len(txt) + 4))
    print(f'\033[m')


def pyhelp():
    from time import sleep
    search = ''
    while search != 'fim':
        format_linha('SISTEMA INTERATIVO PyHelp')
        sleep(1)
        search = str(input('Função ou biblioteca: '))
        if search != 'fim':
            format_linha(f'ACESSANDO MANUAL DE "{search}"', 33)
            sleep(2)
            print(f'\033[1;36m{ajuda(search)}\033[m')
    format_linha('FIM', 31)


pyhelp()
