'''
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.
'''
while True:
    print('Bem Vindo a CalculadoRato')
    a = float(input('Digite o primeiro valor: '))
    b = float(input('Digite o segundo valor: '))
    print(f'Os Valores inseridos foram: A =  {a}  B =  {b} \n')
    print('Escolha uma das funcionalidades disponiveis:')
    escolha = int(input('''1- É par ou ímpar?
2- É positivo ou negativo?
3- É um numero inteiro ou decimal?
Digite: '''))
# 1 - #################################################################################
    if escolha == 1:
        escolha1 = (
            input('Gostaria de saber Referente ao valor de (A) ou de (B)?: '))
        if escolha1.lower() == 'a':
            resultadoA1 = a % 2
            if resultadoA1 == 0:
                print(f'O Valor de A ("{a}")é Par!')
            else:
                print(f'O Valor de A ("{a}") é impar!\n')

            restart1 = input('Deseja Recomeçar? (S) (N): ')
            if restart1.lower() == 's':
                pass
            else:
                quit(0)
        elif escolha1.lower() == 'b':
            resultadoB1 = b % 2
            if resultadoB1 == 0:
                print(f'O Valor de B ("{b}") é Par!')
            else:
                print(f'O Valor de B ("{b}") é impar!')
        else:
            print('O Valor Digitado é Invalido!\n')
            restart1 = input('Deseja Recomeçar? (S) (N): ')
            if restart1.lower() == 's':
                pass
            else:
                quit(0)
# 2 - #################################################################################
    elif escolha == 2:
        escolha2 = (
            input('Gostaria de saber Referente ao valor de (A) ou de (B)?: '))
        if escolha2.lower() == 'a':
            if a >= 0:
                print(f'O Valor de A ("{a}") é Positivo!')
            else:
                print(f'O Valor de A ("{a}") é Negativo!!')

            restart1 = input('Deseja Recomeçar? (S) (N): ')
            if restart1.lower() == 's':
                pass
            else:
                quit(0)

        elif escolha2.lower() == 'b':
            if b >= 0:
                print(f'O Valor de B ("{b}") é Positivo!')
            else:
                print(f'O Valor de B ("{b}") é Negativo!!')

            restart1 = input('Deseja Recomeçar? (S) (N): ')
            if restart1.lower() == 's':
                pass
            else:
                quit(0)
        else:
            print('O Valor Digitado é Invalido!\n')
            restart1 = input('Deseja Recomeçar? (S) (N): ')
            if restart1.lower() == 's':
                pass
            else:
                quit(0)
# 3 - #################################################################################
    elif escolha == 3:
        escolha3 = (
            input('Gostaria de saber Referente ao valor de (A) ou de (B)?: '))
        if escolha3.lower() == 'a':
            if a == int(a):
                print(f'O Valor de A ("{a}") é um numero inteiro')
            else:
                print(f'O Valor de A ("{a}") é um numero decimal')

            restart1 = input('Deseja Recomeçar? (S) (N): ')
            if restart1.lower() == 's':
                pass
            else:
                quit(0)

        elif escolha3.lower() == 'b':
            if b == int(b):
                print(f'O Valor de B ("{b}") é inteiro')
            else:
                print(f'O Valor de B ("{b}") é decimal')

            restart1 = input('Deseja Recomeçar? (S) (N): ')
            if restart1.lower() == 's':
                pass
            else:
                quit(0)
        else:
            print('O Valor Digitado é Invalido!\n')
            restart1 = input('Deseja Recomeçar? (S) (N): ')
            if restart1.lower() == 's':
                pass
            else:
                quit(0)
# ERRO - ###########################################################################
    else:
        print('O Valor Digitado é Invalido!\n')
        restart1 = input('Deseja Recomeçar? (S) (N): ')
        if restart1.lower() == 's':
            pass
        else:
            quit(0)
