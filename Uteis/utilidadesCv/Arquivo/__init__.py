from typing import List


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    a = open(nome, 'wt+')
    a.close


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print(f'Erro ao ler arquivo {nome}')
    else:
        print(a.read())
    finally:
        a.close()


def usuario(arquivo, nome='desconhecido', idade=0):
    try:
        a = open(arquivo, 'at')
    except:
        print('Erro na abertura do arquivo')
    else:
        try:
            a.write(f'{nome:<30} {idade:>3} anos\n')
        except:
            print('Houve um erro na hora de escrever os dados')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()
