"""Calcula autocorrelación y autocovarianza.

Para una secuencia aleatoria dada calcula el grado de linealidad
y disperción gracias al concepto de momentos.
 
"""
import numpy as np
from scipy import stats
from proceso import proceso


def momentos(hr1, hr2, pw_dia):
    """Calcular autocorrelación y autocovarianza.

    Entre los instantes dados hr1 y hr2 de un proceso aleatorio
    generando las respectivas distribuciones "genlogistic"
    a partir de los parámetros en los instantes dados.

    Parameters
    ----------
    hr1 : entero
        Hora del día.
    hr2 : entero
        Hora del día.
    pw_dia : ndarray
        Arreglo de los datos de consumo de potencia
        por cada hora durante :math:`n` días.

    Returns
    -------
    a_CR : tupla
        Tuplan de flotantes. Posiciones:

        - [0] autocorrelación.
        - [1] Autocovarianza.

    """
    # Importar parámetros tamaño: (24, 3)
    parmtrs_datos = proceso.parametros(pw_dia, 24)

    # Extraer parámetros específicos:
    # Un instante:
    c1, l1, s1 = parmtrs_datos[hr1, :]

    # El otro instante:
    c2, l2, s2 = parmtrs_datos[hr2, :]

    # Obtener datos de los instanes
    Xt_1 = pw_dia[:, hr1]
    Xt_2 = pw_dia[:, hr2]

    # Generar pdf:
    X1 = stats.genlogistic(c1, l1, s1)
    X2 = stats.genlogistic(c2, l2, s2)

    # Coeficiente de Pearson:
    r, _ = stats.pearsonr(Xt_1, Xt_2)

    # Calcular desviación estandar:
    std1 = np.std(Xt_1)
    std2 = np.std(Xt_2)

    # Calcular valor Esperado: E[*]
    # Límites de integración: (-inf, +inf)
    x1 = np.linspace(X1.ppf(0.01), X1.ppf(0.99), 100)
    x2 = np.linspace(X2.ppf(0.01), X2.ppf(0.99), 100)

    # Calcular valor esperado por medio de la definición de integral
    E1 = np.trapz(x1 * X1.pdf(x1), x1)
    E2 = np.trapz(x2 * X2.pdf(x2), x2)

    # Autocovarianza:
    CXX = r * std1 * std2

    # Autocorrelación:
    RXX = CXX + (E1 * E2)

    a_CR = (RXX, CXX)
    return a_CR
