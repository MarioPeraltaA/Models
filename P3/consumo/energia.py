r''' Modelos probabilísticos de demanda de energía semanal y anual.

Éste módulo calcula la energía consumida [MJ], los parámetros que modelan
la distribución de demanda energética [MJ] y finalmente, haciendo uso del
Teorema del límite central, encuentra el los parámetros de
la distribución Normal de demanda energética anual.

*Teorema de límite central*
    Convergencia en la distribución.

*Definición*
    Considérese :math:`X_{1}, ..., X_{N}` variables aleatorias
    *independientes e idénticamente distribuidas* ``iid``,
    con media común :math:`\mu_{X_{i}} = \mu`
    y desviación estándar :math:`\sigma_{X_{i}} = \sigma`. Sea además

    .. math:: S_{N} = X_{1} + \cdots + X_{N}

    La **suma** de ellas. Según el teorema del límite central:

    .. math:: S_{N} \sim \mathcal{N}\left(N \mu,\,\sigma \sqrt{N}\right)

    conforme :math:`N \rightarrow \infty`, donde :math:`N \mu`
    es la media y :math:`\sigma \sqrt{N}` la
    desviación estándar de la distribución normal.

'''
# Importar librerías a utilizar:
import numpy as np        # Manejo de arreglos
from scipy import stats   # Herramientas estadísticas
# Vizualización de datos
import matplotlib.pyplot as plt

# Obtener distribución de mejor ajuste
from fitter import Fitter


def energia_semanal(semanas, df):
    '''Energía total consumida por períodos de siete días.

    Mediante el número de horas equivalente a la cantidad
    de semanas solicitadas selecciona, de la base de datos
    disponible, el consumo de potencia respectivo partiendo
    desde la hora 0 del 20190101 hasta la hora
    (``semanas`` :math:`*` 168)
    (exclusivo) para luego integrar dichos datos, cuyo dominio
    ya se sabe que es el tiempo, y por tanto el resultado
    corresponde a la energía (trabajo). Por:

    .. math:: W = \int_{t_{i}}^{t_{f}} Pdt

    donde

    - :math:`W` : Trabajo
    - :math:`P` : Potencia
    - :math:`t_{i}` : Tiempo inicial
    - :math:`t_{f}` : Tiempo final

    Parameters
    ----------
    semanas : entero
        Número de semanas sobre las que se desea
        calcular la energía consumida (MJ).
    df : DataFrame
        Base de datos.

    Returns
    -------
    energia : flotante
        Energía total consumida a lo largo de un número dado de semanas
        como la integral de la potencia consumida en el mismo lapso
        de tiempo.

    '''
    # Crear vector vacío de tamaño en horas para las semanas dadas.
    datos_semanales = np.empty(semanas * 168)

    # Obtener el tamaño del vector de horas resultantes.
    horas = len(datos_semanales)

    # Obtener del DataFrame original los datos de consumo
    # de potencia para la cantidad de horas
    # equivalentes a las semanas requeridas y almacenarlos
    # en el vector datos_semanales.
    datos_semanales[:horas] = df['MW'].iloc[:horas]
    energia = np.trapz(datos_semanales)    # Integrar

    # Retornar la energía (MJ)
    return energia


def modelo_energia_semanal(semanal, df):
    '''Modelo probabilístico de demanda de energía semanal.

    Determina un modelo probabilístico y los parámetros
    de mejor ajuste de la distribución (PDF) de consumo
    de energía de una semana a lo largo de todo el
    período de días disponible (365 exclusivo).
    Asumiendo que un año tiene 52 semanas.

    Parameters
    ----------
    semanal : entero
        Número de semanas sobre las que
        se desea calcular la energía consumida (MJ).
    df : DataFrame
        Base de datos.

    Returns
    -------
    grafica : plot
        Conjunto de distribuciones de mejor ajuste.
    resumen : lista
        Resumen de las cinco distribuciones de mejor ajuste.
    paramtrs : dict
        Diccionario con los parámetros de la distribución
        que mejor modela los datos proporcionados.
    datos_energia : vector
        Datos de consumo de energía para las semanas dadas.

    '''
    # Arreglo para almacenar el consumo por semana
    # donde los índices son el registro de horas equivalentes
    # a una semana y las columnas cada una de las semanas.
    datos_potencia = np.empty((168, semanal))

    # Lazo for para obtener datos de consumo de potencia
    # para una cantidad de semanas determinadas:
    for s in range(semanal):
        k = s
        c = s + 1
        datos_potencia[:, s] = df['MW'].iloc[k*168:c*168]

    # Vector vacío para almacenar la energía consumida
    # del tamaño del número de semanas asignados:
    datos_energia = np.empty((semanal))

    # Lazo for para registrar consumo de energía
    # cada semana, después de integrar la potencia consumida:
    for m in range(semanal):
        datos_energia[m] = np.trapz(datos_potencia[:, m])

    # Usar método Fitter de la librería fitter
    # para obtener la distribución y los parámetros
    # de mejor ajuste para los datos brindados (consumo
    # de energía por semana dentro de una catidad
    # de semanas determinadas):
    plt.figure()
    fenergia = Fitter(datos_energia)

    # Retornar tupla:
    # [0]: Distribución de mejor ajuste
    # [1]: Resumen de las cinco mejores distribuciones de mejor ajuste
    # [2]: Parámetros de la distribución de mejor ajuste
    # [3]: Datos del consumo energético por semana.
    return (
        fenergia.fit(), fenergia.summary(),
        fenergia.get_best(), datos_energia
    )


def modelo_energia_anual(semanas):
    r'''Modelo probabilístico de consumo de energía anual.

    Toma los parámetros de la distribución (PDF)
    de consumo de energía semanal y determina
    los parámetros de mejor ajuste para
    la distribución de consumo de energía anual, que por
    teorema de límite central deduce que será
    aproximadamente *Normal*; además muestra la
    pdf de tal distribución. Asume que la distribución de
    demanda energética es:

    .. math:: f_{X}(x) = \left [ \pi \left(\frac{x^{2}}{\left(a \textrm{  sign}(x) + 1 \right)^{2}} + 1 \right) \right ]^{-1}

    para un número real :math:`x` y parámetro de
    inclinación :math:`-1 < a < 1`. En términos de los parámetros
    :math:`L` para ``loc`` y :math:`S` para ``scale`` la **PDF** es
    equivalente a:

    .. math:: f_{X}(x; a, L, S) = \frac{1}{S}f_{X}\left( \frac{\left(x - L \right)}{S} \right )

    Con:

    - :math:`a = 0.31710287214411537`
    - :math:`L = 211933.0125841577`
    - :math:`S = 3296.880755879225`

    Parameters
    ----------
    semanas : entero
        52 equivale a un año.

    Returns
    -------
    figura : plot
        Gráfica de histograma y distribución normal
        de mejor ajuste.
    mu : flotante
        Media.
    sigma : flotante
        Desviación estándar.

    '''
    # Modelo: Distribución y parámetros de mejor ajuste para el
    # consumo de energía semanal. Obtenidos con la funcion:
    # modelo_energia_semanal()
    energia_model = {'skewcauchy':
                     {'a': 0.31710287214411537,
                      'loc': 211933.0125841577,
                      'scale': 3296.880755879225}}

    # Extraer parámetros del diccionario: energia_model:
    a = energia_model['skewcauchy']['a']
    loc = energia_model['skewcauchy']['loc']
    scale = energia_model['skewcauchy']['scale']

    # Distribución de consumo de energía semanal (MJ):
    energia_semanal = stats.skewcauchy(a, loc, scale)

    # Vector vacío para almacenar el consumo de energía
    # cada semana:
    energia_anual = np.empty(semanas)

    # Se suma la energía consumida por semana
    # a lo largo de todas las semanas dadas.
    #
    # Asumiendo que la demanda de energía en
    # todas las semanas es la misma:
    for w in range(semanas):
        energia_anual[w] = sum(energia_semanal.rvs(168))

    # Por Teorema del Límite Central se obtinene una
    # Distribución normal, cuyos parámetros son:
    mu, sigma = stats.norm.fit(energia_anual)

    # Distribución de densidad para consumo anual:
    energia_pdf = stats.norm(mu, sigma)
    # Intervalo de dominio en el tiempo
    inicio = energia_pdf.ppf(0.01)
    fin = energia_pdf.ppf(0.99)

    # Soporte para la PDF de consumo de energía anual:
    plt.figure()
    t = np.linspace(inicio, fin, 60)

    # Graficar ambos la distribución Normal y el histograma
    # de consumo energético anual:
    plt.plot(
        t, energia_pdf.pdf(t),
        linestyle='--', label='Curva de ajuste normal'
    )
    plt.hist(
        energia_anual, bins=30, density=True, label='Energía anual'
    )

    # Información de la distribución de consumo anual:
    plt.title('Distribución de consumo de energía anual')
    plt.xlabel('Energía [MJ]')
    plt.ylabel('Freq. Relativa')
    plt.legend()

    # Retornar distribución Normal y sus parámetros
    # así como el histograma respectivo.
    return (plt.show(), mu, sigma)
