#Condição de Parada é o número 999
cont = 0
soma = 0
while True:
    num = int(input('Digite um número[999 para parar]: '))
    if num != 999:
        cont += 1
        soma += num
    else:
        break
print(f'Você somou {cont} números, que somadados resultaram em {soma}')
