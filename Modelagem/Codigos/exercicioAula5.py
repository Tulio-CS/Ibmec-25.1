import numpy 
import scipy.optimize
import matplotlib.pyplot as plt


"""Valor exato = Log0.9 = 4/7
   Valor exato = 5.31143 
"""

f = lambda t: 7 * (2-0.9**t) -10

dominio = numpy.linspace(0, 10, 100)

raiz = scipy.optimize.bisect(f, 0, 10, full_output=True)
print(raiz)
plt.plot(dominio, f(dominio))
plt.plot(raiz[0], 0, 'ro')
plt.show()