def notas(*n, sit=False):
    """
    --> Função para analisar notas de vários alunos
    :param n: Recebe uma ou mais notas
    :param sit: Indica se deve ou não adicionar a situação
    :return: O dicionário com todas as informações sobre as notas
    """
    boletim = dict()
    boletim['total'] = len(n)
    boletim['maior'] = max(n)
    boletim['menor'] = min(n)
    boletim['media'] = sum(n) / len(n)
    if sit:
        if boletim['media'] >= 7:
            boletim['situação'] = 'BOA'
        elif boletim['media'] >= 5:
            boletim['situação'] = 'RAZOÁVEL'
        elif boletim['media'] < 5:
            boletim['situação'] = 'RUIM'
    return boletim


resp = notas(4, 3, 7, 6, sit=False)
print(resp)
#help(notas)
