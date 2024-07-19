# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
# qual foi o número escolhido pelo computador
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from time import sleep
import colorama
from colorama import init, Fore, deinit
from random import randint

colorama.init()
sorte = randint(0,5)
print(sorte)
print(Fore.YELLOW, '-=-'*30)
print(Fore.BLUE,'Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print(Fore.YELLOW, '-=-'*30)
print(Fore.WHITE)
chute = int(input('Adivinhe o numero de 0 a 5: '))
print(Fore.CYAN, 'PROCESSANDO...')
sleep(2)

if sorte == chute:
    print(Fore.YELLOW,'Parabêns! Você acertou!\n')
else:
    print(Fore.RED,'Que pena! Você errou!\n')
deinit()