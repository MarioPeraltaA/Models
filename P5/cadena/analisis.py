r"""Éste módulo determina permanencia y transición de un sistema M/M/1.

Para un proceso de nacimiento y muerte en tiempo continuo,
si al tiempo :math:`t`, la máquina está en el estado :math:`i`
es denotado por :math:`X_{t}` y representa
la longitud de la cola (:math:`L`) en ése instante.
Asume que los clientes arriban como una corriente de Poisson
con parámetro :math:`\lambda`. Sea :math:`\lambda` un parámetro
de intensidad es decir, clientes que arriban, en promedio,
por unidad de tiempo (segundos).
Los tiempos de servicio son aleatorios, pero se supone que están
exponencialmente distribuidos con parámetro :math:`\nu`,
luego se cumple que el tiempo medio de servicio es :math:`\frac{1}{\nu}`.

"""


def llegada(media_lam):
    r"""Parámetro de llegada.

    Encuentra el parámetro de la intensidad de llegadas al sistema.
    El parámetro :math:`\lambda` es de la distribución exponencial:

    .. math:: f_X(x) = \lambda e^{-\lambda x}

    Parameters
    ----------
    madia_lam : flotante
        Promedio de intervalos de llegada entre clientes
        (tomado del DataFrame).

    Returns
    -------
    lam_llegada : flotante
        El parámetro de intensidad de llegada (frecuencia promedio
        con que llegan los clientes).

    Examples
    --------
    >>> from cadena import analisis
    >>> import pandas as pd
    >>> clientes = pd.read_csv('clientes.csv')      # Importar datos
    >>> # Determinar media de tiempo de llegada entre clientes
    >>> media_lam = clientes["intervalo"].mean()
    >>> # Parámetro de intervalo de llegada
    >>> lam_llegada = analisis.llegada(media_lam)
    >>> print('Parámetro de intensidad de llegada: {:0.4f}'.format(lam_llegada))
    Parámetro de intensidad de llegada: 0.0350

    """
    lam_llegada = 1 / media_lam
    return lam_llegada


def servicio(media_nu):
    r"""Parámetro de servicio.

    Para servicio único :math:`s` = 1 encuentra el parámetro del tiempo
    de servicio del sistema.
    El parámetro :math:`\nu` es de la distribución exponencial:

    .. math:: f_X(x) = \nu e^{-\nu x}

    Parameters
    ----------
    media_nu : flotante
        Promedio de tiempos de servicio (tomado del DataFrame).

    Returns
    -------
    nu : flotante
        El parámetro nu representa lo que demora el cliente
        en su trámite una vez que es atendido.
    
    Examples
    --------
    >>> from cadena import analisis
    >>> import pandas as pd
    >>> clientes = pd.read_csv('clientes.csv')     # Importar datos
    >>> # Determinar media de servicio a partir de los datos
    >>> media_nu = clientes["servicio"].mean()
    >>> # Parámetro de servicio
    >>> nu = analisis.servicio(media_nu)
    >>> print('Parámetro de Intensidad de servicio: {:0.4f}'.format(nu))
    Parámetro de Intensidad de servicio: 0.0488

    """
    # Determinar parámetro de servicio:
    nu = 1 / media_nu
    return nu


def parametros(lam_llegada, nu, i, s):
    r"""Permanencia y probabilidades de transición de :math:`i`.

    Dependiendo del número de servidores :math:`s` determina
    el parámetro de permanencia (:math:`\Omega_{i}`)
    en el estado actual dado :math:`i` que, asumido como no
    absorvente, existen las probabilidades de transición
    al estado :math:`i + 1` o :math:`i - 1` siendo
    éstas :math:`p` y :math:`q` respectivamente.
    El parámetro :math:`\Omega` es de la distribución exponencial:

    .. math:: f_X(x) = \Omega e^{-\Omega x}

    Parameters
    ----------
    lam_llegada : flotante
        El parámetro de llegada.
    nu : flotante
        El parámetro nu representa lo que demora el cliente
        en su trámite una vez que es atendido.
    i : entero
        Estado específico :math:`i`.
    s : entero
        Número de servidores.

    Returns
    -------
    Omega : flotante
        Parámetro de permanencia (recíproco del tiempo de espera promedio).
    p : flotante
        Probabilidad de la máquina salir del
        estado :math:`i` cambiar al estado :math:`i + 1`.
    q : flotante
        Probabilidad de la máquina salir del
        estado :math:`i` cambiar al estado :math:`i - 1`.

    Examples
    --------
    >>> from cadena import analisis
    >>> import numpy as
    >>> # Parámetros de los primeros seis estados
    >>> i = 5        # Estado del sistema al tiempo t
    >>> n = i + 1    # Número total de estados hasta instante t
    >>> # Arreglo de los tres parámetros
    >>> parmtrs = np.empty((n, 3))
    >>> # Para cada estado solicitado y sistema M/M/1
    >>> for c in range(n):
    >>>     parmtrs[c, :] = analisis.parametros(lam_llegada, nu, c, s=1)
    >>> # Extraer vectores de parámetros encontrados:
    >>> # Parámetro de permanencia
    >>> omega = parmtrs[:, 0]
    >>> # Probabilidades de transición
    >>> p = parmtrs[:, 1]
    >>> q = parmtrs[:, 2]
    >>> # Mostrar resultados:
    >>> print('Parámetro de intensidad de llegada: {:0.4f}'.format(lam_llegada))
    >>> print('Parámetro de Intensidad de servicio: {:0.4f}'.format(nu))
    >>> print('Hasta el estado i = {} (inclusivo) los parámetros son: '.format(i))
    >>> print('Omega: ', omega)
    >>> print('p: ', p)
    >>> print('q: ', q)
    Hasta el estado i = 5 (inclusivo) los parámetros son: 
    Omega:  [0.03503731 0.08385829 0.08385829 0.08385829 0.08385829 0.08385829]
    p:  [1.         0.41781576 0.41781576 0.41781576 0.41781576 0.41781576]
    q:  [0.         0.58218424 0.58218424 0.58218424 0.58218424 0.58218424]

    """
    # Caso: Estado inicial
    if i == 0:
        omega = lam_llegada
        p = 1
        q = 0
    # Caso: i >= 1 y servidores saturados
    elif i >= s:
        omega = lam_llegada + s*nu
        p = lam_llegada / omega
        q = s*nu / omega
    # Caso: i >= 1 y servidores disponibles
    else:
        omega = lam_llegada + i*nu
        p = lam_llegada / omega
        q = i*nu / omega

    return (omega, p, q)
