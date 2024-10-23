from ortools.init.python import init
from ortools.linear_solver import pywraplp


class Variable:
    Data = []
    def __init__(self, name, left_restriction, right_restriction):
        self.Data[0] = name
        self.Data[1] = left_restriction
        self.Data[2] = right_restriction
'''
для класса переменных никаких дополнительных возможностей прописывать не нужно, он просто хранит данные (можно реализовать "защиту от дурака", но на данный момент это будет лишним)
'''

class Constraint:
    Data = []
    Vector_of_var = []
    def __init__(self, left_restriction, right_restriction):
        self.Data[0] = "ct"
        self.Data[1] = left_restriction
        self.Data[2] = right_restriction

    def completion(self, value):
        self.Vector_of_var.append(value)

'''
в обоих классах элемент 
[1] - имя
[2] - левое ограничение
[3] - правое ограничение

класс Constraint также хранит в векторе Vector_of_var информацию об индексе каждой переменной
'''