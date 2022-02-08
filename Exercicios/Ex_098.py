from time import sleep

def mostralinha():
    print('='*50)


def contador(inicio, fim, passo):
    mostralinha()
    if passo == 0:
        passo = 1
    elif passo < 0:
        passo *= -1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio > fim:
        passo *= -1
        fim -= 2
    for n in range(inicio, fim+1, passo):
        print(f'{n} ', end='', flush=True)
        sleep(0.5)
    print('FIM!')


contador(0, 10, 1)
contador(10, 0, -2)
mostralinha()
print('Agora é sua vez de definir a contagem!')
ini = int(input('Inicio: '))
end = int(input('Fim: '))
jump = int(input('Passo: '))
contador(ini, end, jump)
mostralinha()
