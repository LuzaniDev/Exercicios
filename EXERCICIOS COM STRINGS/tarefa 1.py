'''
Tamanho de strings.
Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
Compara duas strings
String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente.
'''
class calculo:
    def __init__(self):
        pass
    
    def principal(self):
        string1 = input('Digite a string 1: ')
        string2 = input('Digite a string 2: ')
        tamanho1 = len(string1)
        tamanho2 = len(string2)

        if tamanho1 == tamanho2:
            print(f'O tamanho das duas strings é o mesmo! \nString 1: "{string1}" Contem: "{tamanho1}" Caracteres')
            print(f'String 2: "{string2}" Também Contem: "{tamanho2}" Caracteres')
        else:
            print(f'O tamanho das duas strings é Diferente! \nString 1: "{string1}" Contem: "{tamanho1}" Caracteres')
            print(f'String 2: "{string2}" Contem: "{tamanho2}" Caracteres')
        if string1.lower() == string2.lower():
            print('As duas strings possuem o mesmo Conteúdo!')
        else:
            print('As duas strings possuem conteúdo Diferente!')

calcular = calculo()

calcular.principal()
 