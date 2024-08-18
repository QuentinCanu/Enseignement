import matplotlib.pyplot as plt
import math

def a(t):
    return 276

def b(t):
    return 1.5 * t

def c(t):
    return 1.5*abs(t) - abs(t - 60) + 60

X = [i for i in range(0,370,10)]
A = [a(t) for t in X]
B = [b(t) for t in X]
C = [c(t) for t in X]
plt.plot(X,A,label='Abonnement A')
plt.plot(X,B,label='Abonnement B')
plt.plot(X,C,label='Abonnement C')
plt.legend()
plt.xlabel('Minutes')
plt.ylabel('Prix')
plt.xticks([i for i in range(0,370,20)], fontsize=7)
plt.yticks(range(0,600,50),fontsize=7)
plt.grid(True)
plt.show()