import numpy
import matplotlib.pyplot as plt

def f(x):
    return x**3-9*x-5

x = numpy.linspace(-2, 0, 50)

xl = -2
xu = 0

def regulaFalsi(f,xl,xu):
    if f(xl) * f(xu) > 0:
        raise ValueError("A funcao deve ter sinais opostos em xl e xu.")
    
    erro = 0.001
    fxl = f(xl)
    fxu = f(xu)
    while True:
        xr = xu - fxu*(xl - xu)/(fxl - fxu)
        fxr = f(xr)
        if abs(fxr) < erro:
            return xr
        if fxl * fxr < 0:
            xu = xr
            fxu = fxr
        else:
            xl = xr
            fxl = fxr


plt.plot(x, f(x))
raiz = regulaFalsi(f, xl, xu)
print(raiz)
plt.plot(raiz,f(raiz),"ro")
plt.show()