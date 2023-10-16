'''
Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''

def calculo_de_eficiencia (area_em_metros_quadrados):

    litros_de_tinta = area_em_metros_quadrados / 3

    latas_de_tinta = (litros_de_tinta + 17) // 18

    Valor_total = latas_de_tinta * 80
    
    return latas_de_tinta, Valor_total

area_em_metros = float(input('Digite o Tamanho da área em Metros quadrados: '))

litros_de_tinta, Valor_total = calculo_de_eficiencia(area_em_metros)

print(f"\nQuantidade de latas de tinta a serem compradas: {litros_de_tinta}")
print(f"Preço total: R$ {Valor_total:.2f}")
