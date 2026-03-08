from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

hdul = fits.open('APOGEE_stars.fits')
data = hdul[1].data
colnames = hdul[1].columns.names

mask_ASFLAG = data['ASPCAPFLAG'] == 0
mask_STARFLAG = data['STARFLAG'] == 0
mask_SNR = data['SNR'] > 10
mask_GAIA_PAR = (data['GAIAEDR3_PARALLAX'])/(data['GAIAEDR3_PARALLAX_ERROR']) > 5
mask_GAIA_G = ~np.isnan(data['GAIAEDR3_PHOT_G_MEAN_MAG'])
mask_GAIA_BP = ~np.isnan(data['GAIAEDR3_PHOT_BP_MEAN_MAG'])
mask_GAIA_RP = ~np.isnan(data['GAIAEDR3_PHOT_RP_MEAN_MAG'])
combined_mask = mask_ASFLAG & mask_STARFLAG & mask_SNR & mask_GAIA_PAR & mask_GAIA_G & mask_GAIA_BP & mask_GAIA_RP
selected_data = data[combined_mask]

n_rows = len(selected_data)
n_select = int(0.8*n_rows)
random_indices = np.random.choice(n_rows, size=n_select, replace=False)
random_80 = selected_data[random_indices]

m_apparent = random_80['GAIAEDR3_PHOT_G_MEAN_MAG']
parralax = random_80['GAIAEDR3_PARALLAX']
temp = random_80['GAIAEDR3_PHOT_BP_MEAN_MAG'] - random_80['GAIAEDR3_PHOT_RP_MEAN_MAG']
m_abs = m_apparent + 5*np.log10(parralax/1000) + 5

is_giant = (m_abs < 3.5) & (temp > 0.8)
is_dwarf = (temp <= 0.8) & (m_abs > 10)
is_ms = ~is_giant & ~is_dwarf

plt.scatter(temp[is_giant], m_abs[is_giant], label='Giants', color='r',linewidths=0.1, s=0.2)
rect = patches.Rectangle((0.8, 10), -2.2, 6.5, linewidth=1, edgecolor='k',facecolor='gray', alpha=0.3, label='White Dwarf region')
plt.gca().add_patch(rect)
plt.scatter(temp[is_ms], m_abs[is_ms], label='Mains',color='b', s=0.2)
plt.ylabel('Absolute Magnitude')
plt.xlabel('BP - RP')
plt.title('HR Diagram')
plt.annotate('WD', (-0.5, 13))
plt.annotate('Giant Branch', xytext=(-1.5, -3), xy=(0.8,-2.5), c='r', arrowprops=dict(arrowstyle="->"))
plt.annotate('MS',xytext=(-1, 4), xy=(0.5, 4), c='b',arrowprops=dict(arrowstyle="->"))
plt.gca().invert_yaxis()
plt.legend()
plt.show()
