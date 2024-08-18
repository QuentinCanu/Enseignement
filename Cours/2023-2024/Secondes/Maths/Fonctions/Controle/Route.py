import matplotlib.pyplot as plt
import math

def a(t):
    return (- 2 / 60) * t * (t-100)

def b(t):
    return (-7/12) * abs(t) - (14 / 12) * abs(t - 30) - (21/12) * abs(t - 80) + 175

print(b(0))

def c(x):
    return -(13 * x**6)/1512000000 + (979*x**5)/302400000 - (577*x**4)/1260000 + (12923*x**3)/432000 - (137363*x**2)/151200 + (2993*x)/252

X = [i / 1000  for i in range(0,100000 + 1)]
A = [a(t) for t in X]
B = [b(t) for t in X]
C = [c(t) for t in X]
plt.plot(X,A,label='Voiture A')
plt.plot(X,B,label='Voiture B')
plt.plot(X,C,label='Voiture C')
plt.legend()
plt.xlabel('Kilomètre de route')
plt.ylabel('Vitesse')
plt.xticks(range(0,105,5))
plt.yticks(range(0,90,5))
plt.grid(True)
plt.show()