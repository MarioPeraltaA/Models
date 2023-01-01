'''Con datos importados éste módulo obtiene modelo, momentos y distribución.

Se cuenta con un archivo ``.json`` que contiene los datos de consumo
de potencia en megawatt [MW] desde el primer día del año 2019 hasta
la primera hora del año 2020, es decir desde la fecha "20190101" hasta
la hora 0 de la fecha "20200101" que corresponde al último registro y que
es excluido. Posteriormente obtiene el modelo de demanda de potencia
a una hora arbitraria, la distribución con sus respectivos momentos
y finalmente una gráfica de la misma.

'''
# Importar librerías a utilizar:
import pandas as pd      # Manipulación de datos
import numpy as np       # Manejo de arreglos
from scipy import stats  # Herramientas estadísticas
# Vizualización de datos
import matplotlib.pyplot as plt
import json              # Importar archivo .json

# Obtener distribución de mejor ajuste
from fitter import Fitter


def datos_demanda(ruta):
    '''Importar y extraer datos necesarios para análisis.

    Importa datos en formato `.json` y extrae aquellos
    de consumo de potencia [MW] para ser retornados como un
    ``DataFrame`` de pandas para posteriores análisis.

    **Nota:**
        Los datos estan ordenados en forma secuencial eso es
        0, 1, 2, ..., 23, 0, 1, 2, ..., 23, ...

    Parameters
    ----------
    ruta : cadena
        Ruta de base de datos que se dispone
        como archivo .json

    Returns
    -------
        df_demanda : DataFrame
           Base de datos de consumo de potencia por hora
           del año 2019.

    '''
    # -----
    # Transformar la información obtenida a un DataFrame de pandas
    # -----
    f = open(ruta, mode='r')   # Abrir archivo para leer
    demanda_datos = json.loads(f.read())       # dict de python
    f.close()                                  # Cerrar archivo
    datos = demanda_datos['data']              # Filtrar llave/key 'data'
    df = pd.DataFrame(datos)                   # Crear DataFrame

    # Retornar DataFrame
    return df


def datos_hora(hora, dias, df):
    '''Consumo de potencia de una hora arbitraria.

    A lo largo de los días. *e.g.*  Los datos del consumo
    de potencia (MW) para las 18:00 horas en 365 días.

    Parameters
    ----------
    hora : entero
        *e.g.* de 0 a 24 (exclusivo).
    dias : entero
        Número de días deseados.
    df : DataFrame
        Base de datos.

    Returns
    -------
    datos_hr : tupla
        Datos de demanda de potencia a una hora particular
        extraídos de la base de datos. Posiciones:

        - [0] Vector de consumo de potencia a la hora especificada.
        - [1] Hora especificada.
        - [2] Cantidad de días seleccionados.

    '''
    # Crear vector vacío de la hora específica
    # del tamaño de los días deseados.
    hora_x = np.empty(dias)

    # Lazo for para almacenar el consumo de potencia (MW)
    # a una hora específica a lo largo de los días dados.
    for d in range(dias):
        hora_x[d] = df['MW'].iloc[hora + 24*d]

    # Retorna tupla
    datos_hr = (hora_x, hora, dias)
    return datos_hr


def modelo_hora(datos_hora):
    '''Modelo probabilístico de mejor ajuste y sus parámetros.

    Para la distribución *(PDF)* de consumo de potencia
    a una hora particular, importa los datos y determina
    la curva de mejor ajuste por medio del paquete ``fitter``.

    Parameters
    ----------
    datos_hora : vector
        Arreglo de consumo de potencia de una hora
        particular del tamaño de los días especificados.

    Returns
    -------
    grafica : plot
        Conjunto de distribuciones de mejor ajuste.
    resumen : lista
        Resumen de las distribuciones de mejor ajuste.
    paramtrs : dict
        Diccionario con los parámetros de la distribución
        que mejor modela los datos proporcionados.

    '''
    # Usar método Fitter de la librería fitter
    plt.figure()
    fhr = Fitter(datos_hora)

    # Retornar tupla:
    return (fhr.fit(), fhr.summary(), fhr.get_best())


def estadisticas_hora(datos_hora):
    '''Momentos a partir de los datos.

    Usar los métodos de ``numpy`` y ``stats`` para
    determinar los momentos estadísticos: media, varianza,
    desviación estándar, inclinación y kurtosis;
    del conjunto de datos proporcionados.

    Parameters
    ----------
    datos_hora : vector
        Arreglo de consumo de potencia de una hora
        particular del tamaño de los días especificados.

    Returns
    -------
    stads : tupla
        Contiene los momentos de los datos datos en
        las posiciones respectivas:

        - [0] media.
        - [1] varianza.
        - [2] desviación estándar.
        - [3] kurtosis.

    '''
    # Obtener las estadísticas a partir de los datos.
    mn = np.mean(datos_hora)
    var = np.var(datos_hora)
    std = np.std(datos_hora)
    skw = stats.skew(datos_hora)
    kts = stats.kurtosis(datos_hora)

    # Retornar tupla que contiene las estadísticas
    stads = (mn, var, std, skw, kts)
    return stads


def visualizacion_hora(datos_hora):
    '''Histograma de demanda de potencia a una hora.

    Genera un histograma de la distribución datos brindados
    haciendo uso del método ``.hist()`` de ``pyplot``.

    Parameters
    ----------
    datos_hora : vector
        Arreglo de consumo de potencia de una hora
        particular del tamaño de los días especificados.

    Returns
    -------
    histograma : figura
        Histograma de la distribución de demanda de potencia [MW]
        a una hora particular definida por los datos.

    '''
    # Usar método hist de pyplot para vizualizar datos
    # a modo de histograma.
    plt.figure()
    plt.hist(datos_hora, bins=50, density=True, label='Consumo (MW)')

    # Información del gráfico
    plt.title('Demanda de potencia en [MW] a una hora particular')
    plt.xlabel('Potencia [MW]')
    plt.ylabel('Freq. Relativa')
    plt.legend()

    # Retornar la figura que contiene el histograma.
    return plt.show()
