import pygame
import sys
import numpy as np
from astropy.io import fits

COLOR = (255, 100, 98)
size = 10
SURFACE_COLOR = (167, 255, 100)
ScreenWideness = 500
ScreenHighness = 500
ShootAngle = 0
FRICTION = 10
power = 0
setup = True
data =


class Ball(pygame.sprite.Sprite):
    def __init__(self, color, highness, wideness, upness):
        super().__init__()
        self.wideness = wideness
        self.highness = highness
        self.image = pygame.Surface([wideness, highness])
        self.image.fill(SURFACE_COLOR)
        self.image.set_colorkey(COLOR)

        pygame.draw.circle(self.image, color, (0, 0, wideness*(upness//10), highness*(upness//10))

        self.rect = self.image.get_rect()

    def move(self, (x, y), vel):
        self.rect.x += x*vel
        self.rect.y += y*vel

    def elevate(self, upness):
        self.upness = upness
        self.image = pygame.Surface([wideness*(1 + upness/100), highness*(1 + upness/10)])

class Field:
    def __init__(self, wideness, highness, data):
        ysz, xsz = np.shape(data)
        for j in data:
            for i in j:
                pass


myball = Ball(COLOR, size, size, 0)

while True:
    for event in pygame.event.get()
        if event.type == pygame.QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        setup = False

    if setup:
        if keys[pygame.K_UP]:
            power += 1
        if keys[pygame.K_DOWN]:
            power -= 1
        if keys[pygame.K_RIGHT]:
            ShootAngle -= 1
        if keys[pygame.K_LEFT]:
            ShootAngle += 1
    else:

pygame.init()
screen = pygame.display.set_mode((ScreenWideness, ScreenHighness))
klok = pygame.time.Clock()
pygame.display.set_caption("Galactic Golf DX")
