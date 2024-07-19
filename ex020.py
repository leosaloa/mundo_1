# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

a = str(input('\nDigite o nome do primeiro aluno: '))
b = str(input('\nDigite o nome do segundo aluno: '))
c = str(input('\nDigite o nome do terceiro aluno: '))
d = str(input('\nDigite o nome do quarto aluno: '))

ordem = [a, b, c, d]
shuffle(ordem)

print('\nA ordem de apresentação é ')
for aluno in ordem:
    print(aluno.upper())
