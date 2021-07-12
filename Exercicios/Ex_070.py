total = mais1k = cheaper = cheaper_price = 0
while True:
    print('-='*30)
    produto = str(input('Produto: ')).strip()
    price = float(input('Preço: R$'))
    if price > 1000:
        mais1k += 1
    if cheaper == 0:
        cheaper = produto
        cheaper_price = price
    if cheaper_price > price:
        cheaper_price = price
        cheaper = produto
    total += price
    print('-='*30)
    while True:
        option = str(input('Deseja continuar?[S/N] ')).strip().upper()
        if option not in ['S', 'N', 'SIM', 'NAO', 'NÃO']:
            print('Valor inválido! Tente novamente.')
        else:
            break
    if option not in ['S', 'SIM']:
        break
print(f'Total gasto: R${total:.2f}')
print(f'Quantidade de produtos que custam mais de R$1000: {mais1k}')
print(f'O produto mais barato foi {cheaper}, que custou R${cheaper_price:.2f} ')
