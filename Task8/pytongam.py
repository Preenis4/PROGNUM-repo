import pygame
import sys

pygame.init()

win = pygame.display.set_mode((500, 500))

x = 200
y = 200

wideness = 20
highness = 20

vel = 2
run = True

while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LSHIFT]:
        vel = 10
    else:
        vel = 2
    if keys[pygame.K_LEFT] and x>0:
        x -= vel
    if keys[pygame.K_RIGHT] and x<500 - wideness:
        x += vel
    if keys[pygame.K_UP] and y>0:
        y -= vel
    if keys[pygame.K_DOWN] and y<500- highness:
        y += vel

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, wideness, highness))
    pygame.display.update()









