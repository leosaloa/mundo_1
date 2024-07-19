# Crie um  programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua posição inteira.
import math

num = float(input('Digite um numero com casa decimal separado por ponto: '))
inteiro = math.floor(num)

print('Numero inteiro {}'.format(inteiro))