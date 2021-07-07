print('='*30)
print(f'{"Calculadora de IMC":^30}')
print('='*30)
peso = float(input('Qual é o seu peso? '))
alt = float(input('Qual é a sua altura? '))
imc = peso / alt**2

if imc < 18.5:
    print('Abaixo do Peso')
elif imc >= 18.5 and imc < 25:
    print('Peso Ideal')
elif imc >= 25 and imc < 30:
    print('Sobrepeso!')
elif imc >= 30 and imc < 40:
    print('Obesidade!')
elif imc >= 40:
    print('Obesidade mórbida')
