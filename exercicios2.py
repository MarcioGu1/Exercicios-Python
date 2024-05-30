# Mexendo com numeros

print('BEM-VINDO AO CALCULA MÉDIA')
num1  = float(input('AV1:'))
num2  = float(input('AV2:'))
media = (num1+num2)/2

if media >= 7.0:
    print('sua media do bimestre é {:.1f} você está aprovado parabéns'.format(media))
elif media < 5:
    print('você ta reprovado, estude mais!!!')
else:
    print('você esta de recuperação , se esforce mais')
#----------------------------------------------------------------
print  ('Conversora de medidas')
num = float (input('digite o valor : '))
und = str (input("Qual unidade de medida ele está[metro,centimetro ou quilômetro]? : ")).lower().strip().split()

if und[0] == 'm':
    print('km:{}\nhm:{}\ndcm:{}\nm:{}\ndm:{:0f}\ncm:{:.0f}\nmm:{:.0f}'.format(num/1000, num/100, num/10, num/1, num*10, num*100, num*1000))
elif und[0] == "c":
    print('km:{}\nhm:{}\ndcm:{}\nm:{}\ndm:{:0f}\ncm:{:.0f}\nmm:{:.0f}'.format(num / 100000, num / 10000, num / 1000, num / 100,
                                                                             num / 10, num * 1, num * 10))
else :
    print('km:{}\nhm:{}\ndcm:{}\nm:{}\ndm:{:0f}\ncm:{:.0f}\nmm:{:.0f}'.format(num * 1, num * 10, num * 100, num * 1000,
                                                                             num * 10000, num * 100000, num * 1000000))
#----------------------------------------------------------------
from math import cos,sin,tan
num =float(input('digite um número:'))
print('seu seno é :{}\nseu cosseno é:{}\nsua tangente é:{}'.format(sin(num),cos(num),tan(num)))
----------------------------------------------------------------
num=int(input('digite o número :'))
u =num//1%10
d =num//10%10
c =num//100%10
m =num//1000%10
print('Analisando o numero:{}'.format(num))
print('milhar:{}\ncentenas:{}\ndezenas:{}\nunidades:{}'.format(m,c,d,u))
print('-'*40)
#----------------------------------------------------------------
from random import randint
from time import sleep
print('-=-'*50)
print('Vou pensar em um numero entre 0 e 5, tente adivinhar . . .')
print('-=-'*50)
maquina =randint(0,5)
palpite =int(input('digite seu palpite:'))
print('PROCESSANDO . . .')
sleep(3)
if palpite == maquina:
   print('Parabéns você me ganhou')
else:
    print('achou errado otário, era {}'.format(maquina))