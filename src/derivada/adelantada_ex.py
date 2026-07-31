import numpy as np
import matplotlib.pyplot as plt

def deriv_adel(f, x, h = 1e-3): #Definimos una función para nuestra derivada adelantada
    return( (f(x + h) - f(x))/h )

f = lambda x: np.sin(x)

x = np.linspace(-2*np.pi, 2*np.pi, 100)

df_dx = deriv_adel(f, x) #Calculamos la derivada numéricamente con nuestra derivada adelantada

realdf = lambda x: np.cos(x) #Derivada analítica de nuestra función

#Graficamos la función con su derivada numérica
#plt.plot(x, f(x))
#plt.plot(x, df_dx)

#Graficamos la función con su derivada analítica
#plt.plot(x, f(x))
#plt.plot(x, realdf(x))

#Graficamos la derivada analítica con la numérica
#plt.plot(x, df_dx)
#plt.plot(x, realdf(x))

#Definimos el error y lo graficamos
err = np.abs(df_dx - realdf(x))
#plt.plot(x, err)

#Graficamos el error absoluto en x = 0.5 para distintos valores de h
h = np.geomspace(1e-20, 1e-1, 50)#[1e-18, 1e-15, 1e-12    i, 1e-9, 1e-5]
k = 0
abserr = np.zeros(len(h))
for i in h:#np.linspace(1e-5, 1e-1, 11):
    deriv = deriv_adel(f,x = 0.3, h = i)
    abserr[k] = np.abs(deriv - realdf(x = 0.3))
    k += 1
plt.xscale("log")
plt.yscale("log")
plt.xlabel("$h$")
plt.ylabel("Error")
plt.scatter(h, abserr)#, label = f"$h$ = {h:.1f}")

#plt.legend()
plt.savefig("../../img/derivadas/adnterr.pdf")
plt.show()

