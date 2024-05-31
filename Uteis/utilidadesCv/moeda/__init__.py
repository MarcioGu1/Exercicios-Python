def titulo(txt):
    tam = 50
    print('~'* tam)
    print(f'{txt}'.center(tam))
    print('~'* tam)

cor = ('\033[m'    ,  # 0 NADA
       '\033[1;33m',  # 1 AMARELO
       '\033[1;34m',  # 2 AZUL
       '\033[7;40m',  # 3 BRANCO
       '\033[1;31m',  # 4 VERMELHO
       '\033[1;32m',  # 5 verde
       )
def moeda (num=0,moeda='R$'):
    return (f'{moeda} \033[1;32m{num:>6.2f}\033[m'.replace('.',','))

def aumentar(valor=0, porc=0,form=False):
    aumento = float(valor) * (porc / 100 + 1)
    if form:
        return (moeda(aumento))
    else:
        return (f'{aumento:.2f}')

def diminuir(valor=0, porc=0,form=False):
    decrescimo = (float(valor) * (porc / 100 - 1))*-1
    if form:
        return (moeda(decrescimo))
    else:
        return (f'{decrescimo:.2f}')

def dobro (valor = 0,form=False):
    dob = float(valor)*2
    return (f'{dob:.2f}')if not form else moeda(dob)

def metade (valor = 0,form=False):
    met = float(valor) / 2
    return (f'\033[1;32{met:.2f}\033[m') if form is False else moeda(met)

def resumo (va = 0,aum = 0 ,dec = 0):
    titulo('Resumo Do Valor')
    print(f'{"Preço analisado:":<11}    {moeda(va):}')
    print(f'{"Dobro do preço:":<10}     {dobro(va, True)}')
    print(f'{"Metade do preço:":<11}    {metade(va, True)}')
    print(f'{aum}{"% de aumento":<11}:     {aumentar(va, aum, True)}')
    print(f'{dec}{"% de redução":<11}:     {diminuir(va, dec, True)}')
    print('~'*(len('Resumo do valor') + 16))