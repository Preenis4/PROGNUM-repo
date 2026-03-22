from astropy.io import fits
import matplotlib.pyplot as plt
import pandas
import numpy as np

fit = fits.open('SDSS_DR17_galaxies.fits')
df = pandas.DataFrame(fit[1].data)
del df['ObjID']
df.info()
#dat = {}
means = []
stds = []
filtered = df[df >=0].dropna()
cols = df.columns
for i in cols:
    for j in cols:
        if (i != j) and not (f"{j}-{i}" in df.columns):
            df[f'{i}-{j}'] = df[i] -df[j]
            means.append(float(np.mean(df[f'{i}-{j}'])))
            stds.append(float(np.std(df[f'{i}-{j}'])))
            #dat.update({f'{i}-{j}' : [float(np.mean(df[f'{i}-{j}'])), float(np.std(df[f'{i}-{j}']))]})

fig, axes = plt.subplots(9, 9)
df.info()
for i in range(5, 14):
    for j in range(5, 14):
        ax = axes[i-5, j-5]
        if i==j:
            ax.hist(df.iloc[:, j-5], 20)
        elif j <= i:
            ax.scatter(df.iloc[:, j-5], df.iloc[:, i], s=0.1)
            ax.set_xlim(means[i-5] - 3*stds[i-5], means[i-5] + 3*stds[i-5])
            ax.set_ylim(means[i-5] - 3*stds[i-5], means[i-5] + 3*stds[i-5])
#fig.tight_layout()
plt.show()
