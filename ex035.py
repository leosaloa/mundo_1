# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

num1 = float(input('\nDigite o primeiro comprimento: '))
num2 = float(input('\nDigite o segundo comprimento: '))
num3 = float(input('\nDigite o terceiro comprimento: '))

if (num1 + num2) > num3 and (num2 + num3) > num1 and (num1 + num3) > num2:
    print('\nPode formar um triângulo.')
else:
    print('\nNão pode formar um triângulo.')