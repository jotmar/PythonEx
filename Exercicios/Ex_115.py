from time import sleep
from MódulosEx.Cadastro115.Format import CreateTittle, LeiaInt, color, menu
from MódulosEx.Cadastro115.data import Arquivo_Existe, Cadastrados, Cadastrar
arquivo = 'Exercicios/MódulosEx/Cadastro115/cursoemvideo.txt'

Arquivo_Existe(arquivo)
try:
    while True:
        CreateTittle('MENU PRINCIPAL', '=', '1;32')
        menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
        print('\033[1;32m=\033[m'*50)
        option = LeiaInt(color('Sua opção: ', 1), 'ERRO! Digite uma opção válida.', 1, 3)
        if option == 1:
            Cadastrados(arquivo)
        elif option == 2:
            Cadastrar(arquivo)
        elif option == 3:
            break
    CreateTittle('Finalizando Programa', '=', '1;31')
    sleep(2)
except KeyboardInterrupt:
    print(color('\nO usuário decidiu encerrar o programa.', '1;31'))
except:
    print(color('Tivemos um problema durante a execução do problema. Tente novamente.', '1;31'))
