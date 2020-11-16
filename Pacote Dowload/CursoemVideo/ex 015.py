# Escreva um programa que pergunta a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado . Calcule o preço a pagar. sabendo
# que o carro custa R460 por dia e R4 0,15 por km rodado.

dias = int(input('Quantos dias Alugados?'))
km = float(input('Quantos Km rodados:'))
pago = (dias * 60) + (km * 0.15)
print('O Total a pagar é de R${:.2f}'.format(pago))


