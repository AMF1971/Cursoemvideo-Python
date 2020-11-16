from time import sleep
from ex_115.lib.interface import *
from ex_115.lib.arquivo import *

cabeçalho('SISTEMA ARQUIVO v1.0')

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa',  'Sair do Sistema'])
    if resposta == 1:
        # Opção de Listar o conteúdo de um arquivo!
        lerArquivo(arq)

    elif resposta == 2:
        #Opção de cadastrar uma nova pessoa.
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome'))
        idade = leiaInt('Idade')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção de sair do siatema.
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)





