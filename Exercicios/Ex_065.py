maior = media = menor = cont = 0
while True:
    num = int(input('Digite um número inteiro: '))
    while True:
        prosseguir = str(input('Deseja continuar?[S/N] ')).strip().lower()
        if prosseguir != 's' and prosseguir != 'n':
            print('Valor Inválido! Por favor tente novamente.')
        else:
            break
    if menor == 0 and maior == 0:
        menor = maior = num
    if menor > num:
        menor = num
    if maior < num:
        maior = num
    media += num
    cont += 1
    if prosseguir == 'n':
        break
print('='*30)
print(f"""A média dos {cont} números digitados foi {media / cont:.2f}
O maior número digitado foi {maior}
O menor número digitado foi {menor}""")
