#Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e a raiz quadrada.
num = int(input('\nDigite um numero: '))
dobro = num*2
triplo = num*3
raiz = num**0.5

print('Dobro do numero digitado {}.\nTriplo do numero digitado {}.\nRaiz quadrada do numero digitado {:.2f}.\n'.format(dobro, triplo, raiz))