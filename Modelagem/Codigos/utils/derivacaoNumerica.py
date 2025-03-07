

#---Centrada---#
def PrimeiraDerivadaCentrada(func,delta:float=1e-6):
    return lambda x: (func(x + delta) - func(x - delta))/(2*delta)

def SegundaDerivadaCentrada(func,delta:float=1e-6):
    return lambda x: (func(x + delta) - 2*func(x) + func(x - delta))/(delta**2)

def TerceiraDerivadaCentrada(func,delta:float=1e-6):
    return lambda x: (func(x + 2*delta) - 2*func(x + delta) + 2*func(x - delta) - func(x - 2*delta))/(2*delta**3)

def QuartaDerivadaCentrada(func,delta:float=1e-6):
    return lambda x: (func(x + 2*delta) - 4*func(x + delta) + 6*func(x) - 4*func(x - delta) + func(x - 2*delta))/(delta**4)


#---Progressiva---#
def PrimeiraDerivadaProgressiva(func,delta:float=1e-6):
    return lambda x: (func(x + delta) - func(x))/(delta)

def SegundaDerivadaProgressiva(func,delta:float=1e-6):
    return lambda x: (func(x + 2*delta) - 2*func(x+delta) + func(x))/(delta**2)

def TerceiraDerivadaProgressiva(func,delta:float=1e-6):
    return lambda x: (func(x + 3*delta) - 3*func(x + 2*delta) + 3*func(x + delta) - func(x))/(2*delta**3)

def QuartaDerivadaProgressiva(func,delta:float=1e-6):
    return lambda x: (func(x + 4*delta) - 4*func(x + 3*delta) + 6*func(x+2*delta) - 4*func(x + delta) + func(x))/(delta**4)


#---Regressiva---#
def PrimeiraDerivadaRegressiva(func,delta:float=1e-6):
    return lambda x: (func(x) - func(x - delta))/(delta)

def SegundaDerivadaRegressiva(func,delta:float=1e-6):
    return lambda x: (func(x) - 2*func(x - delta) + func(x - 2*delta))/(delta**2)

def TerceiraDerivadaRegressiva(func,delta:float=1e-6):
    return lambda x: (2*func(x) - 3*func(x - delta) + 3*func(x - 2*delta) - func(x - 3*delta))/(2*delta**3)

def QuartaDerivadaRegressiva(func,delta:float=1e-6):
    return lambda x: (func(x) - 4*func(x - delta) + 6*func(x - 2*delta) - 4*func(x - 3*delta) + func(x -4*delta))/(delta**4)



