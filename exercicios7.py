from math import factorial
num=int (input('digite o valor:'))
c = num
print('O fatorial de {}! = '.format(num),end = '')
while c >0:
    print('{}'.format(c),end='')
    print(' x 'if c > 1 else ' = {} '.format(factorial(num)),end= '')
    c-= 1
#----------------------------------------------------------------
print('construtor de PA')
a1 = float(input('digite o valor do primeiro termo:'))
r = float(input('qual a razão: '))
periodo = int(input('quantos termos: '))
termo = a1
cont = 0
total = 0
mais = periodo
print('=-'*20)
while mais != 0:
    total += mais
    while cont < total:
        print('{} / '.format(termo), end='')
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais voce quer mostrar? '))
print('\nEssa PA tem {} termos'.format(cont))
#----------------------------------------------------------------
print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
#entrada de dados
termos= int(input('Quantos termos voce quer mostrar:'))
f1 =0
f2 = 1
cont = 3
print('~~~~~~'*termos)
print("{} => {}".format(f1,f2),end='')
while cont <= termos:
    f3= f1+f2
    print(' => {}'.format(f3),end='')
    f1 = f2
    f2 = f3
    cont += 1
print (' .FINAL')
print('~~~~~~~'*termos)

soma = cont = 0
num = float(input('digite um numero:'))
while num != 999:
    print('digite 999 para finalizar')
    cont += 1
    soma += num
    num = float(input('digite um numero:'))
print('voce digitou {} valores e a soma deles é {}'.format(cont,soma))

maior=0
menor= 0
cont = soma = media = 0
pergunta='S'
print('~~'*40)
while pergunta !='N':
    num=float(input('digite um valor:'))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor :
            menor = num
    pergunta =str(input('deseja continuar? [S/N]')).upper().strip()[0]
    print('~~'*40)
media =soma/cont
print('A média entre os {} valores informados é de {} '.format(cont,media))
print('O maior valor é {} enquanto o menor é {}'.format(maior,menor))
print('~~'*40)
#----------------------------------------------------------------
print('~'*50)
print('                    BOMBODEGA')
print('~'*50)
totalCompra = maisDeMil = menor = cont =0
nomeDoMaisBarato=' '
while True:
    produto = str(input('Nome do Produto:')).lower()
    valor = float( input('valor do produto R$ '))
    totalCompra += valor
    cont +=1
    continuar =' '
    if continuar == 'N':
        break
    if cont == 1 or valor < menor:
        menor = valor
        nomeDoMaisBarato = produto
    if valor > 1000 :
        maisDeMil+=1
    while continuar not in 'SN':
        continuar = str(input('deseja continuar:')).upper().strip()[0]
print('{:~^50}'.format('FIM DA COMPRA'))
print(f'O total da compra foi de R$ {totalCompra:.2f}\nTemos {maisDeMil} produtos custando mais de R$ 1000,00\nO produto mais barato foi {nomeDoMaisBarato} que custa R$ {menor:.2f}')
#----------------------------------------------------------------
print('='*50)
print('{:^50}'.format('banco btg'))
print('='*50)
notaCinquenta = notaVinte = notaDez = notaCinco = notaUm = 0
saque = int(input('Qual valor voce deseja sacar : R$ '))
if saque >= 50:
    notaCinquenta = saque // 50
if saque >= 20:
    notaVinte = (saque- notaCinquenta*50) // 20
if saque >= 10:
    notaDez = (saque - (notaCinquenta*50 + notaVinte *20)) // 10
if saque >= 5 :
    notaCinco = (saque - (notaCinquenta*50 + notaVinte *20 + notaDez *10 )) // 5
if saque >= 1:
    notaUm = (saque - (notaCinquenta * 50 + notaVinte * 20 + notaDez * 10 + notaCinco * 5)) // 1
if notaCinquenta >0 :
    print(f'notas de cinquenta : {notaCinquenta}')
if notaVinte:
    print(f'notas de vinte: {notaVinte}')
if notaDez:
    print(f'notas de dez: {notaDez}')
if notaCinco:
    print(f'notas de cinco: {notaCinco}')
if notaUm:
    print(f'notas de um: {notaUm}')