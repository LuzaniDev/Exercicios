'''
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                    Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
receberá ainda um desconto de 10% sobre este total.
Escreva um algoritmo para ler a quantidade (em Kg)de morangos
e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
'''
fruta = input(('Morango ou Maçã?: '))
peso = float(input('Quantidade Desejada em Kgs: '))
##############################################################################################
if fruta.lower() == 'morango':
    morango1 = 2.50
    morango2 = 2.20
    valor_total_M1 = (morango1 * peso)
    valor_total_M2 = (morango2 * peso)
    if peso >= 8.00:
        valor_total_M2 = (morango2 * peso)
        desconto_em_porcento = valor_total_M2 * 0.10
        resultado = valor_total_M2 - desconto_em_porcento
        print(f'O Valor total é de: {resultado:.2f}')

    elif valor_total_M2 >= 25.00:
        valor_total_M2 = (morango2 * peso)
        desconto_em_porcento = valor_total_M2 * 0.10
        resultado = valor_total_M2 - desconto_em_porcento
        print(f'O Valor total é de: {resultado:.2f}')

    elif peso <= 4.99:
        valor_total_M1 = (morango1 * peso)
        print(f'O Valor total é de: {valor_total_M1:.2f}')

    elif 5.00 <= peso <= 7.99:
        valor_total_M2 = (morango2 * peso)
        print(f'O Valor total é de: {valor_total_M2:.2f}')
    ##############################################################################################
elif fruta.lower() == 'maçã' or fruta.lower() == 'maça':
    maca1 = 1.80
    maca2 = 1.50
    valor_total_maca1 = maca1 * peso
    valor_total_maca2 = maca2 * peso
    if peso >= 8.00:
        valor_total_maca2 = maca2 * peso
        desconto_em_porcento = valor_total_maca2 * 0.10
        resultado = valor_total_maca2 - desconto_em_porcento
        print(f'O Valor total é de: {resultado:.2f}')

    elif valor_total_M2 >= 25.00:
        valor_total_maca2 = maca2 * peso
        desconto_em_porcento = valor_total_maca2 * 0.10
        resultado = valor_total_maca2 - desconto_em_porcento
        print(f'O Valor total é de: {resultado:.2f}')

    elif peso <= 4.99:
        valor_total_maca1 = (maca1 * peso)
        print(f'O Valor total é de: {valor_total_maca1:.2f}')

    elif 5.00 <= peso <= 7.99:
        valor_total_maca2 = (maca2 * peso)
        print(f'O Valor total é de: {valor_total_maca2:.2f}')
else:
    raise ValueError('Produto invalido!')

#############################################################################################################
# FORMA MAIS INTELIGENTE DE SE FAZER O MESMO CÓDIGO:


def calcular_valor_frutas(fruta, peso):
    if fruta == 'morango':
        if peso <= 4.99:
            valor_total = 2.50 * peso
        elif peso >= 5 and peso <= 7.99:
            valor_total = 2.20 * peso
        else:
            valor_total = 2.20 * peso * 0.90
    elif fruta == 'maçã' or fruta == 'maça':
        if peso <= 4.99:
            valor_total = 1.80 * peso
        elif peso >= 5 and peso <= 7.99:
            valor_total = 1.50 * peso
        else:
            valor_total = 1.50 * peso * 0.90
    else:
        raise ValueError('Produto inválido!')

    return valor_total


fruta = input('Morango ou Maçã?: ').lower()
peso = float(input('Quantidade Desejada em Kgs: '))
valor_total = calcular_valor_frutas(fruta, peso)

if peso >= 8 or valor_total >= 25:
    valor_total *= 0.90

print(f'Valor a ser pago: R$ {valor_total:.2f}')
