import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

f = lambda x: (-4 + 1.8*x**2 + 1.2*x**3 - 0.3*x**4)
fneg = lambda x: -(-4 + 1.8*x**2 + 1.2*x**3 - 0.3*x**4)

x = np.linspace(-2, 5, 100)
plt.plot(x, f(x))
plt.grid()
maximo = minimize(fneg,1)
print(maximo)
plt.plot(maximo.x,f(maximo.x),'ro')
plt.show()