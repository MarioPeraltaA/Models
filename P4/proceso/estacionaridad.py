"""Para una secuencia aleatoria se evalúa cuan dependiente del tiempo és.

Gracias a los conceptos de proceso Estacionario en el Sentido Amplio
(wss) y Ergodicidad (conociendo el promedio temporal) es posible
estimar cuan estacionaria es las secuencia aleatoria dada.

"""
import numpy as np
# Librería para verificar estacionaridad del proceso.
from statsmodels.tsa.stattools import adfuller


def wss(secuencia_datos):
    """Determina si el proceso aleatorio dado es *wss* .

    Aplica la prueba Augmented Dickey-Fuller
    con una toleracia del 5% para rechazar la hipótesis H0.

    Parameters
    ----------
    secuencia_datos : ndarray
        Matriz de los datos de consumo de potencia
        por cada hora durante :math:`n` días.

    Returns
    -------
    mensaje : string
        Mensaje si es estacionario o no.

    """
    # Implicaciones de wss:
    # i. E[P(t)] = constante
    # ii. E[P1P2] = Rtau

    # Obtener tamaño de las dimensiones de la secuencia:
    d, h = np.shape(secuencia_datos)

    # Crear un sólo vector a lo largo del tiempo:
    sec_datos = np.reshape(secuencia_datos, d*h)

    # Aplicar prueba Augmented Dickey-Fuller:
    # Si el p-value es menor o igual a 0.05 o si el valor absoluto
    # de la prueba estadística ADF es mayor que el valor crítico del 5%
    # se rechaza la hipótesis H0 y la secuencia es estacionaria.
    ADF, p, _, _, values, _ = adfuller(sec_datos)

    if (p <= 0.05) and (ADF <= values['5%']):
        # Se rechaza la hipótesis H0
        return ('El proceso es estacionario al menos en el sentido amplio.')
    else:
        return ('El proceso no es estacionario en el sentido amplio.')


def prom_temporal(dia, secuencia_datos):
    """Dada una función muestra determina el promedio temporal.

    En un intevalo de todo el dominio del tiempo donde
    ésta está definida. i. e. Sea P una variable aleatoria para el consumo
    de potencia a una hora particular y p una muestra de P
    si la muestra es el día :math:`d` el intervalo serán 24 hrs.

    Parameters
    ----------
    dia : entero
        Representa la muestra. No debe ser superior a la candidad
        de días de los que dispone la base de datos.
    secuencia_datos : ndarray
        Matriz de los datos de consumo de potencia
        por cada hora durante :math:`n` días.

    Returns
    -------
    p_media : flotante
        Promedio temporal de la muestra dada.

    """
    # Dominio del tiempo donde está definida la muestra:
    t = np.linspace(0, 23, 24)
    # Nota: Al se secuencia <t> es discreto.

    # Selccionar de la base de datos el día asignado
    s = secuencia_datos[dia, :]

    # Calcular promedio tempotal
    p_media = (1)/(len(t)) * np.trapz(s, t)

    # Retornar promedio temporal de la muestra dada.
    return p_media


def ergodicidad(secuencia_datos):
    """Determina si un proceso es ergódico.

    Es decir, un procesos tal que los que los promedios temporales
    igualan a los estadísticos. Hace uso de la función
    prom_temp().

    Parameters
    ----------
    secuencia_datos : ndarray
        Matriz de los datos de consumo de potencia
        por cada hora durante :math:`n` días.

    Returns
    -------
    mensaje : string
        Un mensaje que indica si el proceso es ergódico o no.

    """
    # Arreglo vacío de días
    dias, hrs = np.shape(secuencia_datos)
    prmt_fs = np.empty(dias)

    # Se toma la media temporal de cada función muestra:
    for ds in range(dias):
        # Llamar función prom_temporal
        prmt_fs[ds] = prom_temporal(ds, secuencia_datos)

    # Media de los promedios muestras temporales:
    m_promt = np.mean(prmt_fs)

    # Media estadística de la variable aleatoria:
    # Intervalos:

    # Arreglo de potencia promedio
    pmedia_hr = np.empty(hrs)

    # Potencia promedio a cada hora
    for hr in range(hrs):
        pmedia_hr[hr] = np.mean(secuencia_datos[:, hr])

    # Media "promedio" del proceso
    E_va = np.mean(pmedia_hr)

    # Diferencia entre promedios.
    error_E = m_promt - E_va

    # Tolerancia
    if pow(error_E, 2) <= pow(E_va*0.05, 2):
        return ('El proceso cumple con ergodicidad')
    else:
        return ('El proceso no cumple con ergodicidad')
