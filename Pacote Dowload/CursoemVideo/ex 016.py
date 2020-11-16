#Crie um programa que leia um número Real qialquer pelo teclado e mostre na tela a sua porção inteira.


'''from math import trunc
num = float(input('Digite um valor:'))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, trunc(num)))'''


'''num = float(input('Digite um valor:'))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, int(num)))'''

import math
num = float(input('Digite um valor:'))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, math.trunc(num)))




