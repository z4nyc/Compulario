import numpy as np
import matplotlib.pyplot as plt

plt.style.use("bmh")

xi = np.array([1, 2, 3, 4, 5])
yi = np.array([2.5, 3.8, 6.7, 7.9, 10.1]) #tendencia casi lineal

#Definimos las variables necesarias

xprom = np.mean(xi)
yprom = np.mean(yi)

x2prom = np.mean(xi**2)
xyprom = np.mean(xi*yi)

A = np.array([[1, xprom],
             [xprom, x2prom]])

B = np.array([[yprom],
             [xyprom]])

a0, a1 = np.linalg.solve(A, B)

x = np.linspace(np.min(xi), np.max(xi), 10)

plt.scatter(xi, yi, label = "Datos")
plt.plot(x, a0 + a1*x, c = "r", label = "Ajuste lineal por MMC")


plt.xlabel("$x$")
plt.ylabel("$y$")

plt.legend()

plt.savefig("../../img/interpol/line_reg.pdf")

plt.show()
