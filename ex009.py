# Faça um programa que leia um numero inteiro qualquer e mostre na tela sua tabuada
num = int(input('\nDigite um numero: '))

for i in range(1, 11):
    print(f'{num} x {i:>2} = {num*i}')