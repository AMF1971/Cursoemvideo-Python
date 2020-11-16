# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
# e mostre seu status, de acordo com a tabela abaixo:
#
# – IMC abaixo de 18,5: Abaixo do Peso
#
# – Entre 18,5 e 25: Peso Ideal
#
# – 25 até 30: Sobrepeso
#
# – 30 até 40: Obesidade

peso = float(input('Qual é seu peso? (Kg)'))
altura = float(input('Qual é sua altura? (m)'))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'. format(imc))
if imc < 18.5:
    print('Você esta ABAIXO DO PESO normal')
elif imc >= 18.5 and imc < 25:
    print('PARABÉNS você está na faixa de PESO IDEAL')
elif imc >= 25 and imc < 30:
    print('Você esta em SOBREPESO')
elif imc >= 30 and imc < 40:
    print('Você esta na faixa de OBSIDADE ')
else:
    print('Você esta em OBSEDIDADE MÓRBIDA, cuidado!')


