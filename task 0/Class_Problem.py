from ortools.init.python import init
from ortools.linear_solver import pywraplp
from abc import ABC, abstractmethod
import numpy as np
class Class_Problem:
    # создаём солвер
    def __init__(self):
        self.solver = pywraplp.Solver.CreateSolver('GLOP')
        self.variables = {}


    # закидываем переменные в солвер, дублируя их в список для вывода если нужен будет
    def add_variables(self, num_vars, lower_bounds, upper_bounds):
        for i in range(num_vars):
            var_name = f'x{i + 1}'
            self.variables[var_name] = self.solver.NumVar(lower_bounds[i], upper_bounds[i], var_name)


    # хранить ограничения будет сложнее, если надо будет сделаю потом
    def add_constraints(self, a, b, a_eq, b_eq):
        # добавляем ограничения <=
        for i in range(a.shape[0]):
            ct = self.solver.Constraint(-self.solver.infinity(), b[i])
            for j in range(a.shape[1]):
                var_name = f'x{j + 1}'
                ct.SetCoefficient(self.variables[var_name], a[i, j])
        # добавляем  ограничения ==
        for i in range(a_eq.shape[0]):
            ct = self.solver.Constraint(b_eq[i], b_eq[i])
            for j in range(a_eq.shape[1]):
                var_name = f'x{j + 1}'
                ct.SetCoefficient(self.variables[var_name], a_eq[i, j])
                
    # максимизируем
    def set_objective(self, c):
        objective = self.solver.Objective()
        for j in range(len(c)):
            var_name = f'x{j + 1}'
            objective.SetCoefficient(self.variables[var_name], c[j])
        objective.SetMaximization()
    
    # запускаем решатель
    def solve(self):
        status = self.solver.Solve()
        if status == pywraplp.Solver.OPTIMAL:
            print('Objective value =', self.solver.Objective().Value())
            for var_name, var in self.variables.items():
                print(f'{var_name} =', var.solution_value())
        else:
            print('The problem does not have an optimal solution.')




class Builder(ABC):
    @property
    @abstractmethod
    def product(self) -> Class_Problem:
        pass

    @abstractmethod
    def add_variables(self, num_vars, lower_bounds, upper_bounds) -> None:
        pass

    @abstractmethod
    def add_constraints(self, a, b, a_eq, b_eq) -> None:
        pass

    @abstractmethod
    def set_objective(self, c) -> None:
        pass

class ConcreteBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Class_Problem()

    @property
    def product(self) -> Class_Problem:
        product = self._product
        self.reset()
        return product

    def add_variables(self, num_vars, lower_bounds, upper_bounds) -> None:
        self._product.add_variables(num_vars, lower_bounds, upper_bounds)

    def add_constraints(self, a, b, a_eq, b_eq) -> None:
        self._product.add_constraints(a, b, a_eq, b_eq)

    def set_objective(self, c) -> None:
        self._product.set_objective(c)

class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build(self, num_vars, lower_bounds, upper_bounds, a, b, a_eq, b_eq, c) -> None:
        self.builder.add_variables(num_vars, lower_bounds, upper_bounds)
        self.builder.add_constraints(a, b, a_eq, b_eq)
        self.builder.set_objective(c)