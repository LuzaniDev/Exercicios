'''
Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada pelo aluno e apresentar:
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.
'''
while True:
    matematica = float(input('Digite a nota de matemática: '))
    ingles = float(input('Digite a nota de Inglês: '))
    espanhol = float(input('Digite a nota de Espanhol: '))
    media = (matematica + ingles + espanhol) / 3
    if 7.00 <= media <= 9.99:
        print (f'Aprovado! Nota: {media:.2f}')
    elif media == 10:
        print(f'Aprovado com Distinção! Nota: {media:.2f}')
    else:
        print (f'Reprovado! Nota:{media:.2f}')
        
        
        
        
        
