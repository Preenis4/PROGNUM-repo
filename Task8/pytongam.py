import pygame

pygame.init()

screen = pygame.display.set_mode((400, 500))

count = 1
running = True
fps = 0
ticks = 0

klok = pygame.time.Clock()

while running:
    deltaT =
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(f'Framerate was {fps} FPS')
            pygame.quit()
    ticks = pygame.time.get_ticks()
    print(count*1000/ticks)

    count += 1
    pygame.time.wait(14)

