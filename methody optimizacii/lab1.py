import matplotlib.pyplot as plt
import numpy as np

def f(x):
  if (x < -5):
    return -8*x-7
  elif((x>=-5)and(x<-3)):
    return -6*x+3
  elif((x>=-3)and(x<-2)):
    return -5*x+6
  elif((x>=-2)and(x<2)):
    return -2*x+11
  elif((x>=2)and(x<8)):
    return x/2+6
  else:
    return 5*x-30

# Шаг построения
lag = 0.01
# Отрезок построения
y_arr=[]
x_arr =[]
x = -10
while(x<10):
  x_arr.append(x)
  y_arr.append(f(x))
  x+=lag

fig = plt.figure()
plt.plot(x_arr, y_arr)
plt.title('График функции  $f(x)= x * x * (50 - x/2)')
plt.ylabel('f(x)')
plt.xlabel('x')

# Показать график
plt.show()