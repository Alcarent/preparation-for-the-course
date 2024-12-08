import matplotlib.pyplot as plt
import numpy as np

def f (x):
  return 6*x**2-240*x+3600

#шаг построения
lag = 0.01
#отрезок построения
x = np.arange(0, 30, lag)
y = f(x)
fig = plt.figure()
plt.plot(x, y)
plt.title('График функции  $f(x)=6 x^2  - 240 x + 3600$ ')
plt.ylabel('f(x)')
plt.xlabel('x')