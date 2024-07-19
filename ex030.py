# Crie um programa que leia um numero inteiro e mostre na tela se ele é PAR ou ÍMPAR

from colorama import init, Fore, deinit
num = int(input('\nEscreva um numero: '))
tipo = num%2

init()
if tipo == 0:
    print(Fore.LIGHTBLUE_EX, 'Numero PAR', Fore.RESET)
else:
    print(Fore.LIGHTBLUE_EX, 'Numero IMPAR', Fore.RESET)

deinit()