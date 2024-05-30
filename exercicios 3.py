# Mexendo com bibliotecas

import random
lista=[ str(input('Escreva seu nome :'))for name in range(1,5)]
random.shuffle(lista)
print(lista)
#----------------------------------------------------------------
nome=str(input('digite seu nome :')).strip()
print(nome.upper())
print(nome.lower())
first = nome.split()
print(len(nome)-nome.count(' '))
print('seu 1º nome é {} e ele tem {} letras'.format(first[0],len(first[0])))
#----------------------------------------------------------------
city =str(input('qual cidade voce nasceu :')).strip()
identificador = str(city.lower())
print(identificador[:5]=='santo')
#----------------------------------------------------------------
fullname = str(input('qual seu nome completo :')).strip()
print('seu nome tem Silva:{}'.format('silva'in fullname.lower()))
#----------------------------------------------------------------
obj=str(input('digite algo :')).strip()
ident=obj.lower()
print('a letra A apareceu :{} vezes\nAletra apraceu pela primeira vez na posição: {} \nA letra A apareceu por ultimo na posição:{}'.format(ident.count('a'),ident.find('a')+1,ident.rfind('a')))
#----------------------------------------------------------------
name = str(input('Digite seu nome:'))
identi = name.split()
print('prazer em te conhecer {}\nSeu primeiro nome é:{}\nSeu ultimo nome é:{}'.format(name,identi[0],identi[-1]))
#----------------------------------------------------------------
velocidade = float(input('Qual sua velocidade:'))
multa = float((velocidade-80.0)*7.0)
if velocidade <= 80.0:
    print('Boa conduta siga em frente')
else:
    print('Paro paro paro ,você excedeu o limite de 80km,sua meulta é de :R${:.2f}'.format(multa))
#----------------------------------------------------------------
from time import sleep
num =float(input('digite um numero:'))
print('calculando ...')
sleep(2)
result = x%2
if result == 0:
    print('{} é um numero par'.format(num))
else:
    print('{} é um número impar'.format(num))
print('_'*50)
print('Obrigado pela preferencia espero ter ajudado')
#----------------------------------------------------------------
distancia=float(input('Qual a kilometragem total da viagem? :'))
if distancia > 200:
    print('o custo da viagem sera de R${:.2f}'.format(distancia*0.45))
else:
    print('O preço da viagem será de R${:.2f}'.format(distancia/2))
print('BOA VIAGEM')
