# Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão)

numero = int(input('Digite um Numero para saber se é impar ou par: '))
resultado = numero % 2
if resultado == 0:
    print('é Par!')
else:
    print('é impar!')