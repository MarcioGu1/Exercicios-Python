'''numero = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito')
while True:
    num = int(input('digite um numero :'))
    if 0<= num <= 8 :
        break
print(f'voce digitou {numero[num]}')'''
#-------------------------------------------------------------------------------------------
'''times = ('BOTAFOGO','BRAGANTINO','GREMIO','PALMEIRAS','FLAMENGO','FLUMINENSE','ATLETICO-MG','ATLETICO-PR','FORTALEZA','SAO PAULO','CUIABA','CRUZEIRO','CORINTHIANS')
print('-='*50)
for t in times:
    print(t,end = ' ')
print('-='*50)
print(f'os cinco primeiro sao {times[0:5]}')
print('-='*50)
print(f'na degola estao {times [-4:]}')
print (f'ordem alfabética{sorted(times)}')
print ('o timao esta na {}ªposição'.format(times.index('CORINTHIANS')+1))'''
#--------------------------------------------------------------------------------------------
'''from random import randint
lista=(randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print('os valores sorteados foram: ',end='')
for num in lista:
    print(f'{num}  ', end='')
print(f'\no maior numero é {max(lista)}')
print(f'o menor numero é {min(lista)}')'''
#----------------------------------------------------------------------------------------------
'''cont=0
lista= (int(input('digite um numero :')),
        int(input('digite um numero :')),
        int(input('digite um numero :')),
        int(input('digite o ultimo numero :')))
print(f'você digitou os valores {lista}')
for elemento in lista:
    if elemento %2 == 0:
        cont += 1
print(f'O numero 9 apareceu {lista.count(9)} vezes')
if 3 in lista:
    print(f'O numero 3 apareceu na {lista.index(3)+1}ªposição')
else:
    print('o numero 3 nao aparece em nenhuma posição')
print(f'voce digitou {cont} numeros pares')'''
#------------------------------------------------------------------------------------------------
'''print('='*50)
print('{:^50}'.format('listagem de preço'))
print('='*50)

lista=('lápis',1.75,
       'Borracha',2,
       'caderno',15.90)
for posiçao in range ( 0,len(lista)):
    if posiçao % 2 == 0:
        print(f'{lista[posiçao]:.<40}',end='')
    else:
        print(f'R${lista[posiçao]:>8.2f}')
print('='*50)'''
#---------------------------------------------------------------------------------------------------
'''lista=('aprender','educar','simplicidade','professora','alemao')
for item in lista:
     print(f'\nNa palavra \033[1;32m{item.upper()}\033[m temos ',end='')
     for letra in item:
         if letra in 'aeiou':
             print (letra, end=' ')'''
#---------------------------------------------------------------------------------------------------
'''from time import sleep
lista = []
while True:
    numero = float(input('digite um numero: '))
    if numero not in lista:
        lista.append(numero)
        print('\033[1;32mvalor inserido\033[m')
    else:
        print('opa , numero já existente na lista')
    resposta = str(input('deseja continuar? ')).lower().strip()[0]
    while resposta not in 'sn':
        print('nao entendi, responda com sim ou nao')
        sleep(1)
        resposta =str(input('voce deseja continuar? '))
    if resposta == 'n':
            break
lista.sort()
print(f'voce digitou a seguinte lista {lista}')'''
#--------------------------------------------------------------------------------------------------------
'''lista=[]
for c in range (0,5):
    numero = int(input('digite um valor:'))
    if c == 0 or numero > lista[-1] :
        lista.append(numero)
        print('adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if  numero <= lista[pos]:
                lista.insert(pos,numero)
                print(f'valor {numero} adicionado na posição {pos}')
                break
            pos+= 1
print (lista)'''
#-------------------------------------------------------------------------------------------------------------
'''lista=[]
while True:
     lista.append(int(input('digite um valor: ')))
     resposta = str(input('deseja continuar?'))
     while resposta not in 'sn':
        print( 'nao entendi')
        resposta = str(input('deseja continuar? '))
     if resposta == 'n':
        break
lista.sort(reverse = True)
print('='*30)
print(f'a lista tem {len(lista)} elementos')
print(lista)
if 5 in lista :
    print('O numero 5 faz parte da lista')
else:
    print('nao tem 5')'''
#--------------------------------------------------------------------------------------------------------------------
'''lista=[]
impar=[]
par = []
while True:
    numero= int(input('digite um valor: '))
    lista.append(numero)
    resposta = input('deseja continuar: ').lower().strip()[0]
    while resposta not in 'sn':
        resposta = input('deseja continuar? ')
    if resposta == 'n':
        break
for i,valor in enumerate(lista) :
        
    if valor % 2 == 0 end valor != 0:
        par.append(valor)
print(f'voce criou a seguinte lista {lista}')
print(f'a lista de numeros pares é {par}')
print(f'a lista de numeros impares é {impar}')'''
#--------------------------------------------------------------------------------------------------------------------
'''expressao = str(input('crie sua expressão: '))
conta=[]
for simbolo in expressao:
    if simbolo  == '(':
        conta.append('(')
    elif simbolo == ')':
        if len(conta) > 0:
            conta.pop()
        else:
            conta.append(')')
            break
if len(conta) == 0:
    print('expressão valida')
else:
    print('expressão invalida')'''
#--------------------------------------------------------------------------------------------------------------------
'''pessoas= []
dados= []
maior = menor = 0
while True:
    dados.append(str(input('digite seu nome: ')))
    dados.append(float(input('digite seu peso: ')))
    if len(pessoas) == 0 :
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resposta =str(input('deseja continuar: ')).upper().strip()[0]
    while resposta not in 'SN':
        resposta = str(input('deseja continuar: ')).upper().strip()[0]
    if resposta == 'N':
        break
print(f'ao total voce cadastrou {len(pessoas)} pessoas ')
print(f'o maior peso foi de {maior}Kg:Peso de ',end= '')
for p in pessoas:
    if p[1]== maior:
        print(f'{p[0]}',end= '')
print(f'\no menor peso foi de {menor}Kg : de ',end='')
for p in pessoas:
    if p[1]== menor:
        print(f'{p[0]}',end= '')'''
#--------------------------------------------------------------------------------------------------------------------
'''numeros=[[],[]]
for n in range(0,5):
    x = int(input(f'digite  o {n+1}º elemnto : '))
    if x % 2 == 0:
        numeros[0].append(x)
    else:
        numeros[1].append(x)
numeros[0].sort()
numeros[1].sort()
print(f'a lista de numeros pares é {numeros[0]}')
print(f'a lista de numeros impares é {numeros[1]}')'''
#--------------------------------------------------------------------------------------------------------------------
'''maior = soma = pares = 0
matriz = [ [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ]]
for linha in range (0,3):
    for coluna in range(0,3):
        matriz[linha][coluna]= int(input(f'digite um valor para a posição {linha+1}:{coluna+1} :'))
print('='*50)
for linha in range (0,3):
    for coluna in range (0,3):
        print(f'[{matriz[linha][coluna]:^6}]',end='')
        if matriz [linha][coluna] % 2 == 0:
            pares += matriz [linha][coluna]
        if coluna == 2:
            soma+= matriz[linha][2]
        if coluna == 0 or matriz[1][coluna] > maior:
            maior = matriz[1][coluna]
    print()
print('='*50)
print(f'A soma dos valores pares é {pares}')
print(f'\nA soma dos valores da terceira coluna é {soma}')
print(f'\nO maior valor da segunda linha é {maior}')'''
#--------------------------------------------------------------------------------------------------------------------
#  PALPITE JOGOS DE AZAR, CRIA DPS UM PROGRAMA IGUAL A ESSES SOQ COM OS NUMEROS QUE MAIS CAEM
'''from random import randint
from time import sleep
palpite = list()
jogos = list()
print('-'*50)
print(f'{"PALPITE DA MEGA SENA":^50}')
print('-'*50)
vezes = int(input('Quantos jogos voce quer que eu faça? '))
totalDeJogos=1
print(f'{"SORTEANDO JOGOS":=^50}')
while totalDeJogos <= vezes:
    cont = 0
    while True:
        numeros = randint(1, 60)
        if numeros not in palpite:
            palpite.append(numeros)
            cont += 1
        if cont >= 6:
            break
    palpite.sort()
    jogos.append(palpite[:])
    palpite.clear()
    totalDeJogos +=1

for i,l in enumerate(jogos):
    print(f'jogo {i+1}: {l}')
    sleep(1)
print(f'{"< BOA SORTE >":=^50}')'''
#--------------------------------------------------------------------------------------------------------------------
'''lista = list()
while True:
    nome =str(input('qual o nome do aluno: '))
    av1 = float(input('Qual sua nota na AV1: '))
    av2 = float(input('Qual sua nota na AV2: '))
    media = (av1+av2)/2
    lista.append([nome,[av1,av2],media])
    resposta = str(input('deseja continuar? ')).upper().strip()[0]
    if resposta == 'N':
        break
    while resposta not in 'SN':
        resposta = str(input('deseja continuar? ')).upper().strip()[0]
print('='*50)
print(f'{"BOLETIM ESCOLA":^28}')
print('-'*28)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
for i,a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.2f} ')
while True:
    resp = int(input('deseja ver a nota de que aluno ?[999 para]: '))
    if resp == 999:
        break
    if resp <= len(lista):
         print(f'O aluno {lista[resp][0]} tirou as seguintes notas : {lista[resp][1]} e ele esta ',end='')
    if lista[resp][2]>= 7.0:
        print('\033[1;32maprovado\033[m',)
    else:
        print('\033[1;31mreprovado\033[m')
print(f'{"<VOLTE SEMPRE>":-^50}')'''
#--------------------------------------------------------------------------------------------------------------------
'''dados = dict()
nome = str(input('nome : '))
media =float(input(f'Qual foi a média de {nome} : '))
dados['nome'] = nome
dados['media']=media
if media >= 7 :
    dados['situação'] = 'Aprovado'
else:
    dados['situação'] = 'Reprovado'
print('-='*30)
for k,v in dados.items():
    print(f' - {k} é igual {v}')'''
#--------------------------------------------------------------------------------------------------------------------
'''from random import randint
from operator import itemgetter
from time import sleep
jogadas = {}
ranking = []
cont= 0
while True:
    numero = randint (1,6)
    if numero not in jogadas:
        jogadas[f'payer{cont+1}']= numero
        cont+= 1
    if cont == 4 :
        break
for p , j in jogadas.items():
    sleep(1)
    print(f'  {p} tirou {j} no dado.')
print('§'*50)
print(f'{" == Ranking dos jogadores == "}')
ranking =sorted(jogadas.items(),key = itemgetter(1),reverse=True)
for i,v in enumerate(ranking):
    sleep(1)
    print(f'  {i+1}º colocado: {v[0]} com {v[1]}')'''
#--------------------------------------------------------------------------------------------------------------------
'''def sorteie ():
    from random import randint
    lista=[]
    r = randint(1,10)
    print(f'Sorteando {r} valores : ',end='')
    for c in range (0,r):
        c = randint(0,10)
        lista.append(c)
    for valor in lista:
        print(f'\033[1;32m{valor}\033[m ',end='')
    print('Pronto !!!!')
    return lista
def somapar(lista):
    soma = 0
    for v in lista :
        if v % 2 == 0:
            soma+= v
    print(f'Somando os valores pares de {lista}, temos {soma}', end='')
somapar(sorteie())'''
#--------------------------------------------------------------------------------------------------------------------
'''def voto (ano):
    from datetime import date
    idade = date.today().year - ano
    print('-'*30)
    if idade < 16 :
        return (f'Voce tem {idade} anos\nseu voto é \033[1;32mNegado\033[m')
    elif 15 < idade < 18 or idade > 65:
        return (f'Voce tem {idade} anos\nseu voto é \033[1;34mOpicional\033[m')
    else:
        return (f'Voce tem {idade} anos\nseu voto é \033[1;31mObrigatório\033[m')
ano = int(input('Que ano voce nasceu: '))
print(voto(ano))'''
#--------------------------------------------------------------------------------------------------------------------
'''def fatorial(num=1,show=False):
    f = 1
    print(f'O fatorial de \033[1;34m{num}\033[m é : ')
    for c in range(num, 0, -1):
        if show:
            print(c,end='')
            if c > 1:
                print (f' x ',end='')
            else:
                print(' = ',end='')
        f *= c
    return (f'\033[1;31m{f}\033[m')
print(fatorial(6,show=True))'''
#--------------------------------------------------------------------------------------------------------------------
'''def ficha(jogador ='<desconhecido>',gol = 0):
    print('-'*30)
    print(f'O {jogador} fez {gol} gols')

atleta= str(input('nome do atleta: '))
g = str(input('quantos gols ele fez:'))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if atleta.strip() == '':
    ficha(gol=g)
else:
    ficha(atleta,g)'''
#--------------------------------------------------------------------------------------------------------------------
'''def leiaInt(msg):
    ok=False
    valor = 0
    while True:
        x = str(input(msg))
        if x.isnumeric():
            valor = int(x)
            ok = True
            break
        else:
            print ('\033[1;31mError! Digite um numero inteiro\033[m')
    return valor
x=leiaInt('Digite um numero:')
print(f'Voce acabou de digitar o numero {x}')'''
#--------------------------------------------------------------------------------------------------------------------
'''def notas (*num,sit=False):
    r = dict()
    r['total'] = len(r)
    r['maior'] = max(r)
    r['menor'] = min(r)
    r['média'] = sum(r)/len(r)
    if sit:
        if r['média'] < 6:
            r['situação'] = '\033[1;31mRuim\033[m'
        elif r['média'] < 7:
            r['situação'] = '\033[1;33mRecuperação\033[m'
        else:
            r['situação'] = '\033[1;32mBoa\033[m'
    for k,v in r.items():
        print(f'{k} = {v:}')
resp = notas(5.5,9.5,10,6.5,sit=True)
print(resp)'''
#--------------------------------------------------------------------------------------------------------------------
'''from time import sleep
cor =('\033[m',    # 0 NADA
        '\033[;;43m',# 1 AMARELO
        '\033[;;44m',# 2 AZUL
        '\033[7;40m',# 3 BRANCO
        '\033[;;41m',# 4 VERMELHO
        '\033[;;42m',# 5 verde
     )
def titulo (msg ,c=0):
    tam = len(msg)+4
    print(cor[c], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(cor[0],end='')
    sleep(1)
def ajuda():
    titulo('Acessando o manual do comando '
                            f'\'{nome}\'',2)
    sleep(0.5)
    print(cor[3],end='')
    help(nome)
    print(cor[0],end='')
while True:
    titulo('Sistema de ajuda PyHELP', 5)
    nome = str(input('Função ou Biblioteca >'))
    if nome.upper() == 'FIM':
        break
    else:
        sleep(1)
        ajuda()
        sleep(1)
titulo('ATÉ LOGO !',4)'''
#--------------------------------------------------------------------------------------------------------------------
'''from Uteis.utilidadesCv import moeda,dados
p =dados.leiaDinheiro('Digite o preço : R$ ')
print(f'a metade de R$ {moeda.moeda(p)} é {moeda.metade(p,True)}')
print(f'a dobro  de R$ {moeda.moeda(p)} é {moeda.dobro(p,True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p,10,True)}')
print(f'Diminuindo 13%, temos {moeda.diminuir(p,13,True)}')
moeda.resumo(p,80,35)'''
#--------------------------------------------------------------------------------------------------------------------
'''from Uteis.utilidadesCv import dados
numero1 = dados.leiaFloat(input('digite um numero real: '))
print(f'O valor digitado foi {numero1}')
numero2 =dados.leiaInt(input('Digite um numero inteiro : '))
print(f'O valor digitado foi {numero2}')'''
#--------------------------------------------------------------------------------------------------------------------
'''from Uteis.utilidadesCv import dados,moeda,Arquivo
from time import sleep
arq = 'listaUsuarios.txt'
if not Arquivo.arquivoExiste(arq):
    Arquivo.criarArquivo(arq)
moeda.titulo('MENU PRINCIPAL')
dados.opcoes('Lista de usuários','Inserir novo usuário','Sair do Programa')
opcao = dados.leiaInt(input('\033[1;32mQual opção : \033[m'))
while opcao != 3:
    if opcao not in [1,2,3]:
        print(f'\033[1;31mERROR,número invalido\033[m')
        sleep(0,5)
        opcao = dados.leiaInt(input('\033[1;32mQual opção : \033[m'))
    elif opcao == 1 :
        moeda.titulo('PESSOAS CADASTRADAS')
        sleep(1)
        Arquivo.lerArquivo(arq)
        print('-' * 50)
        moeda.titulo('MENU PRINCIPAL')
        dados.opcoes('Lista de usuários', 'Inserir novo usuário', 'Sair do Programa')
        opcao = dados.leiaInt(input('\033[1;32mQual opção : \033[m'))
    elif opcao == 2 :
        moeda.titulo('Novo cadastro')
        sleep(1)
        nome=str(input('Qual nome do usuário novo :'))
        idade = dados.leiaInt(input('Qual idade do usuário novo :'))
        Arquivo.usuario(arq,nome,idade)
        moeda.titulo('MENU PRINCIPAL')
        dados.opcoes('Lista de usuários', 'Inserir novo usuário', 'Sair do Programa')
        opcao = dados.leiaInt(input('\033[1;32mQual opção : \033[m'))
moeda.titulo('OPÇÃO 3')
sleep(1)
moeda.titulo("SAINDO DO SISTEMA ...... ADEUS")'''
#--------------------------------------------------------------------------------------------------------------------
'''#CRINADO ARQUIVO EM HTML
with open('C:\codigos\pagina.html','w') as pagina :
    pagina.write('<body> <h1> Esta é um teste para pagina web</h1>')
    pagina.write('<br><h2> Abaixo segue nomes importantes:  web</h2>')
    pagina.write('<h3>')
    nome = ''
    while nome != 'SAIR':
        nome = str(input('Digite seu nome ou sair: ')).upper()
        if nome!='SAIR':
            pagina.write(f'{nome} <br>')
    pagina.write('</h3></body>')'''
#--------------------------------------------------------------------------------------------------------------------
'''with open('C:\codigos\ teste.txt', 'r') as arquivo :
    conteudo = arquivo.readlines ()
print(f'Tipo de dado da variavel {type(conteudo)}')
print(f'\nConteúdo do arquivo :\n{conteudo}')'''
#------------------------------------------------------------------------------------------------------------------
