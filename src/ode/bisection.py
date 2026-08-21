import numpy as np
import matplotlib.pyplot as plt


#Con funcion conocida

def du_cen(f, x, h, **kwargs):
    """Derivada central para un punto x."""
    return (f(x + h, **kwargs) - f(x - h, **kwargs)) / (2 * h)

def du_ad(f, x, h, **kwargs):
    """Derivada adelantada para un punto x."""
    return (f(x + h, **kwargs) - f(x, **kwargs)) / h

def du_atras(f, x, h, **kwargs):
    """Derivada atrasada para un punto x."""
    return (f(x, **kwargs) - f(x - h, **kwargs)) / h


def calcular_derivada_mixta(f, t):
    """
    Calcula la derivada numérica de f(theta, beta) sobre el vector t.
    Usa la Adelantada en t[0] y t[-1], y Central en el interior.
    """
    N = len(t)
    h_local = t[1] - t[0]
    derivada = np.zeros(N)
    for i in range(0, N-1):
        derivada[1:N-1] = du_cen(f, t[1:N-1], h_local)
        derivada[0] = du_ad(f, t[0], h_local)
        derivada[N-1] = du_atras(f, t[N-1], h_local)
    return derivada

#  Derivada para datos discretos

def du_cen_dis(u, h):
    """Derivada central para datos discretos."""
    return (u[2:] - u[:-2]) / (2*h)


def du_ad_dis(u, h):
    """Derivada adelantada para el primer punto."""
    return (u[1] - u[0]) / h


def du_atras_dis(u, h):
    """Derivada atrasada para el último punto."""
    return (u[-1] - u[-2]) / h


def calcular_derivada_mixta_dis(u, h):
    """
    Calcula la derivada numérica de datos discretos u.
    Usa adelantada en el primer punto,
    centrada en los puntos interiores
    y atrasada en el último.
    """
    N = len(u)
    derivada = np.zeros(N)
    derivada[0] = du_ad_dis(u, h)
    derivada[1:-1] = du_cen_dis(u, h)
    derivada[-1] = du_atras_dis(u, h)

    return derivada


#Bisección para datos con funcion conocida


def ceros_discretos(theta, v):
    """
    Encuentra los ceros de una función representada
    mediante datos discretos.

    theta : valores de la variable independiente
    v     : valores de la función

    Retorna
    -------
    ceros : valores aproximados donde v = 0
    """

    ceros = []

    for i in range(len(v) - 1):

        if v[i] * v[i+1] < 0:

            cero = 0.5 * (theta[i] + theta[i+1])

            ceros.append(cero)

    return ceros


def bis(f, a, b, tol=1e-10, iter=100, **kwargs):
    """
    Método de la bisección, encuentra raíces dividiendo 
    el intervalo [a,b] por mitades.
    
    Argumentos
    ----------
    f: función f(x, **kwargs)
    a,b : escalares, límites del intervalo
    beta: parámetro que se decide incluir explícitamente
    tol: tolerancia del método
    iter: Iteraciones máximas
    **kwargs: parámetros extras
    """
    iter_count = 0

    while iter_count < iter:
        c = 0.5 * (a + b)

        if abs(f(c, **kwargs)) < tol or abs(b - a) < tol:
            return c

        if f(a, **kwargs) * f(c, **kwargs) < 0:
            b = c
        else: 
            a = c
        iter_count += 1


#Biseccion para datos discretos

def puntos_criticos(theta, v):
    """
    Encuentra puntos críticos de theta a partir
    de cambios de signo en la velocidad.
    """
    criticos = []

    for i in range(len(v) - 1):

        if v[i] * v[i+1] < 0:

            theta_c = (theta[i] + theta[i+1]) / 2

            criticos.append(theta_c)

    return criticos



