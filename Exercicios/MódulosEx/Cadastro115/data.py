from MódulosEx.Cadastro115.Format import CreateTittle, LeiaInt, color


def Cadastrados(arquivo):
    CreateTittle('PESSOAS CADASTRADAS', '=', color='1;34')
    try:
        arq = open(arquivo, 'rt')
        print(color(arq.read(), 1))
        arq.close()
    except:
        print(color('Não foi possível listar os usuários cadastrados.', '1;31'))


def Cadastrar(arquivo):
    CreateTittle('NOVO CADASTRO', '=', '1;35')
    try:
        nome = str(input(color('Nome: ', 1))).strip()
        idade = LeiaInt('Idade: ', 'ERRO! Digite uma idade válida.', -1, 200)
        arq = open(arquivo, 'rt')
        if arq.read() == '':
            arq = open(arquivo, 'a')
            arq.write(f'{nome:<35}{idade:>3} anos')
        else:
            arq = open(arquivo, 'a')
            arq.write(f'\n{nome:<35}{idade:>3} anos')
    except KeyboardInterrupt:
        print(color('\nO usuário preferiu não digitar.', '1;31'))
    except:
        print(color('Não foi possível cadastrar um novo usuário.', '1;31'))


def Arquivo_Existe(arquivo):
    try:
        arq = open(arquivo, 'rt')
        arq.close()
    except FileNotFoundError:
        arq = open(arquivo, 'wt+')
    else:
        return True
