produto = float(input('Qual o valor do produto a ser comprado? R$'))
print("""
=============================
[1]À vista no dinheiro
[2]Cartão
=============================
""")
op = int(input('Escolha a forma de pagamento: '))
if op == 2:
    parcelado = int(input('Deseja pagar em quantas vezes? '))
    if parcelado == 1:
        print(f'O valor total com 5% de desconto ficará R${produto - (produto * 5 / 100):.2f}')
    elif parcelado == 2:
        print(f'O valor não será alterado. Portanto será R${produto:.2f}')
    elif parcelado > 2:
        print(f'O valor total com 20% de juros ficará R${produto + (produto * 20 / 100):.2f}')
elif op == 1:
    print(f'O valor total com 10% de desconto ficará R${produto - (produto * 10 / 100):.2f}')
else:
    print('Opção de pagamento inválida!')
