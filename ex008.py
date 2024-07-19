# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
metros = float(input('\nDigite o valor em metros: '))
centimetros = metros*100
milimetros = metros*1000

print('Metros: {}\nCentimetros: {}\nMilimetros: {}'.format(metros, centimetros, milimetros))