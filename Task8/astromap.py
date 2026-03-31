import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits
import pygame
import sys


pygame.init()

scrn = pygame.display.set_mode((1000, 1000))
imp = pygame.image.load("compmap.png")
imp = imp.convert()
scrn.blit(imp, (0, 0))

def makemap(ogloc):
    data = fits.open(ogloc)[0].data
    fig, ax = plt.subplots()
    fig = plt.figure(frameon=False)
    fig.set_size_inches(50, 50)
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)

    if len(np.shape(data)) > 2:
        data = np.mean(data, axis = 0)

    plt.imshow(data, cmap = 'Grays_r')
    fig.savefig('compmap.png')

makemap('map.fits')

pygame.display.flip()
status = True
while (status):
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
