def LeiaInt(txt):
    num = input(txt).strip()
    while num.isnumeric() == False:
        print('\033[1;31mERRO! Digite um valor inteiro.\033[m')
        num = input(txt)
    num = int(num)
    return num


n = LeiaInt('Digite um número inteiro: ')
print(f'O número inteiro digitado foi {n}')
