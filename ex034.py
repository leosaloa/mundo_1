# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1200,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('\nDigite o valor do salário que irá receber aumento: '))
sup = (salario * 0.10) + salario
inf = (salario * 0.15) + salario

if salario > 1200.00:
    print(f'\nO novo salário é R$ {sup:.2f}')
else:
    print(f'\nO novo salário é R$ {inf:.2f}')