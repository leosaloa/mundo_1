# Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento.
salario_atual = float(input('\nDigite o salario atual do funcionario: R$ '))

porc = 0.15 # 15%
salario_novo = salario_atual+(salario_atual*porc)

print('O novo salario do funcionario com 15% de aumento é R$ {:.2f}'.format(salario_novo))