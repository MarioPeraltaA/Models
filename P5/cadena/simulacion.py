r"""Éste módulo simula y visualiza un sistema M/M/1 con parámetros dados.

Tales parámetros corresponden a la intensidad del intervalo
de llegada, en forma de corriente de Poisson, entre clientes
y la intensidad del servicio que está exponencialmente distribuida,
se asumen provenientes de una distribución exponencial :math:`\frac{1}{scale}`.
Luego el sistema en cuestión se trata del
proceso de Nacimiento y Muerte de un servidor únicamente :math:`s` = 1

"""
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


def sistema(lam_llegada, nu, N):
    """Simula una secuencia de llegadas y salidas de clientes al sistema.

    Para los parámetros de llegada y salida dados, genera una secuencia
    de llegadas y salidas de clientes al sistema.

    Parameters
    ----------
    lam_llegada : flotante
        Parámetro de la intensidad de intervalos de llegadas
        entre clientes al sistema.

    nu : flotante
        Parámetro del tiempo de servicio del sistema es decir, lo que dura
        el cliente en su trámite una vez que es atendido.

    N : entero
        Número de clientes.

    Returns
    -------
    sis : tupla
        Arreglo de datos generados con los parámetros especificados
        que representa una simulación del sistema en el tiempo. Posiciones:

        - [0] tiempos de llegadas de clientes.
        - [1] tiempos de servicio de cada cliente.
        - [2] tiempos en que cada cliente es atentido.

    Examples
    --------
    >>> from cadena import simulacion
    >>> # Obtener dinámica del sistema
    >>> sistema = simulacion.sistema(lam_llegada, nu, N)
    >>> # Utilizar estos datos obtenidos como argumentos de la función
    >>> # cadena.simulacion.vizualizacion(), ver ejemplo para graficar.

    """
    # Asumiendo que el intervalo de llegada entre los clientes,
    # es de distribución exponencial
    # Determinar parámetro de intervalo de llegada:
    media_lam = 1 / lam_llegada

    # Determinar parámetro de servicio:
    media_nu = 1 / nu

    # -----
    # Generar PDF's
    # -----

    # Distribución de los tiempos de llegada entre cada cliente
    X = stats.expon(scale=media_lam)

    # Distribución de los tiempos de servicio a cada cliente
    Y = stats.expon(scale=media_nu)

    # -----
    # Generar datos de tiempo
    # -----

    # Intervalos entre llegadas
    # (Segundos desde el último cliente)
    t_intervalos = np.ceil(X.rvs(N)).astype('int')

    # Tiempos de servicio: Dependerá del trámite del cliente.
    t_servicio = np.ceil(Y.rvs(N)).astype('int')

    # -----
    # Instantes de llegada y atención
    # -----

    # Instante en que cada cliente llega:
    # Tiempos de llegada de cada cliente, cuyo primer elemento
    # es el intervalo de llegada del primer cliente
    t_llegadas = [t_intervalos[0]]

    # Anexar, mediante lazo for, los instantes (segundos) de llegada
    # de cada cliente
    for t in range(1, N):
        siguiente = t_llegadas[t - 1] + t_intervalos[t]
        t_llegadas.append(siguiente)

    # Tiempos de atención: Instantes en que cada cliente es atentido
    inicio = t_llegadas[0]            # primera llegada
    fin = inicio + t_servicio[0]      # primera salida

    # Lista del conjunto de tiempos de atención.
    t_atencion = [inicio]
    for i in range(1, N):
        inicio = np.max((t_llegadas[i], fin))
        fin = inicio + t_servicio[i]
        t_atencion.append(inicio)

    # Ordenar la dinámica del sistema
    sis = (t_llegadas, t_servicio, t_atencion)
    return sis


def visualizacion(t_llegadas, t_servicio, t_atencion, N):
    """Gráfica del comportamiento del sistema.

    Para los parámetros de llegada y salida dados, crea una gráfica para
    observar un ejemplo del comportamiento del sistema.

    Parameters
    ----------
    t_llegadas : vector
        tiempos de llegadas de clientes.
    t_servicio : vector
        tiempos de servicio de cada cliente.
    t_atencion : vector
        tiempos en que cada cliente es atentido.
    N : entero
        Número de clientes

    Returns
    -------
    plot : objeto de pyplot
        Dinámica (respuestas) del sistema.

    Examples
    --------
    >>> from cadena import simulacion
    >>> # Importar datos
    >>> clientes = pd.read_csv('clientes.csv')
    >>> # Número de clientes
    >>> N = len(clientes)
    >>> # Graficar: Con los datos obtenidos en cadena.simulacion.sistema()
    >>> simulacion.visualizacion(sistema[0], sistema[1], sistema[2], N)
    >>> # Ver gráfica en la sección de resultados

    """
    duracion = t_atencion[-1] + t_servicio[-1] + 1
    t = np.zeros(duracion)

    # Recorrer cada cliente a lo largo de lo que dura el sistema
    for c in range(N):
        # Nacimiento: Llegada c-ésimo cliente
        i = t_llegadas[c]
        t[i] += 1
        # Muerte: Salida c-ésimo cliente
        j = t_atencion[c] + t_servicio[c]
        t[j] -= 1

    # Umbral de P o más personas en sistema (hay P - 1 en fila)
    P = 5

    # Instantes de tiempo con P o más solicitudes en sistema
    exceso = 0

    # Proceso aleatorio (estados n = {0, 1, 2, ...})
    Xt = np.zeros(t.shape)

    # Inicialización de estados n
    n = 0

    # Recorrido del vector temporal y conteo de clientes (estado n)
    for i, c in enumerate(t):
        n += c    # sumar (+1) o restar (-1) al estado
        Xt[i] = n
        if Xt[i] >= P:
            exceso += 1

    # # Fracción de tiempo con P o más solicitudes en sistema
    # fraccion = exceso / len(t)

    plt.plot(Xt)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Clientes en el sistema, n')
    # Guardar figura
    # plt.savefig('figs/respuesta.svg')
    # Retornar gráfica
    return plt.show()
