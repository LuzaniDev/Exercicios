'''
Faça um programa que peça o tamanho de um arquivo para download (em MB)
e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
'''
print('calculadora de tempo de download\n')

tamanho = float(input ('Qual o tamanho do arquivo?(em MB): '))
velocidade = float(input ('Qual a velocidade da internet(em Mbps): '))
calculo = tamanho / (velocidade / 8)
minutos = int(calculo // 60)
segundos = int(calculo % 60)

print('O Download Vai demorar Aproximadamente: ', minutos, 'minutos e', segundos, 'segundos')


