largura = float(input('Qual é a largura da parede? '))
altura = float(input('Qual é a altura da parede? '))
area = largura * altura
print(f'Sua parede tem uma dimensão de {largura}x{altura}\n'
      f'E sua área equivale a {area:.2f}m²')
print(f'Portanto será necessário {area / 2:.2f} litros de tinta para \n'
      f'pintar a parede')
