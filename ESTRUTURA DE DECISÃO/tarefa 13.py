# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.


while True:
    press = (int(input('Digite um numero de 0 a 7: ')))
    
    if press == 1:
        print('1 = Domingo')
    elif press == 2:
        print('2 = Segunda - Feira')
    elif press == 3:
        print('3 = Terça - Feira')
    elif press == 4:
        print('4 = Quarta - Feira')
    elif press == 5:
        print('5 = Quinta - Feira')
    elif press == 6:
        print('6 = Sexta - Feira')
    elif press == 7:
        print('7 = Sábado')
    else:
        print('Valor Invalido!')
        raise ValueError('Valor Invalido!')
    