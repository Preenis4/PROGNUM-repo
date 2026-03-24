import pygame
import time
pygame.init()

screen = pygame.display.set_mode((600, 700), pygame.RESIZABLE)
color = 'yellow'

pygame.display.set_caption('Albanian Virus')

size = 50
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill('black')
    pygame.display.flip()
    xm, ym = pygame.mouse.get_pos()
    pygame.draw.rect(screen, color, pygame.Rect(xm-size,ym-size, 2*size, 2*size))
    pygame.display.flip()

