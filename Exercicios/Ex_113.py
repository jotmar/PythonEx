#Minha forma
def LeiaInt(txt):
    try:
        n = input(txt).strip()
        while n.isnumeric() == False:
            print('\033[31mERRO! Digite um valor inteiro válido.\033[m')
            n = input(txt).strip()
    except KeyboardInterrupt:
        print('\n\033[31mO usuário preferiu não digitar.\033[m')
        return 0
    else:
        return int(n)

#Forma do guanabara

def LeiaFloat(text):
    while True:
        try:
            n = float(input(text).strip())
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um valor real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não digitar.\033[m')
            return 0
        else:
            return n

a = LeiaInt('Digite um número inteiro: ')
b = LeiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {a} e o real foi {b}')
