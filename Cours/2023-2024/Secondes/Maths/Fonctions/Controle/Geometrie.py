import matplotlib.pyplot as plt
import numpy as np

def h(x):
    return (x - 1.5)*(3 - x)

X = [x * 0.1 for x in range(0,31)]
H = [h(t) for t in X]
print(H)
plt.plot(X,H,label='h(x)')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()