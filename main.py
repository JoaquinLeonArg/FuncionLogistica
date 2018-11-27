import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

r = float(input('Ingrese r[0.3]: '))
K = float(input('Ingrese K[10]: '))
P0 = float(input('Ingrese P0[1]: '))
rango_x = int(input('Ingrese rango a mostrar[40]: '))
delta_t = float(input('Ingrese intervalo de discretización[1]: '))
t = np.arange(0, rango_x, delta_t)

def funcion(r, K, P):  # Ecuación diferencial logística (P'(t) = dP/dt)
    return eval('{P}*({r}-{r}/{K}*{P})'.format(r=r, K=K, P=P))

def metodo_adelantado():  # Método adelantado
    f = [P0]  # Condiciones iniciales
    if delta_t > 1:
        rango = int((rango_x-1)/delta_t)
    else:
        rango = int(rango_x / delta_t) - 1
    for x in range(rango):
        p_n = f[-1]  # Asignar P(t)
        p_prima = funcion(r, K, p_n)
        p_nsig = p_n + delta_t*p_prima  # Calcular P(t+1) = P(t) + P(t).deltaT.P'(t)
        f.append(p_nsig)
    return f

def metodo_atrasado():  # Método atrasado
    f = [P0]  # Condiciones iniciales
    if delta_t > 1:
        rango = int((rango_x-1)/delta_t)
    else:
        rango = int(rango_x / delta_t) - 1
    for x in range(rango):
        p_n = f[-1]  # Asignar P(t)
        p_prima = funcion(r, K, p_n)
        p_nsig = p_n + delta_t*p_prima  # Calcular P*(t+1) = P(t) + P(t).deltaT.P'(t)
        p_nsig = p_n + delta_t*funcion(r, K, p_nsig)  # Calcular P(t+1) = P(t) + P(t+1).deltaT.P'*(t+1)
        f.append(p_nsig)
    return f

f = metodo_adelantado()
plt.plot(t, f, color='blue', linestyle='-')
f = metodo_atrasado()
plt.plot(t, f, color='red', linestyle='-')
f = K*P0*np.e**(r*t)/(K+P0*(np.e**(r*t)-1))
plt.plot(t, f, color='yellow', linestyle='-')

plt.xlabel('t')
plt.ylabel('P(t)')
plt.title('Función logística')

leyenda_azul = mpatches.Patch(color='blue', label='Método adelantado')
leyenda_roja = mpatches.Patch(color='red', label='Método atrasado')
leyenda_amar = mpatches.Patch(color='yellow', label='Solución real')
plt.legend(handles=[leyenda_azul, leyenda_roja, leyenda_amar])

plt.show()