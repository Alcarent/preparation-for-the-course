from ortools.init.python import init
from ortools.linear_solver import pywraplp
#для реализации можно просто создать внутренние массивы в которые я буду добавлять 
#вводимые данные через написанную функцию, 
#так я смогу свободно добавлять и редактировать введённые ограничения и переменные
class Problem:
    ARR_OF_VAR = []
    ARR_OF_MIN_VAR = []
    ARR_OF_MAX_VAR = []
    
    def __init__(this, NUM_VARS, NUM_CONSTRAINTS):
        print("Hi2")
        
    def ADD_VAR(self, char(imya), min, max):
        self.ARR_OF_VAR.append('{imya}')
    