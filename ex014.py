# Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF

c  = float(input('Digite o ºC a ser convertido em ºF: '))

f = (c * 9 / 5) + 32

print('A temperatura {} ºC corresponde a {} ºF!.'.format(c, f))