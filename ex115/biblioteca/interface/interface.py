def leiaint(a):
    while True:
        try:
            n = int(input(a))
        except KeyboardInterrupt:
            print()
            print(f'\033[1;31m{"O usuário não digitou nenhum valor! Valor assumido será 0."}\033[0m')
            return 0
        except:
            print(f'\033[1;31m{"ERRO! Por favor, digite uma opção válida."}\033[0m')
        else:
            return n


def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(f'{txt.center(42)}')
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[1;33m{c}\033[0m - \033[1;34m{item}\033[0m')
        c += 1
    print(linha())
    opc = leiaint('Sua Opção: ')
    return opc
