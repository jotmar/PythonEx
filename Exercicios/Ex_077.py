palavras = ('estudar', 'bicicleta', 'ovo', 'bola', 'parede', 'python', 'moto', 'curso', 'suco', 'corrida', 'torradeira', 'programador')
vogais = ('a', 'e', 'i', 'o', 'u')
for palavra in palavras:
    print(f'Na palavra {palavra.upper()} existem as seguintes vogais: ', end=' ')
    for letra in palavra:
        if letra in vogais:
            print(letra, end=' ')
    print()
