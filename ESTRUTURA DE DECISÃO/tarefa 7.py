#Faça um Programa que leia três números e mostre o maior e o menor deles.
valor1 = float(input('1- Digite um Numero: '))
valor2 = float(input('2- Digite outro Numero: '))
valor3 = float(input('3- Digite mais uma vez um Numero: '))

if valor1 > valor2 or valor1 > valor3:
    print ('\nO 1- é o numero de valor mais alto = ', valor1)
elif valor2 > valor1 or valor2 > valor3:
    print ('\nO 2- é o numero de valor mais alto = ', valor2)
elif valor3 > valor1 or valor3 > valor2:
    print ('\nO 3- é o numero de valor mais alto: = ', valor3)
else:
    print('Numeros Repetidos!!! ERRO!')
    
if valor1 < valor2 or valor1 < valor3:
    print ('O 1- é o numero de valor menor = ', valor1)
elif valor2 < valor1 or valor2 < valor3:
    print ('O 2- é o numero de valor menor = ', valor2)
elif valor3 < valor1 or valor3 < valor2:
    print ('O 3- é o numero de valor menor = ', valor3)
else:
    print('Numeros Repetidos!!! ERRO!')

