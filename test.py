import matplotlib.pyplot as plt 
import numpy 

#%%
x = numpy.linspace(0,2 * numpy.pi, 1000)
y = numpy.sin(x)
plt.plot(x, numpy.sin(x))
plt.show()

