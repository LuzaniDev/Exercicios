'''
Faça um Programa que peça 2 números inteiros e um número real. 
Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.
'''
# NÃO ATRIBUIR #
numero_1 = int(input('Digite o Valor do numero A: '))
numero_2 = int(input('Digite o Valor do numero B: '))
numero_3 = float(input('Digite o valor do numero C: '))

resultado_A = (2 * numero_1 ) * (numero_2 / 2)
print ('O valor da soma A: ', resultado_A)
resultado_B = (3 * numero_1) + numero_3
print('O valor da soma B: ', resultado_B)
resultado_C = numero_3 ** 3
print('O valor da soma C: ', resultado_C)