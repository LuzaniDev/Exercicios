#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
genero = input('Qual seu genero? F - Feminino, M - Masculino: ')
if genero.lower() == 'f' or genero.lower() == 'feminino':
    print('Seu Genero é F - Feminino')

elif genero.lower() == 'M' or genero.lower() == 'masculino':
    print('Seu Genero é M - Masculino')
else:
    print('Sexo Inválido.')
    

