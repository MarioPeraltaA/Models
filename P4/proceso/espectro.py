"""Densidad Espectral de Potencia a partir de funcion muestra.

Por la definición matemática de la densidad espectral de potencia *(psd)*
calcula la función y gráfica cuando los datos son finitos y discretos.

"""
from scipy import signal
import matplotlib.pyplot as plt


def psd(dia, secuencia_datos):
    """Calcula y grafica la psd.

    Para una única función muestra de la secuencia de datos dada
    es decir, un día arbitrario.

    Parameters
    ----------
    dia : entero
        Representa miembro del agregado.
    secuencia_datos : ndarray
        Arreglo de los datos de consumo de potencia
        por cada hora durante :math:`n` días.

    Returns
    -------
    figura : plot
        Gráfica del psd
    Sxx : ndarray
        Densidad espectral de potencia.
    fxx : ndarray
        Arreglo de muestras de frecuencia.

    """
    datos_dia = secuencia_datos[dia, :]

    # Número de muestras
    N = len(datos_dia)

    # Duración
    T = N - 1
    # La frecuencia de muestreo fs = N * T = 24 * 23
    # Donde N es el número de datos y T la duración de la señal.
    fsxx = N * T

    # psd
    (fxx, s) = signal.periodogram(datos_dia, fsxx, scaling='density')

    # Por definición se multiplica delta t cuadrado entre periodo
    # Duración del espectro
    T_s = len(s) - 1

    # Diferencia de tiempo al cuadrado
    deltat_2 = pow(N/T_s, 2)

    # Aplicar definición de psd para muestras finitas:
    Sxx = (deltat_2/T)*s

    # Graficar en todo el dominio de la frecuencia
    plt.plot(fxx, Sxx, 'green')
    # Etiquetas
    plt.xlabel('freq. [Hz]')
    plt.ylabel('PSD')
    plt.title('Densidad espectral de potencia (psd)')
    # Guardar gráfica
    # plt.savefig('../figs/psdplot.svg')
    # Graficar
    plt.show()
    return (Sxx, fxx)
