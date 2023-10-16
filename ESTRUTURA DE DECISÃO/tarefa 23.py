# Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.
numero = float(input('Digite um número para saber se é inteiro ou decimal: '))

if numero == int(numero):
    print('O número é inteiro')
else:
    print('O número é decimal')