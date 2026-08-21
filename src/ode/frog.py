import numpy as np
import matplotlib.pyplot as plt



def _condiciones_iniciales(t, x0, y0):
    """  
    Función útil para guardar las condiciones iniciales y 
    guardar algunas variables que se ocuparán después
    t = (Iterable) arreglo de números que funciona como tiempo
        da forma al problema
    x0, y0 = (Escalares o iterables) condiciones iniciales 
    """
    x0 = np.asarray(x0)
    y0 = np.asarray(y0)
    x = np.zeros((len(t),) + x0.shape)
    y= np.zeros((len(t),) + y0.shape)
    x[0] = x0
    y[0] = y0
    return x,y

def dy(a, omega = 2.0, g= 9.8):
    """Derivada a utilizar en el método leap-frog
    """
    return -1 * ( omega **2 ) * a - g

def leapfrog_3steps(dy, x0, y0, t, **kwargs):
    """ 
    Método del salto de la rana, retorna arreglos (soluciones)
    dy = (función) es la derivada se utiliza en cada paso
    x0,y0 = (escalares o iterables) condiciones iniciales
    t = (iterable) arreglo que hace de tiempo
    """
    dt = np.diff(t) #paso
    x, y = _condiciones_iniciales(t, x0, y0)    
    dy0 = dy(x0, **kwargs) 
    for n in range(t.size-1):
        ymedio = y[n] + 0.5 * dt[n] * dy0
        x[n+1] = x[n] + dt[n] * ymedio
        dy0 = dy(x[n+1], **kwargs)
        y[n+1] = ymedio + 0.5 * dt[n] * dy0
    return  x, y

#t = np.linspace(0,10,1000)
#u,w = leapfrog_3steps(dy, 0.0, -1.0,t, omega=2.0)

#omega = 2.0
#E = np.zeros(len(t))
#E[0] = 0.5 * w[0]**2 + 0.5 * omega **2 * (u[0] + 9.8 / (omega ** 2))**2

#for n in range(len(E)-1):
    # Calcular energía en el paso n+1
    E[n + 1] = 0.5 * w[n+1]**2 + 0.5 * (omega) **2 * (u[n+1] + 9.8 / (omega**2)) ** 2


# Gráficos de posición, velocidad y energía
#fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

#ax1.plot(u, w, label="Leapfrog", color="tab:blue")
#ax1.plot(u[0], w[0],"ro", markersize=8, zorder=3, label="Inicio (t=0)")
#ax1.set_title("Espacio de Fase (y vs v)")
#ax1.set_xlabel("Posición (y)")
#ax1.set_ylabel("Velocidad (v)")
#ax1.grid(True)
#ax1.legend()

#ax2.plot(t, E, label="Energía", color="tab:red")
#ax2.set_title("Energía vs Tiempo (Euler)")
#ax2.set_xlabel("Tiempo (t)")
#ax2.set_ylabel("Energía (E)")
#ax2.grid(True)
#plt.tight_layout()
#plt.savefig("frog.pdf")
#plt.show()


