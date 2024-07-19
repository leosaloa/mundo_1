# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
# Exemplo: Ana Maria de Souza
# Primeiro = Ana            ultimo = Souza

name = str(input('\nDigite o nome completo: '))
primeiro = name.split()
ultimo = name.rsplit()

print('\nPrimeiro nome: ', primeiro[0])
print('\nUltimo nome: ', ultimo[-1])