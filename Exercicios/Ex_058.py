from random import randint
num = randint(0, 10)
tentativas = 0

print("""Eu pensei em um número entre 0 e 10, será que você
consegue acertar qual foi?""")
while True:
    palpite = int(input('Qual é o seu palpite? '))
    tentativas += 1
    if palpite == num:
        print(f"""Parabéns você acertou!
Foram necessárias {tentativas} tentativas. """)
        break
    else:
        print('Você errou! Tente novamente.')
