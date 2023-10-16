# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores
# e lhe contratam para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
# baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

valor = float(input('Digite o Salario em R$: '))

if valor < 280.00:
    print('O Salário era de:', valor, 'R$', 'Com o Aumento de 20% ficou de:',
          (valor * 1.20), 'R$' ' Então Teve um Aumento de:', (valor * 0.20), 'R$')

if 280.00 <= valor <= 700.00:
    print('O Salário era de:', valor, 'R$', 'Com o Aumento de 15% ficou de:',
          (valor * 1.15), 'R$' ' Então Teve um Aumento de:', (valor * 0.15), 'R$')

if 700.00 <= valor <= 1500.00:
    print('O Salário era de:', valor, 'R$', 'Com o Aumento de 10% ficou de:',
          (valor * 1.10), 'R$' ' Então Teve um Aumento de:', (valor * 0.10), 'R$')

if valor >= 1500.01:
    print('O Salário era de:', valor, 'R$', 'Com o Aumento de 5% ficou de:',
          (valor * 1.05), 'R$' ' Então Teve um Aumento de:', (valor * 0.05), 'R$')

