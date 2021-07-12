cont = soma = 0
while True:
    num = int(input('Digite um número inteiro [999 para parar]: '))
    if num != 999:
        cont += 1
        soma += num
    else:
        break
print(f'A soma dos {cont} números resultam em {soma}')
