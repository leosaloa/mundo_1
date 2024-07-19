# Crie um progrma que leia o nome completo de uma pessoa e mostre:
# O nome com todas letras maiúsculas
# O nome com todas letras minúsculas
# Quantas letras sem considerar os espaços
# Quantas letras tem o primeiro nome

nome = str(input('\nDigite seu nome completo: ')).strip()
d = nome.split()

print('\nNome maiúsculo: ', nome.upper())
print('\nNome minúsculo: ', nome.lower())
print('\nQuantidade de letras sem considerar os espaços: ', len(nome.replace(' ', '')))
print('\nQuantidade de letras no primeiro nome: ', len(d[0]))