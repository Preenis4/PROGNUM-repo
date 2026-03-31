import pygame
import pygame.gfxdraw
import sys
import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt


TILE_COLOR = (255, 100, 98)
size = 10
SURFACE_COLOR = (167, 255, 100)
BALL_COLOR = (0, 0, 255)
ScreenWideness = 1000
ScreenHighness = 1000
ShootAngle = 0
FRICTION = 1
power = 0
setup = True

pygame.init()
screen = pygame.display.set_mode((ScreenWideness, ScreenHighness))
imp = pygame.image.load("imgoutput.png")
print('img loaded')
print("Original image size:", imp.get_width(), imp.get_height())
image = pygame.transform.scale(imp, (ScreenWideness, ScreenHighness))


class Ball(pygame.sprite.Sprite):
    def __init__(self, color, highness, wideness):
        super().__init__()
        self.wideness = wideness
        self.highness = highness
        self.image = pygame.Surface([wideness, highness], pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (wideness//2, highness//2), wideness//2)
        self.rect = self.image.get_rect()

    def move(self, dx, dy, basevel):
        self.rect.x += dx*basevel
        self.rect.y += dy*basevel

data = fits.open('map.fits')[0].data
data = np.mean(data, axis = 0)
ys, xs = np.shape(data)
uf = 1/np.max(data)
sprite_list = pygame.sprite.Group()

myball = Ball(BALL_COLOR, size, size)
myball.rect.x = 200
myball.rect.y = 300
sprite_list.add(myball)

klok = pygame.time.Clock()
pygame.display.set_caption("Galactic Golf DX")

screen.blit(image, (0, 0))
pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()

    screen.blit(image, (0, 0))

    if (myball.rect.x > 990) or (myball.rect.x < 10) or (myball.rect.y > 990) or (myball.rect.y < 10):
        print('Out of bounds!')
        sys.exit()

    if abs(myball.rect.x - ScreenWideness/2) < 10:
        print('You\'re winner')
        sys.exit()
    if setup:
        if keys[pygame.K_SPACE]:
            setup = False
        if keys[pygame.K_UP]:
            power += 3
        if keys[pygame.K_DOWN]:
            power -= 3
        if keys[pygame.K_RIGHT]:
            ShootAngle += 0.1
        if keys[pygame.K_LEFT]:
            ShootAngle -= 0.1
        xloc = myball.rect.x + power*np.cos(ShootAngle)
        yloc = myball.rect.y + power*np.sin(ShootAngle)
        pygame.gfxdraw.line(screen, int(myball.rect.x), int(myball.rect.y), int(xloc), int(yloc), (255, 0, 0))
        basevel = power/20
    else:
        if basevel > 0:
            myball.move(np.cos(ShootAngle), np.sin(ShootAngle), basevel)
            data_y = int((myball.rect.y/ScreenHighness)*ys)
            data_x = int((myball.rect.x/ScreenWideness)*xs)
            print(basevel)
            basevel = basevel - FRICTION*(data[data_y, data_x]/np.nanmax(data))
            print(FRICTION*(data[data_y, data_x]/np.max(data)))
        elif basevel < 0:
            print('DONE')
            basevel = 0
            setup = True
        else:
            setup = True
    sprite_list.update()
    sprite_list.draw(screen)
    pygame.display.update()
    klok.tick(60)
    #print(basevel)
