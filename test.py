import empymod
import numpy as np
import matplotlib.pyplot as plt

src = [0,0,950,0,0]
# x-directed dipole receiver-array: x, y, z, azimuth, dip
rec = [np.linspace(-1500,1500,200), np.ones(200)*0, 1000.1,0,0]

# data=np.loadtxt('./data.txt')
# data_recx=np.array(data[:,0])
# data_recy=np.array(data[:,1])

# rec = [data_recx, data_recy, 0, 0, 0]

# layer boundaries
depth = [0,1000,1400,1500]
# layer resistivities
res = [1e8,0.3, 1,100,1]
# Frequency
freq = 0.5
# Calculate electric field due to an electric source at 10 Hz. mrec=True,
# [msrc = mrec = False (default)]
EMfield = empymod.bipole(src, rec, depth, res, freq,strength=100,verb=0)
plt.plot(np.linspace(-1500,1500,200),abs(EMfield.real))
plt.plot(np.linspace(-1500,1500,200),abs(EMfield.imag))
print(EMfield)
plt.yscale('log')
plt.show()

# np.savetxt('real.txt',EMfield.real)
# np.savetxt('imag.txt',EMfield.imag)
# plt.plot(data_recx[0:37:1],abs(EMfield.real[0:37:1]))
# plt.plot(data_recx[0:37:1],abs(np.loadtxt('./zz.txt')))
# plt.yscale('log')
# plt.show()