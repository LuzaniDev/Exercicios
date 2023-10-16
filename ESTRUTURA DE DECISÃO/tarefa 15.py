'''
Faça um Programa que peça os 3 lados de um triângulo.
O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo,se o mesmo é: equilátero,
isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
'''
while True:
    a = float(input('Digite o Valor do Lado A: '))
    b = float(input('Digite o Valor do Lado B: '))
    c = float(input('Digite o Valor do Lado C: '))
    if a + b > c and a + c > b and b + c > a:
        if a == b and b == c:
            print("Triângulo Equilátero")
        elif a == b or a == c or b == c:
            print("Triângulo Isósceles")
        else:
            print("Triângulo Escaleno")
    else:
        print ('Não É um Triangulo')
        
