import empymod
import numpy as np
import matplotlib.pyplot as plt

src = [0,0,950,0,0]
# x-directed dipole receiver-array: x, y, z, azimuth, dip
rec = [np.linspace(-1500,1500,200), np.ones(200)*0, 1000.1,0,90]

# layer boundaries
depth = [0,1000,1400,1500]
# layer resistivities
res = [1e8,0.3, 1,100,1]
# Frequency
freq = 0.5
# Calculate electric field due to an electric source at 10 Hz. mrec=True,
# [msrc = mrec = False (default)]
EMfield = empymod.bipole(src, rec, depth, res, freq,strength=100,verb=0)

res = [1e8,0.3, 1,1,1]
EMfield2 = empymod.bipole(src, rec, depth, res, freq,strength=100,verb=0)
plt.plot(np.linspace(-1500,1500,200),(EMfield.real-EMfield2.real))
plt.plot(np.linspace(-1500,1500,200),(EMfield.imag-EMfield2.imag))
print(EMfield)
# plt.yscale('log')
plt.show()
