while True:
    num = int(input('Quer ver a tabuada de qual número? '))
    #Digitar números negativos para encerrar
    if num > -1:
        for c in range(1, 11):
            print(f'{num} X {c} = {num * c}')
    else:
        break
    print('-='*30)
