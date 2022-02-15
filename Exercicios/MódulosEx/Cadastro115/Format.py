def CreateTittle(text, char='=', color=''):
    print(f'\033[{color}m{char * 50}')
    print(text.center(50))
    print(f'{char * 50}\033[m')


def color(text, cor=''):
    c = f'\033[{cor}m{text}\033[m'
    return c

def LeiaInt(text, error='ERRO! Digite um número inteiro válido', min=0, max=0):
    n = input(text).strip()
    while n.isnumeric() == False or int(n) < min or int(n) > max:
        print(color(error, '1;31'))
        n = input(text).strip()
    n = int(n)
    return n

def menu(list):
    for c, i in enumerate(list):
        print(f"{color(f'{c+1}', 33)} - {color(i, '1;36')}")
