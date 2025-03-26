from matplotlib.pyplot import plot, legend, grid, show 
from scipy.optimize import bisect,newton
from numpy import linspace, gradient

def f(x):
    return x**3 -9*x - 5

def df(x):
    return 3*x**2 - 9

x = linspace(-5, 0, 100)


def metodoNewton(f,df,x):
    erro = 0.00001
    x_proximo = x
    while True:
        x_atual = x_proximo
        x_proximo = x_atual - f(x_atual)/df(x_atual)
        if abs(f(x_proximo)) < erro:
            return x_proximo
        else:
            print(f'f = {f(x_proximo)}\ndf = {df(x_proximo)}\nproximo ponto = {x_proximo}\n\n')


raiz = metodoNewton(f,df,-2)

print(f(raiz))




