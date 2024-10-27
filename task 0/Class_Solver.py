from ortools.init.python import init
from ortools.linear_solver import pywraplp
import os

class Solver:
    solver = pywraplp.Solver.CreateSolver("GLOP")
    infinity = solver.infinity()
    uid = os.getuid()
    
    
    locals()[f'']