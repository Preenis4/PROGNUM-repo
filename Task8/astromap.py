import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits



def makemap(w, h):
    data = fits.open('map.fits')[0].data
    fig, ax = plt.subplots()
    fig = plt.figure(frameon=False)
    fig.set_size_inches(w,h)
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)

    if len(np.shape(data)) > 2:
        data = np.mean(data, axis = 0)

    plt.imshow(data, cmap = 'Grays_r')
    fig.savefig('compmap.png')

makemap(40, 40)
