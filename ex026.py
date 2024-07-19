# Faça um programa que leia uma frase
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a ultima vez

frase = str(input('\nDigite uma frase: ')).upper().strip()

print('\nA letra "A" aparece', frase.count('A'), 'vezes')
print('\nA letra "A" aparece primeiro na posição', frase.find('A'))
print('\nA letra "A" aparece a ultima vez na posião', frase.rfind('A'))