

def diferencaCentradaPrimeiraOrdem(func:lambda x: expression,delta:float=1e-6)-> lambda x: expression:
    return lambda x: (func(x + delta) - func(x - delta))/(2*delta)

def diferencaCentradaSegundaOrdem(func:lambda x: expression,delta:float=1e-6)-> lambda x: expression:
    return lambda x: (func(x + delta) - 2*func(x) + func(x - delta))/(delta**2)

def diferencaCentradaTerceiraOrdem(func:lambda x: expression,delta:float=1e-6)-> lambda x: expression:
    return lambda x: (func(x + 2*delta) - 2*func(x + delta) + 2*func(x - delta) - func(x - 2*delta))/(2*delta**3)

def diferencaCentradaQuartaOrdem(func:lambda x: expression,delta:float=1e-6)-> lambda x: expression:
    return lambda x: (func(x + 2*delta) - 4*func(x + delta) + 6*func(x) - 4*func(x - delta) + func(x - 2*delta))/(delta**4)


