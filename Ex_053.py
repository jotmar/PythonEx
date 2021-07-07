print('Detector de Palindromo')
frase = str(input('Digite a frase desejada: ')).strip().lower()
format = frase.replace(' ', '')
cont = 0
resul = 'Esta frase é um palíndromo!'
for a in format[::-1]:
    if a != format[cont]:
        resul = 'Essa frase não é um palíndromo!'
        break
    cont += 1
print(resul)
