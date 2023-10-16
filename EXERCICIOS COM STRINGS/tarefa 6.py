'''
Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.

Data de Nascimento: 29/10/1973
Você nasceu em  29 de Outubro de 1973.
'''
from datetime import datetime 

data1 = input('Digite a sua data de nascimento no formato (dd/mm/aaaa): ')
data = datetime.strptime(data1, '%d/%m/%Y')

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
mes_extenso = meses[data.month - 1]

data_completa = datetime.strftime(data, '%d/%m/%Y')
print(f'Data de Nascimento: {data_completa}')
print(f'Você nasceu em {data.day} de {mes_extenso} de {data.year}.')

