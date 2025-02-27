

#---Centrada---#
def diferencaCentradaPrimeiraOrdem(func,delta:float=1e-6):
    return lambda x: (func(x + delta) - func(x - delta))/(2*delta)

def diferencaCentradaSegundaOrdem(func,delta:float=1e-6):
    return lambda x: (func(x + delta) - 2*func(x) + func(x - delta))/(delta**2)

def diferencaCentradaTerceiraOrdem(func,delta:float=1e-6):
    return lambda x: (func(x + 2*delta) - 2*func(x + delta) + 2*func(x - delta) - func(x - 2*delta))/(2*delta**3)

def diferencaCentradaQuartaOrdem(func,delta:float=1e-6):
    return lambda x: (func(x + 2*delta) - 4*func(x + delta) + 6*func(x) - 4*func(x - delta) + func(x - 2*delta))/(delta**4)


#---Progressiva---#
def diferencaProgressivaPrimeiraOrdem(func,delta:float=1e-6):
    return lambda x: (func(x + delta) - func(x))/(delta)

def diferencaProgressivaSegundaOrdem(func,delta:float=1e-6):
    return lambda x: (func(x + 2*delta) - 2*func(x+delta) + func(x))/(delta**2)

def diferencaProgressivaTerceiraOrdem(func,delta:float=1e-6):
    return lambda x: (func(x + 3*delta) - 3*func(x + 2*delta) + 3*func(x + delta) - func(x))/(2*delta**3)

def diferencaProgressivaQuartaOrdem(func,delta:float=1e-6):
    return lambda x: (func(x + 4*delta) - 4*func(x + 3*delta) + 6*func(x+2*delta) - 4*func(x + delta) + func(x))/(delta**4)


#---Regressiva---#
def diferencaRegressivaPrimeiraOrdem(func,delta:float=1e-6):
    return lambda x: (func(x) - func(x - delta))/(delta)

def diferencaRegressivaSegundaOrdem(func,delta:float=1e-6):
    return lambda x: (func(x) - 2*func(x - delta) + func(x - 2*delta))/(delta**2)

def diferencaRegressivaTerceiraOrdem(func,delta:float=1e-6):
    return lambda x: (2*func(x) - 3*func(x - delta) + 3*func(x - 2*delta) - func(x - 3*delta))/(2*delta**3)

def diferencaRegressivaQuartaOrdem(func,delta:float=1e-6):
    return lambda x: (func(x) - 4*func(x - delta) + 6*func(x - 2*delta) - 4*func(x - 3*delta) + func(x -4*delta))/(delta**4)



