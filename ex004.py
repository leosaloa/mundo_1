entrada = input('Digite algo: ')
print('\nO tipo primitivo desse valor é {}'.format(type(entrada)))
print('Só tem espaços?', entrada.isspace())
print('É um numero?', entrada.isalnum())
print('É alfabetico?', entrada.isalpha())
print('É alfanumerico?', entrada.isalnum())
print('Esta em maiusculas?', entrada.isupper())
print('Esta em minusulas?', entrada.islower())
print('Esta capitalizada?', entrada.istitle())