# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

produto = float(input('\nDigite o valor do produto que recebera desconto: '))

desconto = 0.05
novo_valor = produto-(produto*0.05)

print('O valor do produto com 5% de desconto é R$ {:.2f}'.format(novo_valor))