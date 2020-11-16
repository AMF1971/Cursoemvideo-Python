# Escreva um programa que converta uma temperatura digitada em Graus C e converta para Graus F.

c = float(input(' Informe a temperatura em Graus C:'))
f = ((9 * c) / 5) + 32
print('A temperatura de {}Graus C corresponde a {} Graus F!'.format(c, f))
