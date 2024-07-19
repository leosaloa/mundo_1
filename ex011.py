# Faça um programa que leia a altura e largura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria
# para pinta-la, sabendo que cada litro de tinta pinta uma area de 2m².
largura = float(input('\nDigite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

area = altura*largura
tinta = area/2

print('Area {:.1f} m²\nLitros de tinta necessario para pintar a parede {:.1f}l\n'.format(area, tinta))