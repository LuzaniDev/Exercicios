'''
Faça um Programa que pergunte em que turno você estuda.
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
'''
turno = input('Digite qual o seu turno: M-Matutino ou V-Vespertino ou N-Noturno: ')

if turno.lower() == 'm' or turno.lower() == 'matutino':
    print('Bom Dia!')

elif turno.lower() == 'v' or turno.lower() =='vespertino':
    print('Boa Tarde!')

elif turno.lower() == 'n' or turno.lower() =='noturno':
    print('Boa Noite!')
else:
    print ('Valor Inválido')
    
