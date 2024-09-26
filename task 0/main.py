from ortools.init.python import init
from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver("GLOP")
infinity = solver.infinity()

x1_var = solver.NumVar(0, 6, "x1")
x2_var = solver.NumVar(-infinity, infinity, "x2")
x3_var = solver.NumVar(-3, infinity, "x3")
x4_var = solver.NumVar(-infinity, infinity, "x4")


constraint1 = solver.Constraint(-infinity, 5, "ct")
constraint1.SetCoefficient(x1_var, 1)
constraint1.SetCoefficient(x2_var, -1)
constraint1.SetCoefficient(x3_var, -3)


constraint2 = solver.Constraint(10, infinity, "ct")
constraint2.SetCoefficient(x1_var, 2)
constraint2.SetCoefficient(x2_var, -3)
constraint2.SetCoefficient(x3_var, -7)
constraint2.SetCoefficient(x4_var, 3)

constraint3 = solver.Constraint(60, 60, "ct")
constraint3.SetCoefficient(x1_var, 2)
constraint3.SetCoefficient(x2_var, 8)
constraint3.SetCoefficient(x3_var, 1)


constraint4 = solver.Constraint(60, 60, "ct")
constraint4.SetCoefficient(x1_var, 4)
constraint4.SetCoefficient(x2_var, 4)
constraint4.SetCoefficient(x4_var, 1)

objective = solver.Objective()
objective.SetCoefficient(x1_var, 29)
objective.SetCoefficient(x2_var, 45)
objective.SetMaximization()

result_status = solver.Solve()

print("Solution:")
print("Objective value =", objective.Value())
print("x1 =", x1_var.solution_value())
print("x2 =", x2_var.solution_value())


