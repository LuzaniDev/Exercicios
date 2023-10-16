'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês,
sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
'''
print ('Descontos do das horas trabalhadas no Mês')

valor_hora = float(input('Valor ganho por hora é de: '))
horas_trabalhadas = float(input('Horas trabalhadas no Mês é de: '))
#################################################################################################################################
resultado = horas_trabalhadas * valor_hora
imposto = (resultado * 0.11)
inss = (resultado * 0.08)
sindicato = (resultado * 0.05)
resultado_com_descontos = (resultado - imposto - inss - sindicato)
#################################################################################################################################
print('seu valor a pagar ao Imposto de Renda é: ', imposto)
print('seu valor a pagar ao INSS é: ', inss)
print('seu valor a pagar ao Sindicato é: ', sindicato)
print('\nSeu Salario com descontos é de: ', resultado_com_descontos)

