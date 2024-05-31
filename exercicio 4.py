from datetime import date
ano =int(input('digite o ano:'))
if ano == 0:
    ano =date.today().year
if ano%4 == 0 and ano%100 !=0 or ano%400 == 0:
    print('esse ano de {} é bissexto'.format(ano))
else:
    print('o ano {} não é bissexto'.format(ano))
#----------------------------------------------------------------
print('---'*50)
print(' conversor de bases')
print('---'*50)

num1 = int ( input('digite o valor:'))
print(' [ 1 ] binário \n [ 2 ] octal \n [ 3 ] hexagonal' )
opcao= int( input('digite a opção :'))
if opcao == 1:
   print('{} convertido para binário é: {}'.format(num1,bin(num1)[2:]))
elif opcao == 2:
   print('{} convertido para octal é : {}'.format(num1,oct(num1)[2:]))
elif opcao == 3:
    print('{} convertido para hexagonal é : {}'.format(num1,hex(num1)[2:]))
else:
    print('opção invalida.')
#----------------------------------------------------------------
num1= float (input ('valor :'))
num2= float (input ('valor :'))
result = num1 - num2
if result > 0:
    print('o PRIMEIRO valor é maior')
elif result < 0:
    print('o SEGUNDO valor é maior')
else :
    print('os valores sao iguais')
#----------------------------------------------------------------
from datetime import date
ano_atual = date.today().year
print('qual seu sexo :\n [1] homem \n [2] mulher')
sexo = int(input('digite a opção:'))
ano_nasc = int(input('seu ano de nascimento:'))
idade = ano_atual - ano_nasc

if sexo == 1 :
    if idade == 18 :
        print('\033[1;4;31m alerta , se aliste o mais rapido, é seu momento\033[0;m')
    elif idade == 19:
        print ('\033[1;32m seu alistamento foi a 1 ano \033[0;m','\n seu alistamento ocorreu no ano de {}'.format(ano_atual-1))
    elif idade > 19:
       print('\033[1;32m seu alistamento passou a {} anos \033[0;m','\n seu alistamento ocorreu no ano de {}'.format(idade-18,ano_atual-(idade - 18)))
    elif idade == 17:
        print('\033[1;33m falta 1 ano para seu alistamento \033[0;m','\033[;43m seu alistamento será em {}\033[0;m'.format(ano_atual+ 1))
    else:
        print('\033[1;33m falta {} anos para seu alistamento \033[0;m','\n seu alistamento sera no ano de {}'.format(18 - idade,(18-idade) + ano_atual))
else:
    print('Por você ser do sexo feminino seu alistamento não é obrigatório')