#!/usr/bin/env python
""" wrote this b/c backend wasn't working.  install pyqt5 and now all is ok"""


from matplotlib import pyplot as plt
import matplotlib
import numpy as np

print(matplotlib.get_backend())
#matplotlib.use('QtAgg')
#print(matplotlib.get_backend())


x = np.arange(10)
# make a test figure to make sure the backend is working
plt.figure()
plt.plot(x, x**2)
plt.show()
