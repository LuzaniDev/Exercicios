'''
Faça um programa para o cálculo de uma folha de pagamento,
sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo)
e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
'''
print('Calculadora Salárial\n')

valor_hora = float(input('Valor ganho por hora: '))
horas_trabalhadas = float(input('Horas trabalhadas no Mês: '))
salario_bruto = float(valor_hora * horas_trabalhadas)
if salario_bruto <= 900.00:
    IR = (salario_bruto * 0.00)
    INSS = (salario_bruto * 0.10)
    FGTS = (salario_bruto * 0.11)
    total_de_descontos = (IR + INSS)
    salario_liquido = salario_bruto - (IR + INSS)

    print('Informações Salariais\n')

    print(f'{"Salário Bruto:":30} : R$ {salario_bruto:.2f} ')
    print(f'{"(-) IR (5%)":30} : R$ {IR:.2f} ')
    print(f'{"(-) INSS (10%)":30} : R$ {INSS:.2f} ')
    print(f'{"FGTS (11%)":30} : R$ {FGTS:.2f} ')
    print(f'{"Total de descontos":30} : R$ {total_de_descontos:.2f} ')
    print(f'{"Salário Liquido":30} : R$ {salario_liquido:.2f} ')

if 900.01 <= salario_bruto <= 1500.00:
    IR = (salario_bruto * 0.05)
    INSS = (salario_bruto * 0.10)
    FGTS = (salario_bruto * 0.11)
    total_de_descontos = (IR + INSS)
    salario_liquido = salario_bruto - (IR + INSS)

    print('Informações Salariais\n')

    print(f'{"Salário Bruto:":30} : R$ {salario_bruto:.2f} ')
    print(f'{"(-) IR (5%)":30} : R$ {IR:.2f} ')
    print(f'{"(-) INSS (10%)":30} : R$ {INSS:.2f} ')
    print(f'{"FGTS (11%)":30} : R$ {FGTS:.2f} ')
    print(f'{"Total de descontos":30} : R$ {total_de_descontos:.2f} ')
    print(f'{"Salário Liquido":30} : R$ {salario_liquido:.2f} ')

if 1500.01 <= salario_bruto <= 2500.00:
    IR = (salario_bruto * 0.10)
    INSS = (salario_bruto * 0.10)
    FGTS = (salario_bruto * 0.11)
    total_de_descontos = (IR + INSS)
    salario_liquido = salario_bruto - (IR + INSS)

    print('Informações Salariais\n')

    print(f'{"Salário Bruto:":30} : R$ {salario_bruto:.2f} ')
    print(f'{"(-) IR (5%)":30} : R$ {IR:.2f} ')
    print(f'{"(-) INSS (10%)":30} : R$ {INSS:.2f} ')
    print(f'{"FGTS (11%)":30} : R$ {FGTS:.2f} ')
    print(f'{"Total de descontos":30} : R$ {total_de_descontos:.2f} ')
    print(f'{"Salário Liquido":30} : R$ {salario_liquido:.2f} ')

if salario_bruto >= 2500.01:
    IR = (salario_bruto * 0.20)
    INSS = (salario_bruto * 0.10)
    FGTS = (salario_bruto * 0.11)
    total_de_descontos = (IR + INSS)
    salario_liquido = salario_bruto - (IR + INSS)

    print('Informações Salariais\n')

    print(f'{"Salário Bruto:":30} : R$ {salario_bruto:.2f} ')
    print(f'{"(-) IR (5%)":30} : R$ {IR:.2f} ')
    print(f'{"(-) INSS (10%)":30} : R$ {INSS:.2f} ')
    print(f'{"FGTS (11%)":30} : R$ {FGTS:.2f} ')
    print(f'{"Total de descontos":30} : R$ {total_de_descontos:.2f} ')
    print(f'{"Salário Liquido":30} : R$ {salario_liquido:.2f} ')
