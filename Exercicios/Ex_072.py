num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete','oito','nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

n = int(input('Digite um número de 0 a 20: '))
while n > 20 or n < 0:
    n = int(input('Tente Novamente. Digite um número de 0 a 20: '))
print(f'Você digitou o número {num[n]}')
