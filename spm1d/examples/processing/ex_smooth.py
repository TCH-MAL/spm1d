
import numpy as np
from matplotlib import pyplot
import spm1d

# create random data:
np.random.seed(0)
Y0           = np.random.randn(5,101)

# smooth:
Y           = spm1d.util.smooth(Y0, fwhm=5.0)

# plot:
pyplot.close('all')
pyplot.figure(figsize=(8,3.5))
ax0          = pyplot.axes((0.1,0.15,0.35,0.8))
ax1          = pyplot.axes((0.55,0.15,0.35,0.8))
ax0.plot(Y0.T, 'k')
ax1.plot(Y.T, 'k')
ax0.text(0.5, 0.9, 'Before smoothing', size=14, transform=ax0.transAxes, ha='center')
ax1.text(0.5, 0.9, 'After smoothing', size=14, transform=ax1.transAxes, ha='center')
pyplot.show()

