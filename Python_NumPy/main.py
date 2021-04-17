import numpy
import matplotlib.pyplot as plt
arr = numpy.array([1,2,3,4,5])

print('arr:',arr)

print ('numpy:', numpy.__version__)

xpoints = numpy.array([0, 6])
ypoints = numpy.array([0, -250])

plt.plot(xpoints, ypoints)
plt.show()
