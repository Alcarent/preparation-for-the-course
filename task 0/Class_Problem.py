from ortools.init.python import init
from ortools.linear_solver import pywraplp
#для реализации можно просто создать внутренние массивы в которые я буду добавлять 
#вводимые данные через написанную функцию, 
#так я смогу свободно добавлять и редактировать введённые ограничения и переменные
class Problem:
    
    ARR_OF_VAR = [] #имена и ограничения переменных
    
    ARR_OF_CONSTRAINTS = [] #другие ограничения, для корректной работы мы сначала задаём все переменные, а уже после доп условия
    
    ARR_OF_PROBLEM = []
    
    def __init__(this, NUM_VARS, NUM_CONSTRAINTS):
        print("Hi")
        
    def ADD_VAR(self, imya, min, max):#добавляем имя переменной и её ограничения
        self.ARR_OF_VAR.append(imya)
        self.ARR_OF_VAR.append(min)
        self.ARR_OF_VAR.append(max)
        
    def NUMBER_OF_VAR(self):
        return int(len(self.ARR_OF_VAR)/3)
    
    def ADD_CONSTR(self):
        for i in range(int(len(self.ARR_OF_VAR)/3)):
            name = self.ARR_OF_VAR[i*3]
            self.ARR_OF_CONSTRAINTS.append(int(input(f"{name} * "))) #добавляем значения переменных в ограничение (включая 0)
    
        self.ARR_OF_CONSTRAINTS.append(int(input('min = '))) #min ограничения
        self.ARR_OF_CONSTRAINTS.append(int(input('max = '))) #max ограничения

    def ADD_OBJ(self): #то же самое что и ADD_CONSTR, но для целевой функции
        for i in range(int(len(self.ARR_OF_VAR)/3)):
            name = self.ARR_OF_VAR[i*3]
            self.ARR_OF_PROBLEM.append(int(input(f"{name} * "))) #добавляем значения переменных в ограничение (включая 0)
    
        self.ARR_OF_PROBLEM.append(int(input('min = '))) #min ограничения
        self.ARR_OF_PROBLEM.append(int(input('max = '))) #max ограничения