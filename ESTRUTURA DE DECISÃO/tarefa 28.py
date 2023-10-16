'''
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
porém não há limites para a quantidade de carne por cliente.
Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.
Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal,
contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
'''

class hipermercado:
    def __init__(self):
        pass

    def carnes(self,carne, peso):
        if carne == 'file_duplo':
            if peso <= 4.99:
                valor_total = 4.90 * peso
            elif peso >= 5.00:
                valor_total = 5.80 * peso
        elif carne == 'alcatra':
            if peso <= 4.99:
                valor_total = 5.90 * peso
            elif peso >= 5.00:
                valor_total = 6.80 * peso
        elif carne == 'picanha':
            if peso <= 4.99:
                valor_total = 6.90 * peso
            elif peso >= 5.00:
                valor_total = 7.80 * peso
        else:
            raise ValueError('Produto inválido!')

        return valor_total
    
    def cartao_desconto(self, valor_total):
        desconto = valor_total * 0.05
        valor_com_desconto = valor_total - desconto

        return valor_com_desconto
    
def main():
    hiper = hipermercado()

    carne = input("Digite a carne desejada (file_duplo, alcatra, picanha): ")
    peso = float(input("Digite o peso da carne em kg: "))
    
    valor_total = hiper.carnes(carne, peso)
    print(f"Valor total da carne: R${valor_total:.2f}")

    valor_com_desconto = hiper.cartao_desconto(valor_total)
    print(f"Valor com desconto do cartão: R${valor_com_desconto:.2f}")

    desconto = valor_total * 0.05
    print(f'Valor do desconto: R${desconto:.2f}')

if __name__ == "__main__":
    main()
