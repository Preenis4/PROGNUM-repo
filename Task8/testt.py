import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Ball Test")

class Ball(pygame.sprite.Sprite):
    def __init__(self, color, highness, wideness):
        super().__init__()
        self.wideness = wideness
        self.highness = highness
        self.image = pygame.Surface([wideness, highness], pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (wideness//2, highness//2), wideness//2)
        self.rect = self.image.get_rect()

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

sprite_list = pygame.sprite.Group()
myball = Ball((0, 0, 255), 20, 20)
myball.rect.x = 100
myball.rect.y = 100
sprite_list.add(myball)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        myball.move(5, 0)
    if keys[pygame.K_LEFT]:
        myball.move(-5, 0)
    if keys[pygame.K_UP]:
        myball.move(0, -5)
    if keys[pygame.K_DOWN]:
        myball.move(0, 5)

    screen.fill((0, 0, 0))
    sprite_list.update()
    sprite_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)
