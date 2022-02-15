def LeiaInt(txt):
    v = input(txt).strip().replace(',', '.')
    while v.replace('.', '').isnumeric() == False:
        print(f'\033[31mERRO: "{v}" é um preço inválido!\033[m')
        v = input(txt).strip().replace(',', '.')
    return float(v)
