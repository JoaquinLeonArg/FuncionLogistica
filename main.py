import matplotlib.pyplot as plt
import numpy as np

# Definición de constantes
delta_t = 1
rango_x = 40
r, K, P0 = 0.3, 10, 1
t = np.arange(0, rango_x, delta_t)

def funcion(r, K, P):  # Ecuación diferencial logística (P'(t) = dP/dt)
    return eval('{P}*({r}-{r}/{K}*{P})'.format(r=r, K=K, P=P))

def metodo_adelantado():  # Método adelantado
    f = [P0]  # Condiciones iniciales
    for x in range(rango_x-1):
        p_n = f[-1]  # Asignar P(t)
        p_prima = funcion(r, K, p_n)
        p_nsig = p_n + delta_t*p_prima  # Calcular P(t+1) = P(t) + P(t).deltaT.P'(t)
        f.append(p_nsig)

    plt.plot(t, f, color='red', linestyle='steps')
    plt.plot(t, f, color='blue', linestyle='-')
    plt.xlabel('t')
    plt.ylabel('P(t)')
    plt.title('Función logística')
    plt.show()

def metodo_atrasado():  # Método atrasado
    f = [P0]  # Condiciones iniciales
    for x in range(rango_x-1):
        p_n = f[-1]  # Asignar P(t)
        p_prima = funcion(r, K, p_n)
        p_nsig = p_n + delta_t*p_prima  # Calcular P*(t+1) = P(t) + P(t).deltaT.P'(t)
        p_nsig = p_n + delta_t*funcion(r, K, p_nsig)  # Calcular P(t+1) = P(t) + P(t+1).deltaT.P'*(t+1)
        f.append(p_nsig)

    plt.plot(t, f, color='red', linestyle='steps')
    plt.plot(t, f, color='blue', linestyle='-')
    plt.xlabel('t')
    plt.ylabel('P(t)')
    plt.title('Función logística')
    plt.show()

metodo_adelantado()
metodo_atrasado()