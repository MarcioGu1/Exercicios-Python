maior=0
menor=0
for pos in range (1,6):
    peso= float(input('Peso da {}ª pessoa:'.format(pos)))
    if pos == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('o maior peso é {}kg'.format(maior))
print('E o menor peso é {}kg'.format(menor))
#----------------------------------------------------------------

#variaveis
nomeMaisVelho= ' '
maiorIdade =0
somaIdades=0
mulherMenorVinte=0
men = 0
woman = 0
for pessoa in range (1,5):
    print('--------------------------{}ª CANDIDATO ----------------------'.format(d))
    #receebe dados
    nome = str(input('digite seu nome: ')).strip()
    idade = int(input('digite sua idade: '))
    somaIdades += idade
    print('[H]homen\n[F]mulher')
    sexo = str(input('qual seu sexo :')).upper()
    media = somaIdades/4
    #leitura dos dados
    if pessoa == 1 and sexo=='H':
        maiorIdade = idade
        nomeMaisVelho = nome
    if sexo =='H' and idade > maiorIdade:
        maiorIdade = idade
        nomeMaisVelho = nome
    if sexo == 'H':
        men+=1
    if sexo == 'F':
        woman+= 1
        if sexo == 'F'and idade < 20 :
           mulherMenorVinte += 1
print('A média de idades do grupo é {} anos\nTemos {} mulheres e {} homens\nO homem mais velho é o {} com {} anos\nTemos {} mulheres com menos de 20 anos'.format(media ,woman,men,nomeMaisVelho,maiorIdade,mulherMenorVinte))
#----------------------------------------------------------------
sexo=str(input('Qual seu sexo:[M/F]')) .strip() .upper()[0]
while sexo not in'MF':
    sexo = str(input('codigo invalido, por favor, qual seu sexo:[M/F]')).strip().upper()[0]
print('sexo {} recebido com sucesso'.format(sexo))
#------------------------------------------------------------------
from random import randint
computador= randint(0,10)
print('OI SOU SEU COMPUTADOR,SERA QUE VOCE CONSEGUE ME VENCER?,PEBNSEI EM UM NUMERO ENTRE 0 e 10')
certo = False
palpite= 0

while not certo:
    eu= int(input('digite seu palpite:'))
    palpite += 1
    if eu == computador:
        print('Você acertou em {} tentativas'.format(palpite))
        certo = True
    else:
       if eu < computador:
            print('Maior')
       else:
            print('Menor')
print('GOOD GAME')

    #RECEBENDO VALORES
num1 = float (input('primeiro valor:'))
num2=  float (input('segundo valor:'))
escolhaDoUsuario = 0
    #PROCESSANDO DADOS
while escolhaDoUsuario != 5:
    print('    [ 1 ] somar\n    [ 2 ] multiplicar\n    [ 3 ] maior\n    [ 4 ] novos números\n    [ 5 ] sair')
    escolhaDoUsuario = int(input('>>>>> Qual é a sua opção? '))
    if escolhaDoUsuario == 1:
        resultado = num1 + num2
        print('A soma entre {} + {} = {}'.format(num1,num2,resultado))
    elif escolhaDoUsuario == 2:
        resultado = num1 * num2
        print('A multiplicação entre {} x {} = {}'.format(num1,num2,resultado))
    elif escolhaDoUsuario == 3:
         if num1> num2:
            print(num1,'é o maior número')
         else:
             print(num2,'é o maior número')
    elif escolhaDoUsuario == 4:
        print('informe os novos valores:')
        num1 = float(input('valor:'))
        num2 = float(input('valor:'))
    elif escolhaDoUsuario == 5:
        print('finalizando ....')
    else:
        print('OPÇÃO INVALIDA')
    print('=-='*50)
print("fim,volte sempre")
