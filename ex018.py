# Faça um programa que leia um angulo qualquer e mostre na tela o valor seno, cosseno e tangente desse angulo.
from  math import radians, sin, cos, tan

# Lendo o ângulo em graus
angulo = float(input("Digite o ângulo em graus: "))

# Convertendo o ângulo para radianos
radiano = radians(angulo)

# Calculando o seno, cosseno e tangente
seno = sin(radiano)
cosseno = cos(radiano)
tangente = tan(radiano)

# Mostrando os resultados
print(f"Seno: {seno:.2f}")
print(f"Cosseno: {cosseno:.2f}")
print(f"Tangente: {tangente:.2f}")
