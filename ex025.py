# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome

name = str(input('\nDigite um nome: '))
if 'SILVA' in name.upper():
    print('\nO nome digitado contem Silva')
else:
    print('\nO nome digitado não contem Silva')