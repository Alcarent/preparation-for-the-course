from ortools.init.python import init
from ortools.linear_solver import pywraplp
<<<<<<< HEAD
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

class Problem_and_solve:
    solver = pywraplp.Solver.CreateSolver("GLOP")
    infinity = solver.infinity()
    def __init__(self) -> None:
        return self

    
=======
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
>>>>>>> 15d3d25eec6467807cbe486ded78836be35fcc73
