#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

print('Bem Vindo a Calculadora de peso ideal!\n')
altura = float(input('Digite sua altura: '))

peso_ideal = (72.7*altura) - 58

print ('Seu Peso ideal baseado na sua altura é: ', peso_ideal)