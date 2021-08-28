numbers = list()
for n in range(0, 5):
    numbers.append(int(input(f'Digite o valor da posição {n}: ')))
print(f'O maior valor digitado foi {max(numbers)} nas posições: ', end='')
for pos, n in enumerate(numbers):
    if n == max(numbers):
        print(pos, end='... ')
print()
print(f'O menor valor digitado foi {min(numbers)} nas posições: ', end='')
for pos, n in enumerate(numbers):
    if n == min(numbers):
        print(pos, end='... ')
print()
