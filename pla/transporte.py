import numpy as np
from gurobipy import Model, GRB


custos = np.array([
    [464, 513, 654, 867],  
    [352, 416, 690, 791],  
    [995, 682, 388, 685]   
])

oferta = [75, 125, 100]       
demanda = [80, 65, 70, 85]    

n_fabricas = len(oferta)
n_depositos = len(demanda)

m = Model()

x = m.addVars(n_fabricas, n_depositos, vtype=GRB.CONTINUOUS, name="x")

m.setObjective(
    sum(custos[i][j] * x[i, j] for i in range(n_fabricas) for j in range(n_depositos)),
    GRB.MINIMIZE
)

for i in range(n_fabricas):
    m.addConstr(sum(x[i, j] for j in range(n_depositos)) == oferta[i])

for j in range(n_depositos):
    m.addConstr(sum(x[i, j] for i in range(n_fabricas)) == demanda[j])

m.optimize()


print(f"Custo mínimo total: ${m.objVal:.2f}\n")
matriz_resultado = np.zeros((n_fabricas, n_depositos), dtype=int)

for i in range(n_fabricas):
    total_i = 0
    for j in range(n_depositos):
        val = int(round(x[i, j].X))
        matriz_resultado[i, j] = val
        if val > 0:
            print(f"Enviar {val} carretas da Fábrica {i+1} para Depósito {j+1}")
            total_i += val

print(matriz_resultado)
