# Desenvolva um programa que pergunte a distância de uma viagem em KM.
# Calcule o preço da passagem, cobrando R$ 0,50 por KM para viagens de até 200km e R$ 0,45 para viagens mais longas.


distancia = float(input('\nDigite a distncia da viagem: '))
longa = distancia * 0.45
curta = distancia * 0.50


if distancia > 200:
    print(f'Viagem Longa\nO valor da viagem é R$ {longa:.2f}')
else: 
    print(f'Viagem Curta\nO valor da viagem é R$ {curta:.2f}')