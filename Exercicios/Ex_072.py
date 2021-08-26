num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete','oito','nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
op = None
while op not in ('nao', 'não', 'n'): 
    n = int(input('Digite um número de 0 a 20: '))
    while n > 20 or n < 0:
        n = int(input('Tente Novamente. Digite um número de 0 a 20: '))
    print(f'Você digitou o número {num[n]}')
    while op not in ('s', 'sim', 'n', 'não', 'nao'):
        op = str(input('Deseja continuar?[S/N] ')).lower().strip()
