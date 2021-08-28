parenteses = 0
exp = str(input('Digite a expressão: '))
if '(' not in exp and ')' not in exp:
    print('Sua expressão não tem parênteses.')
else:    
    for carac in exp:
        if parenteses < 0:
            print('Expressão inválida!')
            break
        else:
            if carac == '(':
                parenteses += 1
            elif carac == ')':
                parenteses -= 1
    if parenteses == 0:
        print('Sua expressão está correta.')
    if parenteses > 0:
        print('Sua expressão está errada.')
