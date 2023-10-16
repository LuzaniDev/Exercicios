'''
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos,
o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
'''
tipo = input('Digite o Tipo do combustível: (A)-Álcool (G)-Gasolina : ')
litros = float(input('Digite quantos litros que serão Abastecidos!: '))
valorG = float(2.50)
valorA = float(1.90)
if tipo.lower() == 'a' or tipo.lower() == 'alcool' or tipo.lower == 'álcool':
    if litros <= 19.99:
        desconto = float(f'{valorA * 0.03}')
        valor_a_pagar = (valorA * litros)
        valor_do_desconto = float(f'{desconto * litros}')
        print(
            f'O Valor a ser Pago é de: {valor_a_pagar - valor_do_desconto:.2f} E o Valor do desconto foi de: {valor_do_desconto:.2f}')
    elif litros >= 20.00:
        desconto = float(f'{valorA * 0.05}')
        valor_a_pagar = (valorA * litros)
        valor_do_desconto = float(f'{desconto * litros}')
        print(
            f'O Valor a ser Pago é de: {valor_a_pagar - valor_do_desconto:.2f} E o Valor do desconto foi de: {valor_do_desconto:.2f}')
    else:
        raise ValueError('Caractere Inválido!')

elif tipo.lower() == 'g' or tipo.lower() == 'gasolina':
    if litros <= 19.99:
        desconto = float(f'{valorG * 0.04}')
        valor_a_pagar = (valorG * litros)
        valor_do_desconto = float(f'{desconto * litros}')
        print(
            f'O Valor a ser Pago é de: {valor_a_pagar - valor_do_desconto:.2f} E o Valor do desconto foi de: {valor_do_desconto:.2f}')
    elif litros >= 20.00:
        desconto = float(f'{valorG * 0.06}')
        valor_a_pagar = (valorG * litros)
        valor_do_desconto = float(f'{desconto * litros}')
        print(
            f'O Valor a ser Pago é de: {valor_a_pagar - valor_do_desconto:.2f} E o Valor do desconto foi de: {valor_do_desconto:.2f}')
    else:
        raise ValueError('Caractere Inválido!')
else:
    raise ValueError('O Tipo de combústivel é Invalido!')
