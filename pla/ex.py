import gurobipy as gp

model = gp.Model()

x = model.addVar(vtype="I",name="x")
y = model.addVar(vtype="I",name="y")

model.setObjective(3000*x + 5000*y, gp.GRB.MAXIMIZE)

model.addConstr(x <= 4)
model.addConstr(2*y <= 12)
model.addConstr(3*x + 2*y <= 18)

model.optimize()

print(f"Optimal solution {x.x} {y.x}")