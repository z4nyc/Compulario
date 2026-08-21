import numpy as np
import matplotlib.pyplot as plt

plt.style.use("bmh")

def lagrange(x, xi, yi):
    n = len(xi) - 1

    sum = 0.0
    for j in range(n+1):
        lj = yi[j]
        for i in range(n+1):
            if i != j:
                lj = lj * (x - xi[i])/(xi[j] - xi[i])

        sum = sum + lj
    return sum

N = np.random.randint(101)

xi = np.linspace(0, 1, 10) #10*np.random.rand(N)
fi = xi + 0.1*np.random.randint(1, 10, xi.size)

x = np.linspace(np.min(xi), np.max(xi), 100)


plt.scatter(xi, fi)
plt.plot(x, lagrange(x, xi, fi), "r--", label = "Polinomio interpolador")
#plt.plot(x, np.sin(x) + np.exp(-x**2), label = "$f(x) = e^{-x^{2}} + \\sin(x)$")
plt.legend()

plt.savefig("../../img/interpol/gibbs.pdf")

plt.show()
