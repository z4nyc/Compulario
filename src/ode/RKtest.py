import numpy as np
import matplotlib.pyplot as plt

plt.style.use("bmh")

RK4 = np.array([[0, 0, 0, 0, 0],
                [0.5, 0.5, 0, 0, 0],
                [0.5, 0, 0.5, 0, 0],
                [0, 1/6, 1/3, 1/3, 1/6]])
#Donde ci = butcher[i, 0], bi = butcher[3, i]





def RK_gen(f, x0, tmax, dt, butch, t0 = 0, **kwargs):
    """
    Método de Runge-Kutta genérico para cualquier tabla de butcher
    """
    x0 = np.asarray(x0)

    t = np.arange(t0, tmax, dt)
    x = np.zeros((*t.shape, *x0.shape))
    x[0] = x0 

    shape = np.shape(butch)

    a = butch[0:shape[0]-1, 1:]
    b = butch[shape[0] - 1, 1:]
    c = butch[:, 0]
    

    for i in range(t.size - 1):
        #while x[i+1, 1] > 0: 
        K = np.zeros((np.size(b), *x0.shape))
        sum = 0
        for k in range(0, np.size(b)):
            K[k] = dt*f(t[i] + c[k]*dt, x[i] + sum, **kwargs)
            #if k != 0:
            for j in range(1, k):
                sum = sum + a[k-1, j-1]*K[j+1]
            
        sum2 = 0
        #print("alo", x[i])
        for p in range(1, np.size(b)+1):
            sum2 = sum2 + b[p-1]*K[p-1]
        
        x[i+1] = x[i] + sum2
        #if np.all(x[i+1][1] <= 0):
        #    return t,x
    return t, x

def spring(t, x, w = 5):
    posx, velx = x
    return np.array([velx, -w*posx])

posx0 = 1
velx0 = 0

t, X = RK_gen(spring, x0 = [posx0, velx0], tmax = 50, dt = 0.01, butch = RK4)

x, v = X[:, 0], X[:, 1]

plt.xlabel("$v$")
plt.ylabel("$x$")

plt.plot(v, x)

plt.savefig("../../img/ejemplos/phase_spring.pdf")

#plt.show()
