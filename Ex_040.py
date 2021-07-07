n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2

if media < 5:
    print('Você está reprovado!')
elif media <= 6.9:
    print('Você está de recuperação!')
elif media >= 7:
    print('Parabéns você está aprovado!')

