# Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

print ('Esse ano é bissexto?')
ano = int(input('Digite o ano ex:1891 : '))

if ano == (ano % 4 == 0 and ano % 100 == 0) or ano % 400 == 0 :
    print('Sim, é um ano bissexto!')
else:
    print('Não é um ano bissexto!')