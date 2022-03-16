from ex115.biblioteca.interface.interface import *
from time import sleep
from ex115.biblioteca.arquivo.arquivo import *

arq = 'curso.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #Listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        #cadastrar nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print('Saindo do sistema...', end=' ')
        sleep(2)
        print('Até logo!')
        break
    else:
        print(f'\033[1;31m{"ERRO! Digite uma opção válida!"}\033[0m')
