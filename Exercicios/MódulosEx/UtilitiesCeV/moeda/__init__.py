def aumentar(v, q, form=False):
    """
    :param v: valor do produto
    :param q: Taxa de aumento no preço
    :param form: Se será ou não formatado
    :return: O valor do produto com aumento de acordo com a taxa
    """
    if form:
        return moeda(v + (v / 100 * q))
    else:
        return v + (v / 100 * q)

def diminuir(v, q, form=False):
    """
    :param v: valor do produto
    :param q: Taxa de aumento no preço
    :param form: Se será ou não formatado
    :return: O valor do produto com redução de acordo com a taxa
    """
    if form:
        return moeda(v - (v / 100 * q))
    else:
        return v - (v / 100 * q)


def dobro(n, form=False):
    if form:
        return moeda(n*2)
    else:
        return n*2

def metade(n, form=False):
    if form:
        return moeda(n/2)
    else:
        return n/2


def moeda(n):
    string = f'R${n:.2f}'
    return string.replace('.', ',')


def resumo(v, aumento, reducao):
    print('='*40)
    print(f'{"RESUMO DO VALOR":^40}')
    print('='*40)
    print(f"{'Preço Analisado:':<20}", moeda(v))
    print(f"{'Dobro do preço:':<20}", dobro(v, True))
    print(f"{'Metade do preço:':<20}", metade(v, True))
    print(f"{f'{aumento}% de aumento:':<20}", aumentar(v, aumento, True))
    print(f"{f'{reducao}% de redução:':<20}", diminuir(v, reducao, True))
