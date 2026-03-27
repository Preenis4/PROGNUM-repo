import pygame
import numpy as np

COLOR = (255, 100, 98)
SURFACE_COLOR = (167, 255, 100)
ScreenWideness = 500
ScreenHighness = 500
ShootAngle = 0
FRICTION = 10


class Ball(pygame.sprite.Sprite):
    def __init__(self, color, highness, wideness, upness):
        super().__init__()
        self.image = pygame.Surface([wideness*upness//10, highness*upness//10])
        self.image.fill(SURFACE_COLOR)
        self.image.set_colorkey(COLOR)

        pygame.draw.circle(self.image, color, (0, 0, wideness*(upness//10), highness*(upness//10))

        self.rect = self.image.get_rect()

    def MoveRight(self, vel):
        self.rect.x += vel

    def MoveLeft(self, vel):
        self.rect.x -= vel

    def MoveUp(self, vel):
        self.rect.y -= vel

    def MoveDown(self, vel):
        self.rect.y += vel

def vector_move(sprite, (x, y), vel):
    t

pygame.init()
screen = pygame.display.set_mode((ScreenWideness, ScreenHighness))
klok = pygame.time.Clock()

pygame.display.set_caption("Galactic Golf DX")
