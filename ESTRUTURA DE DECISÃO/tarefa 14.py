'''
Faça um programa que lê as duas notas parciais obtidas por um aluno
numa disciplina ao longo de um semestre, e calcule a sua média.
A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
'''

matematica = float(input('Digite sua nota de matematica: '))
portugues = float(input('Digite sua nota de português: '))
historia = float(input('Digite sua nota de historia: '))
inglês = float(input('Digite sua nota de inglês: '))

media =  (matematica + portugues + historia + inglês) /4

if 0 <= media <= 4.00:
    print(f'Média de aproveitamento: {media} Conceito Atribuido: E')
elif 4.01 <= media <= 6.00:
    print(f'Média de aproveitamento: {media} Conceito Atribuido: D')
elif 6.01 <= media <= 7.5:
    print(f'Média de aproveitamento: {media} Conceito Atribuido: C')
elif 7.51 <= media <= 9.00:
    print(f'Média de aproveitamento: {media} Conceito Atribuido: B')
elif 9.01 <= media <= 10.00:
    print(f'Média de aproveitamento: {media} Conceito Atribuido: A')
else:
    print('Valor Invalido!')
    raise ValueError('Valor Invalido!')
