#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

print('Conversor de Celsius em Fahrenheit\n')

C = float(input('Digite a Temperatura graus Celsius: '))
F = (C * 9 / 5) + 32
resultado = '{:.3f}'.format (F)

print (f'\nO Valor da Temperatura em graus Celsius é equivalente a: {resultado} Fahrenheits')