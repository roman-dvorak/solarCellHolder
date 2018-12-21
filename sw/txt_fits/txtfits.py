import pandas as pd
import numpy as np
from astropy.io import fits

data = pd.read_csv('/home/roman/repos/solarCellHolder/sw/txt_fits/zoom 2 clanek EL I.txt', header = None, sep="\t")


x = sorted(list(set(data[0])))
y = sorted(list(set(data[1])))

res_x = abs(x[1]-x[2])
res_y = abs(y[1]-y[2])
px_x = len(x)
px_y = len(y)
start_x = x[0]
start_y = y[0]

n = np.ndarray((px_x, px_y))
n[0][0] = 10

for d in data.T:
	print(d)
	px, py, pv = data.T[d]
	ix = (px-start_x)/res_x
	iy = (py-start_y)/res_y
	print("ukladam do:", ix, iy)
	n[int(ix), int(iy)] = pv

hdu = fits.PrimaryHDU(n)
hdu.header['CUNIT1'] = 'mm'
hdu.header['CRVAL1'] = start_x
hdu.header['CDELT1'] = res_x

hdu.header['CUNIT2'] = 'mm'
hdu.header['CRVAL2'] = start_y
hdu.header['CDELT2'] = res_y

hdu.writeto('new3.fits')
