# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ele pode comprar
# Considere US$ 1,00 = R$ 3,27
real = float(input('\nDigite o valor que possui em R$ '))
dolar = real/3.27

print('Com R$ {:.2f} você pode comprar US$ {:.2f}'.format(real, dolar))