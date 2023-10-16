'''
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
'''

print('Bem Vindo a Calculadora Tintas Brasil!')



while True:
    escolha = input('Gostaria de ver com 10% de folga? s/n : ')

    if escolha.lower() == 's' or escolha.lower() == 'sim':
        area_em_metros_quadrados = float(input('Digite o Tamanho da área em Metros Quadrados: '))
        print('Versão com 10% de folga: ')
        #################### infos ########################
        area_com_folga = area_em_metros_quadrados * 1.1
        folga_litros_de_tinta = area_com_folga / 6
        folga_lata_1 = (folga_litros_de_tinta + 17) // 18
        folga_preço_lata_1 = folga_lata_1 * 80
        folga_lata_2 = (folga_litros_de_tinta + 3.5) // 3.6
        folga_preço_lata_2 = folga_lata_2 * 25
        ############################################
        print ('80 Litros com 10% de folga:')
        print(f'Quantidade de latas de tinta a serem compradas: {folga_lata_1}')
        print(f'Preço total: R$ {folga_preço_lata_1:.2f}\n')

        print('25 Litros com 10% de folga:')
        print(f'Quantidade de latas de tinta a serem compradas: {folga_lata_2}')
        print(f'Preço total: R$ {folga_preço_lata_2:.2f}')

    elif escolha.lower() == 'n' or escolha.lower() == 'não' or escolha.lower() == 'nao':
        area_em_metros_quadrados = float(input('Digite o Tamanho da área em Metros Quadrados: '))
        print ('\nversão sem folga: \n')
        ################# infos ######################
        litros_de_tinta = area_em_metros_quadrados / 6
        lata_1 = (litros_de_tinta + 17) // 18
        preço_lata_1 = lata_1 * 80
        lata_2 = (litros_de_tinta + 3.5) // 3.6
        preço_lata_2 = lata_2 * 25
        ############################################
        print ('80 Litros:')
        print(f'Quantidade de latas de tinta a serem compradas: {lata_1}')
        print(f'Preço total: R$ {preço_lata_1:.2f}\n')

        print('25 Litros:')
        print(f'Quantidade de latas de tinta a serem compradas: {lata_2}')
        print(f'Preço total: R$ {preço_lata_2:.2f}')
    else:
        resposta = input('Opção inválida. Deseja tentar novamente? "s" ou "n". ')
        if resposta.lower() == 's' or escolha.lower() == 'sim':
            pass
        else:
            break

        
