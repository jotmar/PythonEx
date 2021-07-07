from math import cos, tan, sin, radians
ang = float(input('Qual é o ângulo desejado? '))
angtrue = radians(ang)
print(f'O ângulo de {ang:.2f} tem o SENO de {sin(angtrue):.2f} ')
print(f'O ângulo de {ang:.2f} tem o COSSENO de {cos(angtrue):.2f} ')
print(f'O ângulo de {ang:.2f} tem o TANGENTE de {tan(angtrue):.2f} ')
