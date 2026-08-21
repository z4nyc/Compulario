import numpy as np
import matplotlib.pyplot as plt 
from frog import _condiciones_iniciales, leapfrog_3steps
from bisection import puntos_criticos 
def dy(a, omega = 2.0):
    return (-omega ** 2) * np.sin(a)

t = np.linspace(0,10,10000)
u,w = leapfrog_3steps(dy, 0 / 2, 0, t, omega=2.0)


plt.plot(t,u)
plt.show()

omegas_cero = puntos_criticos(u,w)
print(omegas_cero)
