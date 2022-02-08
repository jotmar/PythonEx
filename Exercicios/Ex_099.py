from time import sleep


def mostralinha():
    print('='+('-='*25))


def maior(*num):
    max = 0
    mostralinha()
    print('Analisando os valores passados...')
    for n in num:
        print(f'{n} ', end='', flush=True)
        if n > max:
            max = n
        sleep(0.5)
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {max}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
