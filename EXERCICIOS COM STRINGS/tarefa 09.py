'''
Verificação de CPF.
Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx
e indique se é um número válido ou inválido através da validação dos dígitos verificadores
e dos caracteres de formatação.
'''
while True:
    cpf = input('Digite seu CPF no formato xxx.xxx.xxx-xx: ')
    
    # Remover pontos e hífen do CPF para validar se contém apenas dígitos numéricos.
    cpf_numerico = cpf.replace('.', '').replace('-', '')
    
    if not cpf_numerico.isdigit() or len(cpf_numerico) != 11:
        raise ValueError('O formato digitado está incorreto! O CPF deve conter 11 dígitos numéricos.')
    
    if cpf[3] != '.' or cpf[7] != '.' or cpf[11] != '-':
        raise ValueError('O formato digitado está incorreto! O CPF deve estar no formato xxx.xxx.xxx-xx.')
    
    print('CPF correto:', cpf)
    break