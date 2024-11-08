from ortools.init.python import init
from ortools.linear_solver import pywraplp
from Class_Variable_and_Constraint import *
from abc import ABC, abstractmethod
'''
для начало нужно определить что мне вообще нужно:
    1) классы для хранения данных о переменныхи и ограничениях, внутри которых я буду хранить данные в более удобном формате и упрощу себе их вывод 

    2) сам билдер будет строить класс таким образом:
        1. создаём вектор из переменных и заполняем их данные
        2. по итоговому числу переменных определяем характеристики ограничений (число переменных)
        3. создаём целевую функцию, она будет использовать класс ограничений
        4. после того как мы заполнили все данные, нужно их все преобразовать в отдельные переменные 

    3) как только начинка с решением готова, нужно организовать вывод всех численных данных решения, включая каждую пременную и ограничение
'''

''' Создаём абстрактный класс для с частями нашей проблемы'''
class ProblemBuilder(ABC):
    @abstractmethod
    def add_variables(self):
        pass

    @abstractmethod
    def add_constraints(self):
        pass

    @abstractmethod
    def add_objective_function(self):
        pass

    @abstractmethod
    def get_problem(self):
        pass

'''директор'''
class PtoblemDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_problem(self):
        self.builder.add_variable()
        self.builder.add_constraint()
'''сам класс проблемы'''
class Problem:
    solver = pywraplp.Solver.CreateSolver("GLOP")
    infinity = solver.infinity()
    def __init__(self):
        self.variables = []
        '''для заполнения используется класс Variable'''

        self.constraints = [] 
        '''для заполнения используется класс Constraint, последнее ограничение- целевая функция'''
        
    def add_variable(self, num_vars):
        i = 0
        while(i < num_vars):
            L_R = input("Enter left restriction for variable{i}: ")
            R_R = input("Enter right restriction for variable{i}: ")
            variable = Variable(i, L_R, R_R)
            self.variables.append()
            i += 1

    def add_constraint(self, num_cons):
        i = 0
        while(i < num_cons):
            j = 0
            L_R = input("Enter left restriction for constrain{i}: ")
            R_R = input("Enter right restriction for constrain{i}: ")
            constrain = Constraint(L_R, R_R)
            
            while(j < len(self.variables)):
                index = input("Enter index of variable{j} for constraint{i}: ")
                constrain.completion(index)
                j += 1

            i += 1