#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua media.
nota1 = float(input('\nDigite a primeira nota: '))
nota2 = float(input('Digite a segunda nota:'))
media = (nota1+nota2)/2

print('Primeira nota {:.1f}\nSegunda nota {:.1f}\nMedia {:.1f}'.format(nota1, nota2, media))