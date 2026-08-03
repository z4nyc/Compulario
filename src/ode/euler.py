import numpy as np
import matplotlib.pyplot as plt

#Condiciones Iniciales
y0 = 0.0
v0 = -1.0


#Función conocida
def g(t, y_0, v_0, omega=1, g=9.8):
    return (y_0 + (g / (omega)**2)) * np.cos(omega * t) + v_0 / omega * np.sin(omega * t) - g/(omega**2)

Ttotal = 25.0
N = 1000  #tomaremos mil pasos
h = Ttotal / N

# Implementación del método
def f(x, omega=1.0, g=9.8):
    y,v = x

    return np.array([v, -y * omega ** 2 - g])

tiempo = np.linspace(0,Ttotal, N+1)

x = np.zeros((N+1,2))

x[0] = [y0, v0]


for n in range(N):
    x[n+1] = x[n] + h * f(x[n])

plt.figure(figsize=(8, 6))
plt.plot(tiempo, x[:,0], color = "red", label="Solución Númerica")
plt.plot(tiempo, g(tiempo,y0,v0), color = "blue", label="Solución Analítica")
plt.xlabel("Tiempo")
plt.ylabel("Posición")
plt.title("Solución Númerica vía Método Euler")
plt.grid(True)
plt.legend(fontsize=12)
plt.savefig("Euler.pdf")
plt.show()



