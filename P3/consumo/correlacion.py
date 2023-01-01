"""Correlación e histograma bivariado de dos variables aleatorias.

El momento de segundo orden :math:`m_{11} = E[XY]` es
denominado la correlación de :math:`X` y :math:`Y`. Recibe el símbolo
especial :math:`R_{XY}` por su importancia.

*Interpretaciones posibles de Correlación:*

    - "La correlación es el grado en el cual dos
      o más cantidades están linealmente asociadas".
    - (fundamental) "correlación no implica causalidad".

Éste módulo determina la correlación entre dos horas arbitrarias
:math:`H_{x}` y :math:`H_{y}` entendidas como
variables aleatorias (v.a) y diferentes, y además muestra
un histograma bivariados de ambas v.a.

"""
# Importar librerías a utilizar:
import numpy as np       # Manejo de arreglos
from scipy import stats  # Herramientas estadísticas
# Vizualización de datos
import matplotlib.pyplot as plt


def correlacion_horas(H_x, H_y, dias_xy, df):
    r'''Coeficiente de correlación (de Pearson).

    Para medir el grado de linealidad entre dos horas arbitrarias
    asumidas como dos variables aleatorias diferentes:
    :math:`H_{x}` y :math:`H_{y}` calcula el coeficiente de Pearson

    .. math:: \rho = \frac{C_{XY}}{\sigma_{X} \sigma_{Y}}

    donde :math:`C_{XY}` es la covarianza. :math:`\sigma_{X}`
    y :math:`\sigma_{Y}` corresponden a la desviación estandar
    de cada variable aleatoria :math:`X` e :math:`Y`.

    Parameters
    ----------
    H_x : entero
        *e.g.* de 0 a 24 (exclusivo).
    H_y : entero
        *e.g.* de 0 a 24 (exclusivo).
    dias_xy : entero
        Cantidad de días deseados. Número de muestras.
    df : DataFrame
        Base de datos.

    Returns
    -------
    corr_hrs : tupla
        Muestras de :math:`H_{x}` y :math:`H_{y}` y coef. Pearson:

        - [0] Matriz de datos de consumo de potencia a dos horas
          diferentes especificadas con una muestra por día.
        - [1] Coeficiente de pearson (el método ``.personr()``
          devuelve una tupla donde el índice [0] corresponde
          al coeficiente de Pearson).

    '''
    # Crear arreglo de registro de días seleccionados (índices)
    # con campo para las dos horas especificadas (columnas)
    horas_xy = np.empty((dias_xy, 2))

    # Lazo for para almacenar, en el arreglo horas_xy,
    # los datos de consumo de potencia a las dos tipos de horas
    # especificadas.
    for y in range(dias_xy):
        for x in range(dias_xy):
            horas_xy[x, 0] = df['MW'].iloc[H_x + 24*x]
        horas_xy[y, 1] = df['MW'].iloc[H_y + 24*y]

    # Retornar tupla:
    corr_hrs = (horas_xy, stats.pearsonr(horas_xy[:, 0], horas_xy[:, 1])[0])
    return corr_hrs


def visualizacion_horas(hora_x, hora_y):
    '''Histograma bivariado de distribución.

    Para la demanda de potencia (aparente) [MW] de dos horas
    arbitrarias, con una muestra por día.

    *Sugerencia*
        Utilizar función :py:func:`consumo.correlacion.correlacion_horas`
        para determinar determinar la matriz de datos de las variables
        aleatorias :math:`H_{x}` y :math:`H_{y}`.

    Parameters
    ----------
    hora_x : vector
        Conjunto de muestras de consumo de potencia
        a la hora :math:`H_{x}`.
    hora_y : vector
        Conjunto de muestras de consumo de potencia
        a la hora :math:`H_{y}`.

    Returns
    -------
    figura : plot
        Histograma bivariado de distribución.

    '''
    # Crear objetos: figura y ejes.
    ax = plt.figure().add_subplot(projection='3d')
    # Crear histograma
    hist, xedges, yedges = np.histogram2d(hora_x, hora_y, bins=25)

    # Definir plano de soporte
    xpos, ypos = np.meshgrid(
        xedges[:-1] + 0.25, yedges[:-1] + 0.25, indexing="ij"
    )
    xpos = xpos.ravel()
    ypos = ypos.ravel()
    zpos = 0

    # Dimenciones de cada barra de histograma (bins)
    dx = dy = 5 * np.ones_like(zpos)
    dz = hist.ravel()

    # Histograma bivariado en 3D
    ax.bar3d(xpos, ypos, zpos, dx, dy, dz)

    # Información de la gráfica
    ax.set_title('Consumo (MW) a dos horas en 365 días')
    ax.set_xlabel('Potencia (MW) a una hora $H_{x}$')
    ax.set_ylabel('Potencia (MW) a una hora $H_{y}$')
    ax.set_zlabel('Freq. Relativa')

    # Retornar figura del histograma bivariado 3D
    return plt.show()
