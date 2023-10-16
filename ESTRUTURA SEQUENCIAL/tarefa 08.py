#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

print ('Calculadora Salarial\n')

valor_hora = float(input('Valor ganho por hora é de: '))
horas_trabalhadas = float(input('Horas trabalhadas é de: '))

resultado = horas_trabalhadas * valor_hora
print('\nSeu Salario é de: ',resultado)