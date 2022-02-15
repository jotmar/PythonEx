from MódulosEx.UtilitiesCeV import moeda 

valor = float(input('Digite o preço: R$'))
print(f'A metade de {valor:.2f} é {moeda.metade(valor):.2f}')
print(f'O dobro de {valor:.2f} é {moeda.dobro(valor):.2f}')
print(f'Aumentado 10%, temos {moeda.aumentar(valor, 10):.2f}')
print(f'Diminuindo 13%, temos {moeda.diminuir(valor, 13):.2f}')
