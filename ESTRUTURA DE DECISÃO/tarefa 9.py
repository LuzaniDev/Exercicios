#Faça um Programa que leia três números e mostre-os em ordem decrescente.

Numero1 = float(input('1- Digite O Primeiro Numero: '))
Numero2 = float(input('2- Digite O Segundo Numero: '))
Numero3 = float(input('3- Digite O Terceiro Numero: '))

numeros = [Numero1, Numero2, Numero3]

numeros_ordenados = sorted(numeros, reverse=True)

print("Números em ordem decrescente:")
for num in numeros_ordenados:
    print(num)

