'''lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
# Tuplas são imutáveis
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')'''

'''lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
for cont in range(0, len (lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi pra caramba!')'''

'''lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!')'''

'''lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(sorted(lanche))'''

'''a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)'''

'''pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)'''

pessoa = ('Gustavo', 39, 'M', 99.88)
del(pessoa)
print(pessoa)