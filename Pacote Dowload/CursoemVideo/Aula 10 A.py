'''nome = str(input('Qual é o seu nome?'))
if nome == 'Marcos':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom Dia, {}'.format(nome))'''

'''n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m = (n1 + n2)/2
print('A sua média é {}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS')
else:
    print('Sua média foi ruim! ESTUDE MAIS')'''

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m = (n1 + n2)/2
print('A sua média Foi: {:.1f}'.format(m))
print('PARABÉNS!' if m >= 6 else 'Estude Mais! ')

