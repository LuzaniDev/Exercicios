'''
Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

quantos espaços em branco existem na frase.
quantas vezes aparecem as vogais a, e, i, o, u.
'''
valor = input('digite algo: ')
espacos = valor.count(' ')
vogais = valor.count('a') + valor.count('e') + valor.count('i') + valor.count('o') + valor.count('u')
print(f'Nesta frase existem: {espacos} espaços em branco e existem: {vogais} vogais')