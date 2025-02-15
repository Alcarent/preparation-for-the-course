from ortools.linear_solver import pywraplp
import numpy as np
solver = pywraplp.Solver.CreateSolver("GLOP")

class Probem:
    solver = pywraplp.Solver.CreateSolver("GLOP")
    c = []
    vars = []
    a = []
    b = []
    a_eq = []
    b_eq = []
    status = ""
    x = []
    def add_c(self, c):
        self.c = c.copy()

    def add_x(self, vars):
        self.vars = vars.copy()
        
    def add_a_b_aeq_beq(self, a, b, a_eq, b_eq):
        self.a = a.copy()
        self.b = b.copy()
        self.a_eq = a_eq.copy()
        self.b_eq = b_eq.copy()
        
        
    def solve(self):
        n = len(self.c)
        x_string = ['x'+str(i) for i in range(1, n+1)]
        self.x = [solver.NumVar(self.vars[0][i], self.vars[1][i], x_string[i]) for i in range(n)]
#self.solver.infinity()
        for r in range(len(self.b_eq)):
          solver.Add(sum(self.a_eq[r][u] * self.x[u] for u in range(n)) == self.b_eq[r])

        for r in range(len(self.b)):
          solver.Add(sum(self.a[r][u] * self.x[u] for u in range(n)) <= self.b[r])

        solver.Maximize(sum(self.c[i] * self.x[i] for i in range(n)))
        result_status = self.solver.Solve()
        print(result_status)
        print("Objective value =", self.solver.Objective().Value())
        
        
        
        
        
x = np.array([[0.0, 0.0],
              [10.0, 10.0]])

"""np.array([[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0]])"""

c = np.array([2.0, 1.0])

"""np.array([3.0, 20.0, -2.0, 6.0, 13.0, 12.0, 32.0, 7.0, 21.0, 2.0, 0.0, 7.0])
"""
a = np.array([[1.0, 1.0]])

"""np.array([[1.0, 3.0, 8.0, 6.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 2.0, 5.0, 13.0, 1.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 6.0, -2.0, 2.0, 9.0]])"""
        
b = np.array([90.0])

"""np.array([290.0,430.0,511.0] )"""

a_eq = np.array([[6.0, 1.0]])

"""np.array([[1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
         [0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0]])
       #  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0]]"""
b_eq = np.array([70.0])
"""np.array([191.0, 250.0])#, 601.0]"""


Problema = Probem()
Problema.add_c(c)
Problema.add_a_b_aeq_beq(a, b, a_eq, b_eq)
Problema.add_x(x)
Problema.solve()