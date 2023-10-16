#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

from math import pi
print ('Calculadora de area\n')
raio = float(input('Digite o Raio do circulo: '))
resultado = '{:.3f}'.format (pi * raio **2)

print ('A area do circulo é de: ', resultado)