numbers = list()
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0 or num > max(numbers):
        numbers.append(num)
        print('Adicionado no final da lista.')
    else:
        for pos, n in enumerate(numbers):
            if num <= n:
                numbers.insert(pos, num)
                print(f'Adicionado na posição {pos}')
                break
print(numbers)
