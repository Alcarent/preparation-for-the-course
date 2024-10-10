from ortools.init.python import init
from ortools.linear_solver import pywraplp


class Solver:
    solver = pywraplp.Solver.CreateSolver("GLOP")
    infinity = solver.infinity()