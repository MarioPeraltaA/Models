r"""Éste módulo dimensiona parámetros para cierto citerio de calidad.

Para un sistema M/M/s, determina el número de servidores :math:`s`
o, a través de cierto parámetro de servicio :math:`\nu`,
el tiempo promedio de servicio necesarios para satisfacer
el criterio de calidad requerido, a saber:
Se desea tener :math:`L_{q}` (o menos) cliente en fila
(más los :math:`s` del sistema que están siendo atendidos)
al menos el :math:`P` % del tiempo.
En otras pabras: Dado un porcentaje del tiempo, :math:`P`,
si el sistema tiene más de una cantidad :math:`L_{q}`
de clientes en fila por una fracción de tiempo mayor
a :math:`\left(1 - \frac{P}{100} \right)` entonces no satisface el criterio.
Por ejemplo, es deseado que no exista una fila de más de 5 clientes el
95% del tiempo. Si se analiza el sistema por un periodo de tiempo de 10 minutos
y durante un minuto la fila fue de 6 clientes o más, entonces no fue satisfecho
el criterio, puesto que solamente el 90% del tiempo fue cumplida la condición,
y se requería el 95%.

"""
import numpy as np                  # Manipulación de datos
import math                         # Usar factorial
from scipy.optimize import fsolve   # Resolver ecuaciones


def t_servicio(lam, Lq, P):
    r"""Para M/M/1, tiempo promedio de servicio que cumple criterio.

    Si se cuenta con un único servidor, considera el criterio
    de calidad especificado y el parámetro de intensidad de
    arribo del sistema actual para encontrar
    una taza de servicio "v" tal que cumpliría el criterio
    de calidad de servicio.

    Parameters
    ----------
    lam: flotante
        Parámetro de llegada del sistema.
    Lq : entero
        Número de espacios por debajo del cual se desea que los
        clientes esperen en fila antes de recibir el servicio.
    P : entero
        Porcentaje de tiempo mínimo requerido en que se desea que la
        situacción de exceso (espera de más de Lq espacios antes de
        ser atendido) se presente únicamente un
        :math:`\left(1 - \frac{P}{100} \right)` del tiempo.
        Advertencia: :math:`0 < P < 100`.

    Returns
    -------
    t : entero
        tiempo promedio de servicio (segundos), dedicado a cada cliente
        para que el servidor único cumpla con el criterio de calidad.
        Nota:
        Corresponde al recíproco del parámetro de intensidad mínima de servicio
        que cumple criterio.

    Examples
    --------
    >>> from cadena import dimensionamiento
    >>> lam_llegada = 0.0350
    >>> # Criterios de diseño:
    >>> Lq = 5       # Clientes en cola (esperan a ser atendidos)
    >>> P = 99       # Porcentaje de tiempo
    >>> # Para M/M/1: Tiempo
    >>> T = dimensionamiento.t_servicio(lam_llegada, Lq, P)
    >>> print(
    >>>     ('El servidor debe demorar {} segundos como máximo').format(T),
    >>>     ('en asistir a cada cliente.'))
    El servidor debe demorar 15 segundos como máximo en asistir a cada cliente.

    """
    # Estados para el diseño, asumiendo M/M/1:
    L = Lq + 1        # Número de clientes en el sistema
    e = L + 1         # Situación de exceso

    # Porcentaje de tiempo, como máximo, en situación de exceso
    p = 1 - (P/100)

    # Para que el sistema alcance estado estacionario
    # se debe cumplir: rho = (lam / s * nu) < 1.
    # Luego sea v = s * nu
    #
    # Se asumen un v si la cantidad de servidores fuera s = 1
    # Aplicar definición para M/M/1
    def f(v):
        y = (lam/v)**(e) - p
        return y

    # Resolver ecuación para "v"
    # suposición inicial positivo cerca de cero: v0 = 0.001
    v = fsolve(f, 0.0001)

    # Obtener el entero próximo superior del inveso del parámetro "v"
    t = np.ceil(1 / v[0]).astype('int')

    # Retornar tiempo promedio de servicio (segundos) que cada cliente
    # debe recibir para cumplir criterio.
    return t


def probabilidades(r, L, s):
    r"""Probabilidades de estado sistema M/M/s.

    Función auxiliar. Determina la probabidad
    acumulada a partir del estado :math:`i`, o sea
    la probabilidad de que la cola tenga una
    longitud al menos de :math:`L`.

    Parameters
    ----------
    r : flotante
        Relación de parámetros de intensidad. Se debe cumplir que:
        :math:`\frac{\rho}{s} < 1`
    L : entero
        Longitud promedio de la cola del sistema.
    s : entero
        Número de servidores.

    Returns
    -------
    probabilidad : flotante
        Probabilidad acumulada de al menos :math:`L + 1`

    """
    kes = []         # Inicializar sumatoria de k's
    # Probabilidad de estado inicial: i = 0
    for k in range(s):
        stadok = r**k / math.factorial(k)
        # Operar sumatoria
        kes.append(stadok)
    alfa = sum(kes)
    beta = (s * r**s) / ((math.factorial(s))*(1-((r)/(s))))
    serie = alfa + beta
    phi0 = 1 / serie

    # Calcular probabilidad asumiendo estados
    # mutuamente excluyentes (o sea no pueden ocurrir
    # multiples estados a la vez)
    #
    # Probabilidad de cola como mucho L (inclusivo).
    phiL = []
    for i in range(L + 1):
        if i < s:
            phii = ((pow(r, i)) / (math.factorial(i))) * phi0
            phiL.append(phii)
        # Todos servidores ocupados
        else:
            phis = (((s**s) * (pow(r/s, i))) / (math.factorial(s))) * phi0
            phiL.append(phis)
    # Tomar complemento: Probabilidad de almenos L + 1 (inclusivo)
    probabilidad = 1 - sum(phiL)
    return probabilidad


def servidores(lam_llegada, nu, Lq, P):
    r"""Para M/M/s encuentra número de servidores mínimos requeridos.

    Considera el criterio de calidad especificado y los parámetros
    de arribo y servicio del sistema actual para encontrar
    la cantidad de servidores mínimos :math:`s` que lo cumplirían.

    Parameters
    ----------
    lam_llegada: flotante
        Parámetro de llegada del sistema.
    nu : flotante
        Parámetro de servicio actual del sistema.
    Lq : entero
        Número de espacios por debajo del cual se desea que los
        clientes esperen en fila antes de recibir el servicio.
    P : entero
        Porcentaje de tiempo mínimo requerido en que se desea que la
        situacción de exceso (espera de más de Lq espacios antes de
        ser atendido) se presente únicamente un
        :math:`\left(1 - \frac{P}{100} \right)` del tiempo.
        Advertencia: :math:`0 < P < 100`.

    Returns
    -------
    s : entero
        Cantidad de servidores mínimos que cumplen con el requerimiento.
        Advertencia: Para :math:`s \geqslant 10` cumputacionalmente es muy demandante
        por tanto se sugiere un modelo de infinitos servidores :math:`s` cuya
        probabilidad de estados converga en una distribución de Poisson.

    Examples
    --------
    >>> from cadena import dimensionamiento
    >>> lam_llegada = 0.0350
    >>> nu = 0.0488
    >>> # Criterios de diseño:
    >>> Lq = 5       # Clientes en cola (esperan a ser atendidos)
    >>> P = 99       # Porcentaje de tiempo
    >>> # M/M/s: Aumento de servidores
    >>> ss = dimensionamiento.servidores(lam_llegada, nu, Lq, P)
    >>> print('Cantidad de servidores mínimos requeridos: ', ss)
    Cantidad de servidores mínimos requeridos: 5

    """
    s = 1                     # Inicializar cantidad de servidores
    Pt = 1 - (P/100)          # Cota máxima de porcentaje de tiempo
    r = lam_llegada / nu      # Relación de parámetros de intensidad
    # Longitud de cola promedio del sistema i = L
    L = np.ceil(Lq + r).astype('int')

    # Iterar hasta cumplir criterio:
    while s < 10:
        # Llamar función de probabilidad acumulada
        probabilidad = probabilidades(r, L, s)
        # Verificar criterio
        if probabilidad < Pt:
            # Condición se satisface
            break
        # No cumple todavía
        s += 1
    return s


def tiempo(lam_llegada, nu, Lq, P, s):
    r"""Para M/M/s, tiempo promedio máximo de servicio que cumple criterio.

    Con la cantidad de servidores de los que se dispone,
    considera el criterio especificado y los parámetros
    de intensidad del sistema actual (M/M/1),
    para encontrar el tiempo máximo que deba tardar, cada servidor
    del sistema, en asistir clientes.

    Parameters
    ----------
    lam : flotante
        Parámetro de llegada del sistema.
    nu : flotante
        Parámetro de intensidad de servicio actual del sistema.
    Lq : entero
        Número de espacios por debajo del cual se desea que los
        clientes esperen en fila antes de recibir el servicio.
    P : entero
        Porcentaje de tiempo mínimo requerido en que se desea que la
        situacción de exceso (espera de más de Lq espacios antes de
        ser atendido) se presente únicamente un
        :math:`\left(1 - \frac{P}{100} \right)` del tiempo.
        Advertencia: :math:`0 < P < 100`.
    s : entero
        Número de servidores de los que se dispone.
        Advertencia :math:`s \geqslant 2`.

    Returns
    -------
    t : entero
        Tiempo (segundos) promedio necesario de servicio a cierto
        cliente (una vez que es atendido) que satisfase
        el criterio dado cuando hay múltiples servidores.

    Examples
    --------
    >>> from cadena import dimensionamiento
    >>> lam_llegada = 0.0350
    >>> nu = 0.0488
    >>> # Criterios de diseño:
    >>> Lq = 5       # Clientes en cola (esperan a ser atendidos)
    >>> P = 99       # Porcentaje de tiempo
    >>> s = 3        # Servidores disponibles
    >>> # M/M/s: Disminución tiempo
    >>> t = dimensionamiento.tiempo(lam_llegada, nu, Lq, P, s)
    >>> print(
    >>>     ('Si se cuenta con {} servidores unicamente, cada\n'.format(s)),
    >>>     ('servidor debería tardar {} seg. en asistir algún cliente'.format(t)))
    Si se cuenta con 3 servidores unicamente, cada
    servidor debería tardar 20 seg. en asistir algún cliente.

    """
    Pt = 100 - P              # Cota máxima de porcentaje de tiempo
    r = lam_llegada / nu      # Relación de parámetros de intensidad
    # Longitud de cola promedio del sistema i = L
    L = np.ceil(Lq + r).astype('int')
    # Llamar función de probabilidad acumulada
    probabilidad = probabilidades(r, L, s)
    pro = 100 * probabilidad      # Tomar procentaje
    # Relación de probabilidades
    D = pro / Pt
    if D <= 1:
        # Ya se cuenta con la intensidad de servicio necesaria
        # Tomar recíproco entero superior
        t = np.ceil(1 / nu).astype('int')
        # Retornar segundos necesarios
        return t
    else:
        # Probabilidad de cola como mucho L (inclusivo).
        phiL = 1 - probabilidad
        # Constante de proporción
        E = (phiL+D-1) / (D*phiL)
        # Nueva intensidad por servidor
        nu_s = E * nu
        # Tomar recíproco entero superior
        t = np.ceil(1 / nu_s).astype('int')
        # Retornar segundos necesarios
        return t
