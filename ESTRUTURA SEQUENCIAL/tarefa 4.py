#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

print ('NOTA BIMESTRAL\n')

matematica = float(input('Digite sua nota de matematica: '))
portugues = float(input('Digite sua nota de português: '))
historia = float(input('Digite sua nota de historia: '))
inglês = float(input('Digite sua nota de inglês: '))

nota =  (matematica + portugues + historia + inglês) /4

print ('\nSua média este Bimestre foi de: ',nota,'\n')