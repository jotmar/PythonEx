nome = str(input('Digite seu nome completo: ')).strip()
sep = nome.split()
print(f'Seu primeiro nome é {sep[0]}')
print(f'Seu último nome é {sep[len(sep) - 1]}')
