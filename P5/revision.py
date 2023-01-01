r"""Aquí se llaman todas las funciones del paquete "cadena".

En un sistema M/M/:math:`\1` o M/M/:math:`\s`, con datos de clientes importados
cuyas llegadas son descritas como una corriente de *Poisson*
con parámetro :math:`\lambda`. Cada uno de los :math:`\s` servidores
tiene un tiempo de servicio exponencial con parámetro :math:`\nu`.

*Secciones:*

    A. Llama ``analisis.py`` para determianar parámetros del sistema.
    B. Llama ``simulacion.py`` para ver respuesta del sistema.
    C. Llama ``servicio.py`` para calcular las probabilidades de estados
    de estado estable y el número de clientes en cola.
    D. Llama ``dimensionamiento.py`` para determinar aquellos valores
    :math:`\s` y :math:`\nu` que cumple con cierto criterio de calidad.

"""

from cadena import analisis, simulacion, servicio, dimensionamiento
import numpy as np
import pandas as pd

# -----
# SECCIÓN A: Analisis
# -----

# Importar datos
clientes = pd.read_csv('clientes.csv')

# Número de clientes
N = len(clientes)

# Determinar media de tiempo de llegada entre clientes
media_lam = clientes["intervalo"].mean()

# Determinar media de servicio a partir de los datos
media_nu = clientes["servicio"].mean()

# Parámetro de intervalo de llegada
lam_llegada = analisis.llegada(media_lam)

# Parámetro de servicio
nu = analisis.servicio(media_nu)

# Parámetros de los primeros seis estados
i = 5        # Estado del sistema al tiempo t
n = i + 1    # Número total de estados hasta instante t
# Arreglo de los tres parámetros
parmtrs = np.empty((n, 3))
# Para cada estado solicitado y sistema M/M/1
for c in range(n):
    parmtrs[c, :] = analisis.parametros(lam_llegada, nu, c, s=1)

# Extraer vectores de parámetros encontrados:
# Parámetro de permanencia
omega = parmtrs[:, 0]
# Probabilidades de transición
p = parmtrs[:, 1]
q = parmtrs[:, 2]

# Mostrar resultados:
print('Parámetro de intensidad de llegada: {:0.4f}'.format(lam_llegada))
print('Parámetro de Intensidad de servicio: {:0.4f}'.format(nu))
print('Hasta el estado i = {} (inclusivo) los parámetros son: '.format(i))
print('Omega: ', omega)
print('p: ', p)
print('q: ', q)

# -----
# SECCIÓN B: Simulación
# -----

# Obtener dinámica del sistema
sistema = simulacion.sistema(lam_llegada, nu, N)

# Graficar:
simulacion.visualizacion(sistema[0], sistema[1], sistema[2], N)

# -----
# SECCIÓN C: Servicio
# -----

# Probabilidad de estado i = 5
v_phi = servicio.probabilidad(lam_llegada, nu, i=5)

# Promedio de clientes en fila: sistema M/M/1
Lq = servicio.fila(lam_llegada, nu)

# Resultados:
# Mostrar vector resultante
print('Probabilidad del estado i = {} es {:0.4%}'.format(i, v_phi))
# Mostrar porcentaje promedio de tiempo que Lq o más clientes esperan:
print(
    ('El {:0.4f}% del tiempo los clientes').format(Lq[1]),
    ('esperan en fila, en general,\n'),
    ('al menos {} espacios antes de ser atendidos.'.format(Lq[0])))

# -----
# SECCIÓN D: Dimensionamiento
# -----

# Criterios de diseño:
Lq = 5       # Clientes en cola (esperan a ser atendidos)
P = 99       # Porcentaje de tiempo
s = 3        # Servidores disponibles
# Llamar funciones del módulo:
# M/M/1: Tiempo
T = dimensionamiento.t_servicio(lam_llegada, Lq, P)
# M/M/s: Aumento de servidores
ss = dimensionamiento.servidores(lam_llegada, nu, Lq, P)
# M/M/s: Disminución tiempo
t = dimensionamiento.tiempo(lam_llegada, nu, Lq, P, s)

# Mostrar resultados:
# M/M/1
if (s == 1 or ss == 1):
    print(
        ('El servidor debe demorar {} segundos como máximo').format(T),
        ('en asistir a cada cliente.'))
# M/M/s Cuando la cantidad de servidores disponibles ya es suficiente
elif s >= ss:
    print('Con la intensidad de servicio actual el sistema ya cumple criterio')
    print('Cantidad de servidores mínimos requeridos: ', ss)
# M/M/s cuando no hay suficientes servidores dispobibles
# y se debe disminuir el tiempo de servicio.
else:
    print(
        ('Si se cuenta con {} servidores unicamente, cada\n'.format(s)),
        ('servidor debería tardar {} seg. en asistir algún cliente.'.format(t)))
