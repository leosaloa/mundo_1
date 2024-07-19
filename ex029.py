# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada KM acima do limite.

from colorama import Fore, init, deinit
carro = int(input('\nDigite a velocidade do carro: '))
limite = 80
multa_km = 7
valor = (carro-limite) * multa_km

init()
if carro > limite:
    print(Fore.RED, 'MULTADO! O carro ultrapassou o limite da via, o valor da multa é', Fore.YELLOW, f'R$ {valor:.2f}')
else:
    print(Fore.GREEN, 'Velocidade dentro do limite.')
print(Fore.BLUE, '\nTenha um bom dia! Dirija com segurança!')

deinit()