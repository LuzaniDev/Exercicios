'''
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".
'''

print("Responda às perguntas abaixo com 'sim' ou 'não'.")

respostas_positivas = 0

pergunta1 = input("Telefonou para a vítima? ").lower()
if pergunta1 == "sim":
    respostas_positivas += 1

pergunta2 = input("Esteve no local do crime? ").lower()
if pergunta2 == "sim":
    respostas_positivas += 1

pergunta3 = input("Mora perto da vítima? ").lower()
if pergunta3 == "sim":
    respostas_positivas += 1

pergunta4 = input("Devia para a vítima? ").lower()
if pergunta4 == "sim":
    respostas_positivas += 1

pergunta5 = input("Já trabalhou com a vítima? ").lower()
if pergunta5 == "sim":
    respostas_positivas += 1

if respostas_positivas == 2:
    print("Classificação: Suspeita")
elif 3 <= respostas_positivas <= 4:
    print("Classificação: Cúmplice")
elif respostas_positivas == 5:
    print("Classificação: Assassino")
else:
    print("Classificação: Inocente")

# FORMA MAIS EFICAZ DE SE FAZER O MESMO COMANDO!
breakpoint
######################################

tipo = input('Digite o Tipo do combustível: (A)-Álcool (G)-Gasolina : ')
litros = float(input('Digite quantos litros que serão Abastecidos!: '))
valorG = 2.50
valorA = 1.90

if tipo.lower() in ['a', 'alcool', 'álcool']:
    desconto = 0.03 if litros <= 20 else 0.05   ## muito inteligente essa forma de pensamento! 
    valor_por_litro = valorA
elif tipo.lower() in ['g', 'gasolina']:
    desconto = 0.04 if litros <= 20 else 0.06
    valor_por_litro = valorG
else:
    raise ValueError('O Tipo de combustível é inválido!')

valor_a_pagar = valor_por_litro * litros * (1 - desconto)

print(f'O Valor a ser Pago é de: {valor_a_pagar:.2f} E o Valor do desconto foi de: {valor_por_litro * litros * desconto:.2f}')
