#!/usr/bin/env python

from matplotlib import pyplot as plt
import matplotlib
import numpy as np

print(matplotlib.get_backend())
matplotlib.use('QtAgg')

print(matplotlib.get_backend())


x = np.arange(10)

plt.figure()
plt.plot(x,x**2)
plt.show()
