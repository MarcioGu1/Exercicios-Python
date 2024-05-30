# primeiros passos em python

print('olá mundo')

nome=input('Digite seu nome :')
print('É um prazer te conhecer',nome)

num1= float(input('digite um número :'))
num2 =float(input('digite um número :'))
result = x + y
print('o resultado da soma entre {} + {} = {}'.format(num1,num2,result))

obj=input('digite algo :')
print('Qual o tipo dele:',type(obj))
print ('Ele está todo minusculo ?:',obj.islower())
print('Ele é um numero ? :',obj.isnumeric())
print('Ele é uma letra? :',obj.isalpha())

obj=str(input('Qual seu nome? :'))
print ('Olá {:=^20} tudo bom?\nvamos iniciar.'.format(obj))

num = float(input('Digite um numero : '))
suce = x +1
ant = x - 1
potencia = x **2
print('o sucessor de {} é :{} \no antecessor é:{} \nseu quadrado é:{}'.format(num,suce,ant,potencia))