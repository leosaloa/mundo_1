# Faça um programa que leia o comprimento do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa
import math

a = float(input('\nDigite o cateto adjacente: '))
b = float(input('\nDigite o cateto oposto: '))
r = (a**2)+(b**2)

h = math.sqrt(r)

print(f'A hipotenusa é {h:.2f}')