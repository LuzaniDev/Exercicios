'''
Tendo como dado de entrada a altura (h) de uma pessoa,
construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
'''
print('Bem Vindo a Calculadora de peso ideal!\n')
genero = input('Gostaria de calcular para Homem ou Mulher:  (H)/(M)?: ')
genero1 = genero.lower()

if genero1 == 'h' or genero1 == 'homem':
    altura = float(input('Digite sua altura: \n'))
    peso_ideal_H = (72.7*altura) - 58
    print(f'Seu Peso ideal baseado na sua altura é: {peso_ideal_H:.2f}')

elif genero1 == 'm' or genero1 == 'mulher':
    altura = float(input('Digite sua altura: '))
    peso_ideal_M = (62.1*altura) - 44.7
    print(f'Seu Peso ideal baseado na sua altura é: {peso_ideal_M:.2f}')

else:
    print('O Valor Digitado esta incorreto!\n')  # aparecera para o usuario
    raise ValueError
