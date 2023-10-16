'''
Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice-versa.
Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados.
A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados.
Faça um programa que leia uma seqüência de caracteres, mostre-a e diga se é um palíndromo ou não.
'''


class verificacao:

    def init(self):
        pass

    def verificar(self, valor):
        valor = input('Digite uma palavra: ')
        valor1 = valor.replace(" ", "")
        conversao = valor1[::-1]

        if valor1 == conversao:
            print(f'A palavra digitada "{valor}" é um Palíndromo!')
        else:
            print(f'A palavra digitada "{valor}" não é um Palíndromo!')

        return valor
chamada = verificacao()
chamada.verificar('')


