km = float(input("Qual é a velocidade do carro em km/h? "))
if km > 80:
    print(f"""Você ultrapassou o limite de velocidade que
era 80km/h sua multa foi de R${(km - 80) * 7.00:.2f}""")
else:
    print("Tenha uma boa viagem!")
