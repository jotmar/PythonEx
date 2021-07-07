produto = float(input('Qual é o preço do produto? R$'))
print(f'O produto teve um desconto de 5% e agora custa R${produto - (produto * 5 / 100):.2f}')
