import pygame
import sys
import random

COLOR = (255, 100, 98)
SURFACE_COLOR = (255, 255, 255)
WIDENESS = 500
HIGHNESS = 500
vel = 10

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, highness, wideness):
        super().__init__()

        self.image = pygame.Surface([wideness, highness])
        self.image.fill(SURFACE_COLOR)
        self.image.set_colorkey(COLOR)


        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, wideness, highness))

        self.rect = self.image.get_rect()

    def moveRight(self, vel):
        self.rect.x += vel
    def moveLeft(self, vel):
        self.rect.x -= vel
    def moveUp(self, vel):
        self.rect.y -= vel*vel/10
    def moveDown(self, vel):
        self.rect.y += vel*vel/10

pygame.init()

RED = (255, 0, 0)
size = (WIDENESS, HIGHNESS)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Sprite Creation")

sprite_list = pygame.sprite.Group()

object_ = Sprite(RED, 20, 30)
object_.rect.x = 200
object_.rect.y = 300

sprite_list.add(object_)

running = True
klok = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        sprite_list.update()
        screen.fill(SURFACE_COLOR)
        sprite_list.draw(screen)
        pygame.display.flip()
        klok.tick(60)
