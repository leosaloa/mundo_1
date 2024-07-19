# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

# Condição 1: Ser múltiplo de 4 e não ser múltiplo de 100
# Condição 2: Ser múltiplo de 400 (se for múltiplo de 400 automaticamente é de 4)

from datetime import date
data_atual = date.today().year

ano = int(input('\nQual ano quer analisar? Digite 0 para o ano atual: '))

divisivel_por_4 = ano % 4 == 0
divisivel_por_100 = ano % 100 == 0
divisivel_por_400 = ano % 400 == 0

if ano == 0:
    ano = data_atual
if (divisivel_por_4 and not divisivel_por_100) or divisivel_por_400:
    print('O ano é BISSEXTO')
else:
    print('O ano não é BISSEXTO')
