# Faça um programa que leia três números e mostre qual é o MAIOR e qual é o Menor.

num = int(input('\nDigite o primeiro numero: '))
num2 = int(input('\nDigite o segundo numero: '))
num3 = int(input('\nDigite o terceiro numero: '))

verificar = [num, num2, num3]
verificar.sort()

print(f'\nO numero MENOR é o {verificar[0]}\nO numero MAIOR é o {verificar[-1]}')