def leiaInt(msg):


    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):


    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número Real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n

n1 = leiaInt('Digite um Inteiro:')
n2 = leiaFloat('Digite um Real:')
print(f'O valor digitado foi {n1} e o real foi {n2}')


#Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a
#possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função
#leiaFloat() com a mesma funcionalidade.