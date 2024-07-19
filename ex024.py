# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

cidade = str(input('\nDigite o nome de uma cidade: ')).strip()
cidade2 = cidade.split()[0]

print('SANTO' in cidade.upper())