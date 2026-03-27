import pygame
import sys

pygame.font.init()

screen = pygame.display.set_mode([600, 500])
klok = pygame.time.Clock()

basefont = pygame.font.SysFont(None, 32)

mytext = ''

textrect = pygame.Rect(200, 200, 140, 32)
active_color = pygame.Color('lightskyblue3')
passive_color = pygame.Color('chartreuse4')
color = passive_color
active = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if textrect.collidepoint(event.pos):
                active = True
            else:
                active = False
        if event.type == pygame.KEYDOWN and active:
            if event.key == pygame.K_BACKSPACE:
                mytext = mytext[:-1]
            else:
                mytext += event.unicode

    screen.fill((255, 255, 255))

    if active:
        color = active_color
    else:
        color = passive_color

    pygame.draw.rect(screen, color, textrect)

    text_surface = basefont.render(mytext, True, (255, 255, 255))
    screen.blit(text_surface, (textrect.x + 5, textrect.y + 5))
    textrect.w = max(100, text_surface.get_width() + 10)

    pygame.display.flip()

    klok.tick(60)
