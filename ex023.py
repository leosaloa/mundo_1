# Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados
# Exemplo: Digite um numero: 1834
# unidade: 4     dezena: 3      centena: 8      milhar: 1 

num = int(input('\nDigite um numero de 0 a 9999: '))
uni = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10

print(f'\nUnidade: {uni}')
print(f'\nDezena: {dez}')
print(f'\nCenteza: {cen}')
print(f'\nMilhar: {mil}')