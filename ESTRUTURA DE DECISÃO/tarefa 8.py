# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
cmst = 'Camiseta'
clc = 'Calça'
clcd = 'Calçado'


class Produtos:
    def __init__(self):
        self.camiseta = 0
        self.calça = 0
        self.calçado = 0

    def solicitação(self):
        self.camiseta = float(input('Digite o valor da Camiseta em R$: '))
        self.calça = float(input('Digite o valor da Calça em R$: '))
        self.calçado = float(input('Digite o valor do Calçado em R$: '))

    def decisão(self):
        if min(self.camiseta, self.calça, self.calçado) == self.camiseta:
            print('O Mais Barato dos 3 produtos é a : ', cmst,'Que custa: ',
                  min(self.camiseta, self.calça, self.calçado),'R$')

        elif min(self.camiseta, self.calça, self.calçado) == self.calça:
            print('O Mais Barato dos 3 produtos é a : ', clc,'Que custa: ',
                  min(self.camiseta, self.calça, self.calçado),'R$')

        else:
            print('O Mais Barato dos 3 produtos é o : ', clcd,'Que custa: ',
                  min(self.camiseta, self.calça, self.calçado),'R$')


produtos1 = Produtos()
produtos1.solicitação()
produtos1.decisão()


