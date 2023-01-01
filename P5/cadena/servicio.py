r"""Éste módulo encuentra las probabilidades de cada estado en un sistema M/M/1.

Para una corriente de arribo de Poisson con parámetro :math:`\lambda`
y un tiempo de servicio exponencialmente distribuido
con parámetro :math:`\nu` y un sólo servidor, :math:`s` = 1, se determina
la probabilidad de estado estable de cada estado :math:`i`
-es decir, la probabilidad de que el número de personas
en el sistema sea :math:`i`- y determina el porcentaje
del tiempo que la fila del sistema está por encima de cierto valor.

"""
import numpy as np


def estados(omega, p, q, n):
    r"""Para ``n`` pequeño, obtiene el vector de estado estable.

    Se usa la fórmula recursiva con los valores de los
    parámetros :math:`\Omega_{i}` y las probabilidades de transición
    :math:`p_{i}` , :math:`q_{i}` para
    :math:`n = 0, 1, 2, ... i` con :math:`\lvert n \rvert = i + 1` estados definidos.

    Parameters
    ----------
    omega : vector
        Arreglo de parámetros de permanencia para todos i-ésimos estados.
    p : vector
        Arreglo de probabilidades de transición de :math:`i` a :math:`i + 1`
        para todos los :math:`i`-ésimo estado.
    q : vector
        Arreglo de probabilidades de transición de :math:`i` a :math:`i - 1`
        para todos los :math:`i`-ésimo estados.
        Advertencia: Tener en cuenta que :math:`p_{i}` del :math:`i`-ésimo término
        sería entonces 0, :math:`q_{i}` = 1 y :math:`\Omega_{i} = i \nu`,
        ya que el módulo ``analisis.py``
        es únicamente para colas de longitud indefinidad.
    n : entero
        Número de estados (:math:`i + 1`). Estados definidos y finitos.

    Returns
    -------
    v_estable : vector
        Vector de estado estable (probabilidades de estado estable).

    """
    # Vector de estado estable
    phi = np.empty(n)

    # Estado i = 1
    phi[1] = (omega[0] * p[0] * 1) / (omega[1] * q[1])

    # para el resto de estados i = 2, 3, ...
    for h in range(2, n):
        phi[h] = (omega[h - 1] * p[h - 1] * phi[h - 1]) / (omega[h] * q[h])

    # Normalizar y despejar phi_i para estado i = 0
    phi[0] = 1/(1+np.sum(phi[1:]))

    # Definir vector de estado estable
    v_estable = np.empty(n)
    # Probabilidad para cada estado
    for v in range(n):
        if v == 0:
            v_estable[v] = phi[0]
        else:
            v_estable[v] = phi[0] * phi[v]

    return v_estable


def probabilidad(lam_llegada, nu, i):
    r"""En general, probabilidad de estado de cada estado.

    Para cantidad de estados (:math:`i + 1`) indefinidos,
    calcula la probabilidad de estado estable del
    estado arbitrario :math:`i` dado.

    Parameters
    ----------
    lam_llegada : flotante
        Parámetro de intensidad de llegadas al sistema.
    nu : flotante
        Parámetro de intensidad servicio del sistema.
    i : entero
        Estado arbitrario.

    Returns
    -------
    phi_i : flotante
        Probabilidad del estado :math:`i`.

    Examples
    --------
    >>> from cadena import servicio
    >>> # Parámetros de sistema
    >>> lam_llegada = 0.0350
    >>> nu = 0.0488
    >>> i = 5       # Estado arbitrario
    >>> # Probabilidad de estado: i
    >>> v_phi = servicio.probabilidad(lam_llegada, nu, i=5)
    >>> # Mostrar vector resultante
    >>> print('Probabilidad del estado i = {} es {:0.4%}'.format(i, v_phi))
    Probabilidad del estado i = 5 es 5.3750%

    """
    # Cociente de parámetros del sistema
    r = lam_llegada / nu
    # Por fórmula
    phi_i = pow(r, i) * (1 - r)

    # Retornar probabilidad del estado i
    return phi_i


def fila(lam_llegada, nu):
    r"""Tiempo que :math:`L_{q}` clientes o más esperan en fila.

    Sea :math:`L` el número promedio de la longitud
    de clientes en el sistema y :math:`L_{q}` el número
    promedio de espacios que el cliente espera antes de
    recibir el servicio (cuando el servidor está ocupado), entonces
    la función calcula el porcentaje de clientes que hacen una fila
    de :math:`L_{q}` o más espacios antes de ser atendidos.

    Parameters
    ----------
    lam_llegada : flotante
        Parámetro de intensidad de llegadas al sistema.
    nu : flotante
        Parámetro de intensidad servicio del sistema.

    Returns
    -------
    Lq : entero
        Espacios promedio antes de recibir atención.
    PLq : flotane
        Porcentaje de tiempo en que los clientes que hacen fila
        (cuando todos los servidores están ocupados)
        de al menos :math:`L_{q}` espacios antes de recibir el servicio.

    Examples
    --------
    >>> from cadena import servicio
    >>> # Parámetros de sistema
    >>> lam_llegada = 0.0350
    >>> nu = 0.0488
    >>> # Promedio de clientes en fila: sistema M/M/1
    >>> Lq = servicio.fila(lam_llegada, nu)
    >>> # Mostrar porcentaje promedio de tiempo que Lq o más clientes esperan:
    >>> print(
    >>>     ('El {:0.4f}% del tiempo los clientes').format(Lq[1]),
    >>>     ('esperan en fila, en general,\n'),
    >>>     ('al menos {} espacios antes de ser atendidos.'.format(Lq[0])))
    El 36.9635% del tiempo los clientes esperan en fila, en general,
    al menos 2 espacios antes de ser atendidos.

    """
    # Promedio clientes en fila cuando el servidor está ocupado
    fila = (pow(lam_llegada, 2)) / ((nu) * (nu - lam_llegada))
    # Obtener entero próximo superior:
    Lq = np.ceil(fila).astype('int')
    # Relación de parámetros
    r = lam_llegada / nu
    # Longitud de cola
    L = np.ceil(Lq / r).astype('int')
    phi = 0        # Inicializar vector estado estable

    # Operar sumatoria
    for n in range(L):
        # Probabilidad de estado: Llamar función anterior
        # phi_i = pow(lam_llegada/nu, n) * (1 - lam_llegada/nu)
        phi_i = probabilidad(lam_llegada, nu, n)
        phi += phi_i
    # Sacar complemento
    PLq = 1 - phi

    # Retornar porcentaje
    return (Lq, PLq*100)
