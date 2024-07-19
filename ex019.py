# Um professor que sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice

a = str(input('\nDigite o nome do primeiro aluno: '))
b = str(input('\nDigite o nome do segundo aluno: '))
c = str(input('\nDigite o nome do terceiro aluno: '))
d = str(input('\nDigite o nome do quarto aluno: '))
e = str(input('\nDigite o nome do quarto aluno: '))


sorteio = choice([a, b, c, d, e])

print(f'Aluno sorteado: \n>>> {sorteio.upper()} <<<')