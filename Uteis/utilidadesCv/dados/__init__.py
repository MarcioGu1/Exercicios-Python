def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[1;31mError:\"{entrada}\" número invalido!\033[m')
        else:
            valido = True
            return float(entrada)


def leiaInt(msg):
    while True:
        try:
            msg = int(msg)
        except (ValueError, TypeError):
            print(f'\033[1;31mErro: "{msg}" não é um número inteiro.\033[m')
            msg = input('Insira aqui um número inteiro: ')
            continue
        else:
            return msg


def leiaFloat(msg):
    while True:
        try:
            valor = msg.replace(',', '.')
            real = float(valor)
        except (ValueError, TypeError):
            print(f'\033[1;31mError!"{msg}" not is real number \033[m')
            msg = input('Insira aqui um número real: ')
            continue
        else:
            return f'{real}'.replace('.', ',')

def opcoes(* nome):
    lista = [nome]
    cont=0
    while cont <= len(lista)+1:
        print(f'\033[1;33m{cont + 1}\033[m - \033[1;34m{lista[0][cont]}\033[m')
        cont += 1
    print('-'*50)
