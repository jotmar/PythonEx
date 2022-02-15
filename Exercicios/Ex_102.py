def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número
    :param n: O número a ser calculado
    :param show: (opcional) Mostra a conta
    :return: O valor do fatorial de um número.
    """
    f = 1
    for v in range(n, 0, -1):
        f *= v
        if show and v != 1:
            print(f'{v} x ', end='')
        elif show and v == 1:
            print(f'{v} ', end='')
    if show:
        print(f'= {f}', end='')
        return ''
    else:
        return f

print(fatorial(12, True))
