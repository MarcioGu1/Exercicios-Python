from datetime import date
nasc = int (input ('seu ano de nascimento:'))
idade = date.today().year - nasc
print('olá, você tem {} anos'.format(idade))
if idade <= 9 :
    print('sua categoria é Mirim')
elif idade <= 14 :
    print('sua categoria é infantil')
elif idade <= 19 :
    print('sua categoria é JUNIOR')
elif idade <= 25 :
    print('sua categoria é seniôr')
else:
    print('sua categoria é MASTER')
#----------------------------------------------------------------
peso = float( input( 'Qual seu peso (Kg):'))
altura = float( input( 'Qual sua altura (m) :'))
imc = peso/altura**2
print("{:.1f}".format(imc))
if imc < 18.5:
    print('\033[1;45mvocê esta abaixo do peso\033[0;m')
elif imc < 25 :
    print('\033[1;42mseu peso é ideal\033[0;m')
elif imc < 30 :
    print('\033[1;43você esta sobreopeso\033[0;m')
elif imc < 40 :
    print('\033[1;45mvocê esta obeso\033[0;m')
else:
    print('\033[1;41mvocê ta na obesidade morbida, se cuide imediatamente !!!\033[0;m')
#----------------------------------------------------------------

print('{:=^40}'.format('MERCADINHO DA VOVÓ'))
valor= float(input('Valor da compra : R$'))
print('[ 1 ] à vista no dinheiro\n[ 2 ] à vista cartão\n[ 3 ] 2x no cartão\n[ 4 ] 3x no cartão\n[ 5 ] mais vezes no cartão')
opcao= int(input('Qual a opção de pagamento : '))
if opcao == 5 :
    parcelas =int(input('Quantas parcelas :'))
    if parcelas > 12:
        print('\033[1;41merror\033[0;m opção invalida')
    else:
        print('sua compra será parcelada em {} parcelas de R${} com juros',
              'sua compra passa de {} para {} por causa dos juros'.format(parcelas, (valor*1.20)/parcelas,valor,valor*1.20))
elif opcao == 1:
    print('Parabéns sua compra foi finalizada, você recebeu um desconto de 10% , sua compra saiu por R$ {}'.format(valor*0.9))
elif opcao == 2:
    print('Parabéns sua compra foi finalizada, você recebeu um desconto de 5% , sua compra saiu por R$ {}'.format(valor*0.95))
elif opcao == 3:
    print('Parabéns sua compra foi finalizada,sua compra saiu em 2 parcelas de  R$ {}'.format(valor/2))
elif opcao == 4:
    print('Parabéns sua compra foi finalizada, você recebeu um acrescimo de 20% devido ao juros , sua compra saiu por R$ {} em parcelas de R$ {}'.format(valor*1.20,(valor*1.20)/3))
else:
    print('\033[1;41merror\033[0;m opção invalida')
#----------------------------------------------------------------
from random import randint
from time import sleep
itens = ('pedra' ,'tesoura','papel')
print('Suas opções :\n 0 pedra\n 1 tesoura\n 2 papel')
player = int (input('Qual é a sua jogada:'))
maquina = randint(0,2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO !!!')
sleep(2)

if player >2:
    print('\033[1;31mJOGADA INVALIDA\033[0;m')
else:
    print('sua escolha: {}'.format(itens[x]))
    print('escolha da máquina: {}'.format(itens[y]))
    if player == maquina:
        print('empate')
    elif player == 0 and maquina == 1:
        print('Você ganhou')
    elif player == 1 and maquina == 2:
        print('Você ganhou')
    elif player == 2 and maquina == 0:
        print('Você ganhou')
    else:
        print('Você perdeu')
#----------------------------------------------------------------
from datetime import date
cont = 0
num = 0
for pos in range (1,8):
    ano = int (input('que ano a {}ª pessoa nasceu?'.format(pos)))
    idade = date.today().year -ano
    if idade >= 18:
        cont += 1
    if idade < 18:
        num += 1
print('Ao total temos {} maiores de idade \ne {} menores de idade'.format(cont,num))
