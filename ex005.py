#Faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e anterior
num = int(input('\nDigite um numero: '))
anterior = num-1
seguinte = num+1

print('Numero digitado {}, numero anterio {}, numero seguinte {}'.format(num, anterior, seguinte))