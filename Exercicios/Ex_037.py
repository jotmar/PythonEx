n1 = int(input('Qual número desejar converter? '))
print("""
[1] Octal
[2] Binário
[3] Hexadecimal
""")
#Conversões --- Transformei em str para formatar melhor
octal = str(oct(n1))
binario = str(bin(n1))
hexadecimal = str(hex(n1))


op = int(input('Deseja converter utilizando quais das opções? '))
if op == 1:
    print(f'O número {n1} convertido para Octal é {octal[2:]}')
elif op == 2:
    print(f'O número {n1} convertido para Binário é {binario[2:]}')
elif op == 3:
    print(f'O número {n1} convertido para Hexadecimal é {hexadecimal[2:]}')
else:
    print('Opção Inválida, tente novamente')
