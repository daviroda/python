import pygame

pygame.init()
pygame.mixer_music.load('jazz.mp3')
pygame.mixer_music.play(0, 1, 1)
pygame.event.wait(input())
pygame.mixer_music.set_volume(1)
