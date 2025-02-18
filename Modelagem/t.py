import gurobipy as gp

# Create a new model
m = gp.Model()

# Create variables
x = m.addVar(vtype='I', name="m1")
y = m.addVar(vtype='I', name="m2")

# Set objective function
m.setObjective(90*x + 120*y, gp.GRB.MINIMIZE)

# Add constraints
m.addConstr(0.2*x + 0.3*y >= 8000)
m.addConstr(0.2*x + 0.25*y >= 6000)
m.addConstr(0.15*x + 0.1*y >= 5000)
# Solve it!
m.optimize()



print(f"Optimal objective value: {m.objVal}")
print(f"Solution values: m1={x.X}, m2={y.X}")

