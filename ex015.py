# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a 
# quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias_aluguel = int(input('Quantidade de dias alugados: '))

km_rodado = float(input('Quantidade de km rodado: '))

vl_total = (dias_aluguel * 60) + (km_rodado * 0.15)

print('O valor total é R$ {:.2f}'.format(vl_total))