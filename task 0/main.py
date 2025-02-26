from ortools.init.python import init
from ortools.linear_solver import pywraplp
from Class_Problem import *
import numpy as np

""" для проверки
x = np.array([[0.0, 0.0, 0.0, 0.0],
        [10.0, 10.0, 10.0, 12.0]])
c = np.array([29.0, 45.0, 0.0, 0.0])
num_vars = len(c)
a = np.array([ 
    [1.0, -1.0, -3.0, 0.0],
    [-2.0, 3.0, 7.0, -3.0],
    [1.0,  0.0, 0.0,  0.0],
    [-1.0, 0.0, 0.0,  0.0],
    [0.0,  0.0, -1.0, 0.0]
    ])
b = np.array([5.0, -10.0, 6, 0, 3])
a_eq = np.array([
    [2.0, 8.0, 1.0, 0.0],
    [4.0, 4.0, 0.0, 1.0]
    ])
b_eq = np.array([60.0, 60.0])
"""

#""" из прошлого задания
x = np.array([[0.0, -np.inf, -3.0, -np.inf],
        [6.0, np.inf, np.inf, np.inf]])
c = np.array([29.0, 45.0, 0.0, 0.0])
num_vars = len(c)
a = np.array([ 
    [1.0, -1.0, -3.0, 0.0],
    [-2.0, 3.0, 7.0, -3.0]])
b = np.array([5.0, -10.0])
a_eq = np.array([
    [2.0, 8.0, 1.0, 0.0],
    [4.0, 4.0, 0.0, 1.0]
    ])
b_eq = np.array([60.0, 60.0])
#"""



director = Director()
builder = ConcreteBuilder()
director.builder = builder


director.build(num_vars, x[0], x[1], a, b, a_eq, b_eq, c)
problem = builder.product
problem.solve()
