# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

print ('Conversor Fahrenheit em Celsius\n')

F = float(input('Digite o valor em Fahrenheit: '))
C = 5 * ((F-32) / 9)
resultado ='{:.3f}'.format(C)

print (f'\nO Valor em Fahrenheit é equivalente a {resultado} Graus Celsius')