# Faça um programa em Python que abra e reproduza o audio de um arquivo mp3.

import pygame

pygame.init()
pygame.mixer.music.load('mc_paulin_da_capital-aoa.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()