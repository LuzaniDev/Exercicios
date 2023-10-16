'''
Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

F
FU
FUL
FULA
FULAN
FULANO

nome = input('Digite seu nome: ')
pontos = ""
for letras in nome:
    pontos += letras
    print(pontos)

ou
'''
nome = input('Digite seu nome: ')

for ponto in range(1, len(nome) + 1):
    print(nome[:ponto])