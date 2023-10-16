# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra = input('Digite uma letra: ')
vogais = 'aeiou'
if letra.lower() in vogais:
    print('A Letra digitada é uma Vogal!')
else:
    print('A Letra digitada é uma Consoante!')
    
