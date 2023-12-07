import empymod
import numpy as np
import matplotlib.pyplot as plt

src = [0,0,0.1,0,0]

rec = [np.ones(5)*0,  np.linspace(100,500,5), 0.1,0,0]

# layer boundaries
depth = [0]
# layer resistivities
res = [1e8,100]
# Frequency
freq = 100
# Calculate electric field due to an electric source at 10 Hz. mrec=True,
# [msrc = mrec = False (default)]
EMfield = empymod.bipole(src, rec, depth, res, freq,strength=1,verb=0)

print(EMfield)

