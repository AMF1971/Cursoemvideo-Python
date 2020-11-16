# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# ex:
# Digite um número 1834
# unidade: 4 dezena: 3 centena: 8 milhar:1

'''num = int(input('Informe um número:'))
n = str(num)
print('Analisando o numero {}'.format(num))
print('UNIDADE: {}'.format(n[3]))
print('DEZENA: {}'.format(n[2]))
print('CENTENA: {}'.format(n[1]))
print('MILHAR: {}'.format(n[0]))'''

num = int(input('Informe um número:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o numero {}'.format(num))
print('UNIDADE: {}'.format(u))
print('DEZENA: {}'.format(d))
print('CENTENA: {}'.format(c))
print('MILHAR: {}'.format(m))
