
def bissecao(f, a, b, tol=1e-6, max_iter=100):    
    if f(a) * f(b) > 0:
        raise ValueError("A funcao deve ter sinais opostos em a e b.")
    
    for _ in range(max_iter):
        c = (a + b) / 2
        if abs(f(c)) < tol or (b - a) / 2 < tol:
            return c 
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    
    return None 



if __name__ == "__main__":
    funcao = lambda x: x**3
    raiz = bissecao(funcao, -2, 3,tol=1e-10)
    print(f"Raiz encontrada: {raiz}")
