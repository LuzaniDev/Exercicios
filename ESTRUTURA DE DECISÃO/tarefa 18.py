#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
while True:
    dia = int(input('Digite o Dia: '))
    mes = int(input('Digite o Mês: '))
    ano = int(input('Digite o Ano: '))
    data = (f'{dia}/{mes}/{ano}')

    if 1 <= dia <= 31 and 1 <= mes <= 12 and 1000 <= ano <= 3000:
        print (f'A Data informada é: {data}')
    else:
        raise ValueError('Data Incorreta!')