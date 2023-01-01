"""Obtiene la base de datos, grafica de proceso y probabilidad.

Contiene todas las funciones necesarias para solicitar
la base de datos del servidor API del CENCE, analizar
una secuencia aleatoria, obtener su función de densidad
y asumiendo que la distribución es genlogistic generar
los parámetros de las distribuciones en el tiempo para
una gráfica 3D de la secuencia aleatoria.

"""
import pandas as pd      # Manipulación de datos
import numpy as np       # Manejo de arreglos
from scipy import stats
import matplotlib.pyplot as plt
# Paquete para el manejo de intercambio de datos.
import requests
import datetime
from datetime import timedelta

# -----
# 1. Función datos demanda:
# -----


def datos_demanda(dato_inicio, dato_fin, dias):
    """Solicita datos de potencia [MW] consumida.

    Directamente desde la página del CENCE, para las fechas entre
    los parámetros ``dato_inicio`` y ``dato_fin``, obtiene
    los datos de consumo, que se encuentran en formato JSon
    pero que python los convierte a un diccionario
    por el método ``.json()``; hasta la primera hora del
    último día inclusive. Luego ordena los datos de consumo por hora.

    Parameters
    ----------
    dato_inicio : cadena
        *e.g.* 20190101.
    dato_fin : cadena
        *e.g.* 20190102.
    dias : entero
        Total de días sobre los que se desea obtener el consumo
        a una hora particular, debe ser menor al lapso de fechas
        especificadas anteriormente.

    Returns
    -------
    df_hr : DataFrame
        Ordenado por hora. e.g el consumo a la hora 10
        a lo largo de 365 días (para todas las 24 horas).

    """

    # Construcción del url
    proto_url = "https://apps.grupoice.com/CenceWeb/data/sen/json/DemandaMW?"
    params = {"inicio": dato_inicio, "fin": dato_fin}
    # Hacer la solicitud GET y guardar un "Response" en la variable r
    r = requests.get(proto_url, params)

    # Extraer del dict que es devuelto por el método <.json()>,
    # los datos filtrando por la llave 'data'
    datos = r.json()['data']

    # Crear dataframe de pandas
    df = pd.DataFrame(datos)

    # Odenar DataFrame:

    # Horas del día
    h_0 = "2019-01-01 00:00:00.0"
    h_1 = "2019-01-01 01:00:00.0"
    h_2 = "2019-01-01 02:00:00.0"
    h_3 = "2019-01-01 03:00:00.0"
    h_4 = "2019-01-01 04:00:00.0"
    h_5 = "2019-01-01 05:00:00.0"
    h_6 = "2019-01-01 06:00:00.0"
    h_7 = "2019-01-01 07:00:00.0"
    h_8 = "2019-01-01 08:00:00.0"
    h_9 = "2019-01-01 09:00:00.0"
    h_10 = "2019-01-01 10:00:00.0"
    h_11 = "2019-01-01 11:00:00.0"
    h_12 = "2019-01-01 12:00:00.0"
    h_13 = "2019-01-01 13:00:00.0"
    h_14 = "2019-01-01 14:00:00.0"
    h_15 = "2019-01-01 15:00:00.0"
    h_16 = "2019-01-01 16:00:00.0"
    h_17 = "2019-01-01 17:00:00.0"
    h_18 = "2019-01-01 18:00:00.0"
    h_19 = "2019-01-01 19:00:00.0"
    h_20 = "2019-01-01 20:00:00.0"
    h_21 = "2019-01-01 21:00:00.0"
    h_22 = "2019-01-01 22:00:00.0"
    h_23 = "2019-01-01 23:00:00.0"

    # Selección de datos de columna
    dt_h_0 = df[df["fechaHora"] == h_0]
    dt_h_1 = df[df["fechaHora"] == h_1]
    dt_h_2 = df[df["fechaHora"] == h_2]
    dt_h_3 = df[df["fechaHora"] == h_3]
    dt_h_4 = df[df["fechaHora"] == h_4]
    dt_h_5 = df[df["fechaHora"] == h_5]
    dt_h_6 = df[df["fechaHora"] == h_6]
    dt_h_7 = df[df["fechaHora"] == h_7]
    dt_h_8 = df[df["fechaHora"] == h_8]
    dt_h_9 = df[df["fechaHora"] == h_9]
    dt_h_10 = df[df["fechaHora"] == h_10]
    dt_h_11 = df[df["fechaHora"] == h_11]
    dt_h_12 = df[df["fechaHora"] == h_12]
    dt_h_13 = df[df["fechaHora"] == h_13]
    dt_h_14 = df[df["fechaHora"] == h_14]
    dt_h_15 = df[df["fechaHora"] == h_15]
    dt_h_16 = df[df["fechaHora"] == h_16]
    dt_h_17 = df[df["fechaHora"] == h_17]
    dt_h_18 = df[df["fechaHora"] == h_18]
    dt_h_19 = df[df["fechaHora"] == h_19]
    dt_h_20 = df[df["fechaHora"] == h_20]
    dt_h_21 = df[df["fechaHora"] == h_21]
    dt_h_22 = df[df["fechaHora"] == h_22]
    dt_h_23 = df[df["fechaHora"] == h_23]

    # Creación de csv para manejo de datos extraídos
    dt_h_0.to_csv("dt_h_0.csv", index=False)
    dt_h_1.to_csv("dt_h_1.csv", index=False)
    dt_h_2.to_csv("dt_h_2.csv", index=False)
    dt_h_3.to_csv("dt_h_3.csv", index=False)
    dt_h_4.to_csv("dt_h_4.csv", index=False)
    dt_h_5.to_csv("dt_h_5.csv", index=False)
    dt_h_6.to_csv("dt_h_6.csv", index=False)
    dt_h_7.to_csv("dt_h_7.csv", index=False)
    dt_h_8.to_csv("dt_h_8.csv", index=False)
    dt_h_9.to_csv("dt_h_9.csv", index=False)
    dt_h_10.to_csv("dt_h_10.csv", index=False)
    dt_h_11.to_csv("dt_h_11.csv", index=False)
    dt_h_12.to_csv("dt_h_12.csv", index=False)
    dt_h_13.to_csv("dt_h_13.csv", index=False)
    dt_h_14.to_csv("dt_h_14.csv", index=False)
    dt_h_15.to_csv("dt_h_15.csv", index=False)
    dt_h_16.to_csv("dt_h_16.csv", index=False)
    dt_h_17.to_csv("dt_h_17.csv", index=False)
    dt_h_18.to_csv("dt_h_18.csv", index=False)
    dt_h_19.to_csv("dt_h_19.csv", index=False)
    dt_h_20.to_csv("dt_h_20.csv", index=False)
    dt_h_21.to_csv("dt_h_21.csv", index=False)
    dt_h_22.to_csv("dt_h_22.csv", index=False)
    dt_h_23.to_csv("dt_h_23.csv", index=False)

    # Fechas iniciales
    out_0 = datetime.datetime.strptime(h_0, "%Y-%m-%d %H:%M:%S.%f")
    out_1 = datetime.datetime.strptime(h_1, "%Y-%m-%d %H:%M:%S.%f")
    out_2 = datetime.datetime.strptime(h_2, "%Y-%m-%d %H:%M:%S.%f")
    out_3 = datetime.datetime.strptime(h_3, "%Y-%m-%d %H:%M:%S.%f")
    out_4 = datetime.datetime.strptime(h_4, "%Y-%m-%d %H:%M:%S.%f")
    out_5 = datetime.datetime.strptime(h_5, "%Y-%m-%d %H:%M:%S.%f")
    out_6 = datetime.datetime.strptime(h_6, "%Y-%m-%d %H:%M:%S.%f")
    out_7 = datetime.datetime.strptime(h_7, "%Y-%m-%d %H:%M:%S.%f")
    out_8 = datetime.datetime.strptime(h_8, "%Y-%m-%d %H:%M:%S.%f")
    out_9 = datetime.datetime.strptime(h_9, "%Y-%m-%d %H:%M:%S.%f")
    out_10 = datetime.datetime.strptime(h_10, "%Y-%m-%d %H:%M:%S.%f")
    out_11 = datetime.datetime.strptime(h_11, "%Y-%m-%d %H:%M:%S.%f")
    out_12 = datetime.datetime.strptime(h_12, "%Y-%m-%d %H:%M:%S.%f")
    out_13 = datetime.datetime.strptime(h_13, "%Y-%m-%d %H:%M:%S.%f")
    out_14 = datetime.datetime.strptime(h_14, "%Y-%m-%d %H:%M:%S.%f")
    out_15 = datetime.datetime.strptime(h_15, "%Y-%m-%d %H:%M:%S.%f")
    out_16 = datetime.datetime.strptime(h_16, "%Y-%m-%d %H:%M:%S.%f")
    out_17 = datetime.datetime.strptime(h_17, "%Y-%m-%d %H:%M:%S.%f")
    out_18 = datetime.datetime.strptime(h_18, "%Y-%m-%d %H:%M:%S.%f")
    out_19 = datetime.datetime.strptime(h_19, "%Y-%m-%d %H:%M:%S.%f")
    out_20 = datetime.datetime.strptime(h_20, "%Y-%m-%d %H:%M:%S.%f")
    out_21 = datetime.datetime.strptime(h_21, "%Y-%m-%d %H:%M:%S.%f")
    out_22 = datetime.datetime.strptime(h_22, "%Y-%m-%d %H:%M:%S.%f")
    out_23 = datetime.datetime.strptime(h_23, "%Y-%m-%d %H:%M:%S.%f")

    # Contador de bucle
    cont = 1     # comenzar desde 1 porque no hay dia cero.
    # Bucle para generación de csv con datos requeridos
    while cont < dias:

        # 00H
        out_plus_0 = out_0 + timedelta(cont)
        fechas_0 = out_plus_0.strftime("%Y-%m-%d %H:%M:%S.%f").rstrip("0")
        output_0 = fechas_0.ljust(1 + len(fechas_0), "0")
        dt_h_0 = df[df["fechaHora"] == output_0]
        dt_h_0.to_csv("dt_h_0.csv", mode='a',
                      header=False, index=False)

        # 01H
        out_plus_1 = out_1 + timedelta(cont)
        fechas_1 = out_plus_1.strftime("%Y-%m-%d %H:%M:%S.%f").rstrip("0")
        output_1 = fechas_1.ljust(1 + len(fechas_1), "0")
        dt_h_1 = df[df["fechaHora"] == output_1]
        dt_h_1.to_csv("dt_h_1.csv", mode='a',
                      header=False, index=False)

        # 02H
        out_plus_2 = out_2 + timedelta(cont)
        fechas_2 = out_plus_2.strftime("%Y-%m-%d %H:%M:%S.%f").rstrip("0")
        output_2 = fechas_2.ljust(1 + len(fechas_2), "0")
        dt_h_2 = df[df["fechaHora"] == output_2]
        dt_h_2.to_csv("dt_h_2.csv", mode='a',
                      header=False, index=False)

        # 03H
        out_plus_3 = out_3 + timedelta(cont)
        fechas_3 = out_plus_3.strftime("%Y-%m-%d %H:%M:%S.%f").rstrip("0")
        output_3 = fechas_3.ljust(1 + len(fechas_3), "0")
        dt_h_3 = df[df["fechaHora"] == output_3]
        dt_h_3.to_csv("dt_h_3.csv", mode='a',
                      header=False, index=False)

        # 04H
        out_plus_4 = out_4 + timedelta(cont)
        fechas_4 = out_plus_4.strftime("%Y-%m-%d %H:%M:%S.%f").rstrip("0")
        output_4 = fechas_4.ljust(1 + len(fechas_4), "0")
        dt_h_4 = df[df["fechaHora"] == output_4]
        dt_h_4.to_csv("dt_h_4.csv", mode='a',
                      header=False, index=False)

        # 05H
        out_plus_5 = out_5 + timedelta(cont)
        fechas_5 = out_plus_5.strftime("%Y-%m-%d %H:%M:%S.%f").rstrip("0")
        output_5 = fechas_5.ljust(1 + len(fechas_5), "0")
        dt_h_5 = df[df["fechaHora"] == output_5]
        dt_h_5.to_csv("dt_h_5.csv", mode='a',
                      header=False, index=False)

        # 06H
        out_plus_6 = out_6 + timedelta(cont)
        fechas_6 = out_plus_6.strftime("%Y-%m-%d %H:%M:%S.%f").rstrip("0")
        output_6 = fechas_6.ljust(1 + len(fechas_6), "0")
        dt_h_6 = df[df["fechaHora"] == output_6]
        dt_h_6.to_csv("dt_h_6.csv", mode='a',
                      header=False, index=False)

        # 07H
        out_plus_7 = out_7 + timedelta(cont)
        fechas_7 = out_plus_7.strftime("%Y-%m-%d %H:%M:%S.%f").rstrip("0")
        output_7 = fechas_7.ljust(1 + len(fechas_7), "0")
        dt_h_7 = df[df["fechaHora"] == output_7]
        dt_h_7.to_csv("dt_h_7.csv", mode='a',
                      header=False, index=False)

        # 08H
        out_plus_8 = out_8 + timedelta(cont)
        fechas_8 = out_plus_8.strftime("%Y-%m-%d %H:%M:%S.%f").rstrip("0")
        output_8 = fechas_8.ljust(1 + len(fechas_8), "0")
        dt_h_8 = df[df["fechaHora"] == output_8]
        dt_h_8.to_csv("dt_h_8.csv", mode='a',
                      header=False, index=False)

        # 9H
        out_plus_9 = out_9 + timedelta(cont)
        fechas_9 = out_plus_9.strftime("%Y-%m-%d %H:%M:%S.%f").rstrip("0")
        output_9 = fechas_9.ljust(1 + len(fechas_9), "0")
        dt_h_9 = df[df["fechaHora"] == output_9]
        dt_h_9.to_csv("dt_h_9.csv", mode='a',
                      header=False, index=False)

        # 10H
        out_plus_10 = out_10 + timedelta(cont)
        fechas_10 = out_plus_10.strftime("%Y-%m-%d %H:%M:%S.%f").rstrip("0")
        output_10 = fechas_10.ljust(1 + len(fechas_10), "0")
        dt_h_10 = df[df["fechaHora"] == output_10]
        dt_h_10.to_csv("dt_h_10.csv", mode='a',
                       header=False, index=False)

        # 11H
        out_plus_11 = out_11 + timedelta(cont)
        fechas_11 = out_plus_11.strftime("%Y-%m-%d %H:%M:%S.%f").rstrip("0")
        output_11 = fechas_11.ljust(1 + len(fechas_11), "0")
        dt_h_11 = df[df["fechaHora"] == output_11]
        dt_h_11.to_csv("dt_h_11.csv", mode='a',
                       header=False, index=False)

        # 12H
        out_plus_12 = out_12 + timedelta(cont)
        fechas_12 = out_plus_12.strftime("%Y-%m-%d %H:%M:%S.%f").rstrip("0")
        output_12 = fechas_12.ljust(1 + len(fechas_12), "0")
        dt_h_12 = df[df["fechaHora"] == output_12]
        dt_h_12.to_csv("dt_h_12.csv", mode='a',
                       header=False, index=False)

        # 13H
        out_plus_13 = out_13 + timedelta(cont)
        fechas_13 = out_plus_13.strftime("%Y-%m-%d %H:%M:%S.%f").rstrip("0")
        output_13 = fechas_13.ljust(1 + len(fechas_13), "0")
        dt_h_13 = df[df["fechaHora"] == output_13]
        dt_h_13.to_csv("dt_h_13.csv", mode='a',
                       header=False, index=False)

        # 14H
        out_plus_14 = out_14 + timedelta(cont)
        fechas_14 = out_plus_14.strftime("%Y-%m-%d %H:%M:%S.%f").rstrip("0")
        output_14 = fechas_14.ljust(1 + len(fechas_14), "0")
        dt_h_14 = df[df["fechaHora"] == output_14]
        dt_h_14.to_csv("dt_h_14.csv", mode='a',
                       header=False, index=False)

        # 15H
        out_plus_15 = out_15 + timedelta(cont)
        fechas_15 = out_plus_15.strftime("%Y-%m-%d %H:%M:%S.%f").rstrip("0")
        output_15 = fechas_15.ljust(1 + len(fechas_15), "0")
        dt_h_15 = df[df["fechaHora"] == output_15]
        dt_h_15.to_csv("dt_h_15.csv", mode='a',
                       header=False, index=False)

        # 16H
        out_plus_16 = out_16 + timedelta(cont)
        fechas_16 = out_plus_16.strftime("%Y-%m-%d %H:%M:%S.%f").rstrip("0")
        output_16 = fechas_16.ljust(1 + len(fechas_16), "0")
        dt_h_16 = df[df["fechaHora"] == output_16]
        dt_h_16.to_csv("dt_h_16.csv", mode='a',
                       header=False, index=False)

        # 17H
        out_plus_17 = out_17 + timedelta(cont)
        fechas_17 = out_plus_17.strftime("%Y-%m-%d %H:%M:%S.%f").rstrip("0")
        output_17 = fechas_17.ljust(1 + len(fechas_17), "0")
        dt_h_17 = df[df["fechaHora"] == output_17]
        dt_h_17.to_csv("dt_h_17.csv", mode='a',
                       header=False, index=False)

        # 18H
        out_plus_18 = out_18 + timedelta(cont)
        fechas_18 = out_plus_18.strftime("%Y-%m-%d %H:%M:%S.%f").rstrip("0")
        output_18 = fechas_18.ljust(1 + len(fechas_18), "0")
        dt_h_18 = df[df["fechaHora"] == output_18]
        dt_h_18.to_csv("dt_h_18.csv", mode='a',
                       header=False, index=False)

        # 19H
        out_plus_19 = out_19 + timedelta(cont)
        fechas_19 = out_plus_19.strftime("%Y-%m-%d %H:%M:%S.%f").rstrip("0")
        output_19 = fechas_19.ljust(1 + len(fechas_19), "0")
        dt_h_19 = df[df["fechaHora"] == output_19]
        dt_h_19.to_csv("dt_h_19.csv", mode='a',
                       header=False, index=False)

        # 20H
        out_plus_20 = out_20 + timedelta(cont)
        fechas_20 = out_plus_20.strftime("%Y-%m-%d %H:%M:%S.%f").rstrip("0")
        output_20 = fechas_20.ljust(1 + len(fechas_20), "0")
        dt_h_20 = df[df["fechaHora"] == output_20]
        dt_h_20.to_csv("dt_h_20.csv", mode='a',
                       header=False, index=False)

        # 21H
        out_plus_21 = out_21 + timedelta(cont)
        fechas_21 = out_plus_21.strftime("%Y-%m-%d %H:%M:%S.%f").rstrip("0")
        output_21 = fechas_21.ljust(1 + len(fechas_21), "0")
        dt_h_21 = df[df["fechaHora"] == output_21]
        dt_h_21.to_csv("dt_h_21.csv", mode='a',
                       header=False, index=False)

        # 22H
        out_plus_22 = out_22 + timedelta(cont)
        fechas_22 = out_plus_22.strftime("%Y-%m-%d %H:%M:%S.%f").rstrip("0")
        output_22 = fechas_22.ljust(1 + len(fechas_22), "0")
        dt_h_22 = df[df["fechaHora"] == output_22]
        dt_h_22.to_csv("dt_h_22.csv", mode='a',
                       header=False, index=False)

        # 23H
        out_plus_23 = out_23 + timedelta(cont)
        fechas_23 = out_plus_23.strftime("%Y-%m-%d %H:%M:%S.%f").rstrip("0")
        output_23 = fechas_23.ljust(1 + len(fechas_23), "0")
        dt_h_23 = df[df["fechaHora"] == output_23]
        dt_h_23.to_csv("dt_h_23.csv", mode='a',
                       header=False, index=False)

        cont += 1
        if cont == dias:
            break

    # Subir los datos de consumo ordenados por hora.
    # Dataframe 00H
    dfh_0 = pd.read_csv("dt_h_0.csv")

    # Dataframe 01H
    dfh_1 = pd.read_csv("dt_h_1.csv")

    # Dataframe 02H
    dfh_2 = pd.read_csv("dt_h_2.csv")

    # Dataframe 03H
    dfh_3 = pd.read_csv("dt_h_3.csv")

    # Dataframe 04H
    dfh_4 = pd.read_csv("dt_h_4.csv")

    # Dataframe 05H
    dfh_5 = pd.read_csv("dt_h_5.csv")

    # Dataframe 06H
    dfh_6 = pd.read_csv("dt_h_6.csv")

    # Dataframe 07H
    dfh_7 = pd.read_csv("dt_h_7.csv")

    # Dataframe 08H
    dfh_8 = pd.read_csv("dt_h_8.csv")

    # Dataframe 09H
    dfh_9 = pd.read_csv("dt_h_9.csv")

    # Dataframe 10H
    dfh_10 = pd.read_csv("dt_h_10.csv")

    # Dataframe 11H
    dfh_11 = pd.read_csv("dt_h_11.csv")

    # Dataframe 12H
    dfh_12 = pd.read_csv("dt_h_12.csv")

    # Dataframe 13H
    dfh_13 = pd.read_csv("dt_h_13.csv")

    # Dataframe 14H
    dfh_14 = pd.read_csv("dt_h_14.csv")

    # Dataframe 15H
    dfh_15 = pd.read_csv("dt_h_15.csv")

    # Dataframe 16H
    dfh_16 = pd.read_csv("dt_h_16.csv")

    # Dataframe 17H
    dfh_17 = pd.read_csv("dt_h_17.csv")

    # Dataframe 18H
    dfh_18 = pd.read_csv("dt_h_18.csv")

    # Dataframe 19H
    dfh_19 = pd.read_csv("dt_h_19.csv")

    # Dataframe 20H
    dfh_20 = pd.read_csv("dt_h_20.csv")

    # Dataframe 21H
    dfh_21 = pd.read_csv("dt_h_21.csv")

    # Dataframe 22H
    dfh_22 = pd.read_csv("dt_h_22.csv")

    # Dataframe 23H
    dfh_23 = pd.read_csv("dt_h_23.csv")

    # Lista de Dataframe's:
    frame = [dfh_0, dfh_1, dfh_2, dfh_3, dfh_4, dfh_5, dfh_6,
             dfh_7, dfh_8, dfh_9, dfh_10, dfh_11, dfh_12, dfh_13,
             dfh_14, dfh_15, dfh_16, dfh_17, dfh_18, dfh_19, dfh_20,
             dfh_21, dfh_22, dfh_23]

    # Concatenarlos
    df_hr = pd.concat(frame)
    return df_hr

# -----
# 2. Consumo a una hora específica
# -----


def datos_hora(hora, dias, df_hr):
    """Obtener los datos de consumo de potencia de una hora particular.

    La hora va de 0 - 24 (exclusivo) a lo largo de todo
    el período de días especificados.

    Parameters
    ----------
    hora : entero
        e.g. de 0 a 24 (exclusivo).
    dias : entero
        Periodo de días deseados.
    df_hr : DataFrame
        Ya ordenado por horas.

    Returns
    -------
    datos_hr : tupla
        Tupla que contiene un arreglo, la hora y el día dados, cuyas
        posiciones son:

        - [0] Vector de consumo de potencia a una hora específica.
        - [1] Hora especificada.
        - [2] Cantidad de días seleccionados.

    """
    # Crear vector vacío de la hora específica
    # del tamaño de los días seleccionados.

    hora_x = np.empty(dias)

    # Almacenar el consumo de potencia (MW)
    # a una hora específica a lo largo de los días dados.
    init = dias * hora
    final = init + dias
    hora_x[:] = df_hr['MW'].iloc[init:final]

    # Retorna tupla de tamaño tres:
    datos_hr = (hora_x, hora, dias)
    return datos_hr

# -----
# 3. Consumo de potencia a cada hora
# -----


def demanda(horas, dias, df_hr):
    """Arreglo de muestras.

    Llama la función :py:func:`proceso.proceso.datos_hora` para cada hora
    y almacena en una matriz el consumo de potencia
    a dichas horas, donde las filas corresponden a los días
    (registros) y las columnas a las horas (campos).
    Retorna una matriz de datos de tamaño (dias, horas)
    donde ``dias`` es la cantidad de días sobre los que se desea
    requistrar los datos de la hora particular, debe ser
    menor o igual a la cantidad de días disponibles en la base
    de datos ``df_hr`` disponible y ``horas`` es la cantidad de horas
    al día empezando desde la hora cero (0) y termina en la hora 24
    (exlusivo) *e.g* si horas = 24 se refiere a un día.

    Parameters
    ----------
    horas : entero
        horas deseadas de 0 a 24 (exlusivo).
    dias : entero
        Se asumirá que 365 días corresponden a un año.
    df_hr : DataFrame
        Base de datos de la que se dispone.

    Returns
    -------
    pw_dia : ndarray
        Matriz con los datos de consumo de
        potencia (filas) a cada hora (columnas).

    """
    # Matriz de consumo a cada hora durante un día
    pw_dia = np.empty((dias, horas))

    # Almacenar el consumo a lo largo de las horas del día
    for hr in range(horas):
        # Llamar función datos_hora()
        pw_dia[:, hr], _, _ = datos_hora(hr, dias, df_hr)

    # Retorna matriz de datos de consumo cada hora
    # a lo largo de todos los días especificados.
    return pw_dia

# -----
# 4. Modelo de parámetros
# -----


def parametros(datos_hrs, hrs):
    r"""Parámetros de la distribución de consumo de cada hora.

    Se define una distribución **genlogistic** para el consumo por hora
    (seleccionada por la experiencia de demanda de electricidad
    a una hora particular en Costa Rica). La función determina los distintos
    parámetros que modelan la distribución de consumo según
    la hora a partir de los datos de consumo a lo largo de los días.
    Su PDF, en forma estándar, se define:

    .. math:: f_{X}(x) = c\frac{e^{-x}}{(1+e^{-x})^{c+1}}

    Sea :math:`L` para ``loc`` y :math:`S` para ``scale``
    estandarizar mediante:

    .. math:: f_{X}\left(x; c, L, S\right) = \frac{1}{S}f_{X}\left(\frac{\left( x - L \right)}{S} \right)

    donde :math:`x \geqslant , c > 0`.

    Donde los parámetros :math`c, L, S`: varían según la hora.

    Parameters
    ----------
    datos_hrs : ndarray
        Datos de consumo de potencia [MW] con registro a lo
        largo del los días (fila) y campo
        para cada hora (columna).
    hrs : entero
        Cantidad de horas dadas (0-24 exclusivo) partiendo
        desde la hora cero. *e. g* si hrs = 3 se toman
        las horas: 0, 1, 2.

    Returns
    -------
    parmtrs : ndarray
        Arreglo de parámetros de la distribución genlogistic
        para las distintas horas. Donde las filas corresponden
        a las horas y las columnas cada uno de los parámetros
        encontrados: c | loc | scale.
    
    """
    # Para encontrar la cantidad de parámetros
    # que devuelve una distribución genlogistic,
    # se generan datos aleatorios con distribución genlogistic.
    gmm = stats.genlogistic.fit(np.random.randn(100))
    num_parmtrs = len(gmm)

    # Arreglo vacío de los parámetros por hora a lo largo del día
    # Donde las filas son las horas y las columnas
    # los respectivos parámetros: c, loc, scale
    parmtrs = np.empty((hrs, num_parmtrs))
    for pw in range(hrs):
        parmtrs[pw, :] = stats.genlogistic.fit(datos_hrs[:, pw])
    return parmtrs


def modelo_parmtrs(parmtrs_data, polyn):
    """Modelo polinómico de los parámetros como función del tiempo.

    Encuentra un polinomio para cada parámetro en función del tiempo
    de orden máximo polyn = 10 que modelan la evolución de las distribuciones
    *e.g:* [model_a(t), model_loc(t), model_scale(t)].

    Parameters
    ----------
    parmtrs_datos : ndarray
        Matriz de parámetros obtenidos a partir de los datos reales.
    polyn : Entero.
        Orden del modelo se fija hasta 10 (inclusivo)
        por ser suficiente.

    Returns
    -------
    prm_l : lista
        Lista que contiene el modelo polinómico de cada parámetro
        en función del tiempo (continuo).
    polyn : entero
        Orden del polinomio dado que modela los parámetros.

    """
    while (polyn < 0) or (polyn > 10):
        polyn = int(input('Introduzaca un valor válido (entre 0-10): '))

    # Definir la dimenciones del arreglo de parámetros:
    hr, pr = np.shape(parmtrs_data)

    # Crear lista vacía para almacenar los modelos de cada parámetro:
    prm_l = []

    # Horas como soporte
    t = range(hr)

    # Lazo for para generar los modelos de cada parámetro
    for prs in range(pr):
        # Optener función polinomial a partir de los datos
        mdls_parmtrs = np.polynomial.polynomial.Polynomial.fit(
            t, parmtrs_data[:, prs], polyn)
        # Agregar a la lista el modelo encontrado
        prm_l.append(mdls_parmtrs)

    return (prm_l, polyn)

# -----
# 5. Graficar modelos de parámetros
# -----


def plot_parmtrs(parmtrs_datos, mdls_parmtrs, hrs, n):
    """Grafica comparativa entre parámetros reales y aproximados.

    Grafica a(t), loc(t), scale(t) obtenidos con la función
    :py:func:`proceso.proceso.modelo_parmtrs` y los parámetros reales tomados
    a partir de los datos.

    Parameters
    ----------
    parmtrs_datos : ndarray
        Matriz de parámetros de los datos reales de cada hora.
    mdls_parmtrs : lista
        Modelo continuo aproximado en función del tiempo.
    hrs : entero
        Soporte del tiempo (discreto) para cada hora.
    n : entero
        Orden del modelo ingresado

    Returns
    -------
    figura : plot
        Gráfica comparativa del modelo aprox. de parámetros
        en función del tiempo como función polinómica continua.
        Y los datos de parámetros reales como puntos.

    """
    # Dominio del soporte
    t = np.linspace(0, hrs, 100)

    lbl = ['c', 'loc', 'scale']
    # Graficar
    for gr in range(3):
        # número de figuras
        fg = gr + 1

        # Tamaño figuras
        plt.figure(fg, figsize=(5, 4))
        # Gráfica por medio del modelo
        plt.plot(t, mdls_parmtrs[gr](t), 'r-', label=lbl[gr])
        # Gráfica de Datos
        plt.scatter(list(range(hrs)), parmtrs_datos[:, gr], c='b')
        # Información gráficos
        plt.title('Modelo Parámetros orden n={}'.format(n))
        plt.xlabel('Hora')
        plt.ylabel('Magnitud')
        plt.legend()
        # Guardar figuras:
        # if gr == 0:
        #     plt.savefig('figs/pfig_1.svg')
        # elif gr == 1:
        #     plt.savefig('figs/pfig_2.svg')
        # elif gr == 2:
        #     plt.savefig('figs/pfig_3.svg')

    return plt.show()


def plotpdf_datos_modelo(parmtrs_datos, mdls_parmtrs, pic):
    """Compara las distribuciones resultantes.

    Para un instante (hora específica) dado genera
    gráfica de la distribución
    genlogistic con parámetros aproximados del modelo continuo
    y parámetros reales discretos.

    Parameters
    ----------
    parmtrs_datos : ndarray
        Matriz de parámetros de los datos reales de cada hora.
    mdls_parmtrs : 
        Modelo continuo aproximado en función del tiempo.
    pic : entero
        Instante de tiempo. La hora dada.

    Returns
    -------
    figura : plot
        Gráfica comparativa de la distribución obtenida con
        los parámetros de los datos reales y con los
        modelos polinómicos continuos aproximados.
    
    """
    while (pic < 0) or (pic >= 24):
        pic = int(input('Ingrese un instante de tiempo válido: '))

    # Tamaño de la figura
    plt.figure(4, figsize=(4, 3))
    # Distribución a partir de los datos:
    # Parámetros a una hora particular
    a_hr = parmtrs_datos[pic, 0]
    l_hr = parmtrs_datos[pic, 1]
    scl_hr = parmtrs_datos[pic, 2]
    # Distribución con parámetros reales:
    rv_real = stats.genlogistic(a_hr, l_hr, scl_hr)

    # Distribución a partir del modelo:
    # Se llama la función densidad evaluando los parámetros
    # en un instante de tiempo dado.
    # Desempacar modelos
    a_t = mdls_parmtrs[0]
    lc_t = mdls_parmtrs[1]
    scl_t = mdls_parmtrs[2]

    # Distribución con parámetros aproximados.
    # evaluando los parámetros en el tiempo dado.
    rv_aprox = stats.genlogistic(a_t(pic), lc_t(pic), scl_t(pic))

    # Límites de soporte
    inf = 500
    sup = 2000

    # Soporte
    x = np.linspace(inf, sup, 100)

    # Graficar:
    # Gráfica con datos reales:
    plt.plot(x, rv_real.pdf(x), label='pdf real')
    # Gráfica con datos aproximados:
    plt.plot(x, rv_aprox.pdf(x), label='pdf aprox.')

    # Información de la gráfica
    plt.legend()
    plt.title('Distribución en el instante {}:00'.format(pic))
    plt.xlabel('Potencia [MW]')
    plt.ylabel('$f_{P}(p)$')
    return plt.show()

# -----
# 6. PDF de la secuencia aleatoria
# -----


def densidad(parmtrs_datos, taxi, taxf):
    """Conjunto de distribuciones que describen la secuencia aleatoria.

    Dados los parámetros en el tiempo discreto,
    retorna una lista con tantas pdf's de consumo de potencia
    como horas evaluadas (24hrs: 0-23).

    Parameters
    ----------
    parmtrs_datos : ndarray
        Matriz de parámetros de los datos reales de cada hora.
    taxi : entero
        Hora inicial. Límite inferior
        del dominio del tiempo. Inclusivo.
    taxf : entero
        Hora final. Límite superior
        del dominio del tiempo. Exclusivo.

    Returns
    -------
    distr_t : lista
        Contiene todas las pdf's genlogistic generadas con cada parámetro
        evaluado en cada hora.
    rango : tupla
        Contiene el intevalo del dominio del tiempo (soporte).
        que se usa en la función :py:func:`proceso.proceso.plot_p_hora`
        si se quisiera graficar la **PDF** específica en un tiempo particular
        dentro de éste dominio.

    """
    # Dominio en el tiempo:
    deltat = 0
    while deltat <= 0:
        while (taxi < 0) or (taxi > 24):
            taxi = int(input('Ingrese una hora inicial válida: '))
        while (taxf < 0) or (taxf > 24):
            taxf = int(input('Ingrese una hora final válida: '))
        deltat = taxf - taxi
        if (deltat <= 0):
            print('La hora inical debe ser menor a la final')

    # Lista de distribuciones a lo largo del tiempo discreto
    distr_t = []

    # Lazo for para almacenar todas las distribuciones
    # con parámetros evaluados en el tiempo
    for pmt in range(taxi, taxf, 1):
        # Extraer parámetros del arreglo
        als = parmtrs_datos[pmt, :]
        # Generar distribuciones
        distt = stats.genlogistic(als[0], als[1], als[2])
        # Almacenar distribuciones
        distr_t.append(distt)
    rango = (taxi, taxf)
    return (distr_t, rango)


def plot_p_hora(distr_t, rango, hora):
    """Grafica del proceso aleatorio en un instante.

    A partir de los parámetros reales donde el parámetro
    'hora' es el instante donde se desea evaluar la distribución
    del consumo de potencia.

    Parameters
    ----------
    distr_t : lista 
        Lista de distribuciones. Se pueden generar con la función
        :py:func:`proceso.proceso.densidad` y usada como
        argumento en ésta función.
    rango : tupla
        Contiene los límites de soporte definidos en la función
        :py:func:`proceso.proceso.densidad`
    hora : entero
        Hora específica a evaluar entre 0-24 (exclusivo)

    Returns
    -------
    figura : plot
        **PDF** específica en un tiempo particular
        dentro del rango de horas (dominio de soporte).

    """
    # Rango de horas definidos en la función densidad()
    (taxi, taxf) = rango

    # Número total de distribuciones
    deltat = taxf - taxi

    # Verificar hora válida:
    while (hora < 0) or (hora >= 24):
        print('El día sólo tiene 24 horas (0-23) inclusivo')
        hora = int(input('Ingrese una hora del día válida: '))

    while not (taxi <= hora < taxf):
        print('La hora ingresada está fuera del rango definido.')
        hora = int(input('Ingrese una hora entre {} y {}: '
                         .format(taxi, taxf)))

    # Graficar la pdf como función de la potencia consumida:
    # Límites del dominio de la potencia:
    lim_inf = 500
    lim_sup = 2000

    pw = np.linspace(lim_inf, lim_sup, 100)

    plt.figure(5, figsize=(4, 3))
    plt.plot(pw, (1/deltat)*distr_t[hora].pdf(pw), label=('pdf'))
    # Nota: La pdf se divide entre el número total de distribuciones
    # por ser una pdf(x, y) y el volumen bajo la superficie es uno.

    # Información de la gráfica
    plt.title('Distribución de potencia a las {}:00 horas'.format(hora))
    plt.legend()
    plt.xlabel('Porencia [MW]')
    plt.ylabel('$f_{P}$(p)')
    return plt.show()

# -----
# 7. Gráfica 3D del proceso aleatorio
# -----


def grafica(distr_t, rango):
    """Grafica 3D de la secuencia aleatoria.

    Se definen los ejes x: Periodo de horas (discreto)
    y: Consumo de potencia (continuo) y z: pdf del proceso.

    Parameters
    ----------
    distr_t : lista 
        Lista de distribuciones. Se pueden generar con la función
        :py:func:`proceso.proceso.densidad` y usada como
        argumento en ésta función.
    rango : tupla
        Contiene los límites de soporte definidos en la función
        :py:func:`proceso.proceso.densidad`

    Returns
    -------
    figura : plot
        Gráfica 3D de la secuencia aleatoria.

    """
    # Rango de horas definidos en la función densidad()
    (taxi, taxf) = rango

    # Número total de distribuciones
    deltat = taxf - taxi

    # Número y tamaño de figura
    plt.figure(4, figsize=(5, 6))

    # Proyección en 3d por el comando:
    ax = plt.axes(projection='3d')

    # Definir los ejes (soportes)

    # Potencia
    lim_i = 500
    lim_f = 2000
    pw = np.linspace(lim_i, lim_f, 100)

    # Tiempo
    for t in range(deltat):
        # Graficar
        # función de densidad tridimencional
        z = (1/deltat)*distr_t[t].pdf(pw)
        # Nota: La pdf se divide entre el número total de distribuciones
        # por ser una pdf(x, y) y el volumen bajo la superficie es uno.
        ax.plot3D(pw, z, t, 'green')
    # Información gráfica
    # ax.set_title('Secuencia aleatoria $P(t)$')
    ax.set_xlabel('Potencia [MW]')
    ax.set_ylabel('$f_{P}$(p, t)')
    ax.set_zlabel('Tiempo [hr]')

    # Guardar figura
    # plt.savefig('figs/p3D.svg')
    return plt.show()

# -----
# 8. Probabilidad
# -----


def probabilidad(distr_t, C, T):
    """Encuentra la probabilidad de ocurrencia de un valor.

    Para un consumo :math:`p_{1} < P < p_{2}` en el
    tiempo :math:`t_{1} < T < t_{2}` de la secuencia
    aleatoria :math:`P(t)`.

    Parameters
    ----------
    distr_t : lista 
        Lista de distribuciones. Se pueden generar con la función
        :py:func:`proceso.proceso.densidad` y usada como
        argumento en ésta función.
    C : tupla
        Intervalo de potencia consumida
        dónde se desea conocer la probabilidad de ocurrencia
    T : tupla
        Intervalo de tiempo dónde se desea calcular la probabilidad.

    Returns
    -------
    prbblty_t : flotante
        Suma de las probabilidades de cada distribución
        en el rango definido.

    """
    # Desempaquetar tupla con valores límites.
    (c1, c2) = C
    (t1, t2) = T

    # Verificar que el intervalo se ingresó correctamente:
    while (t1 > t2):
        print('El límite inferior debe ser menor al superior.')
        t1 = int(input('Ingrese hora inicial: '))
        t2 = int(input('Ingrese hora final: '))

    # Número total de distribuciones
    deltat = t2 - t1

    # Lista vacía de probabilidad por hora
    prbblty = []

    # Lazo for para generar todas las probabilidades cada hora
    for ndis in range(t1, t2, 1):
        # Usar método .cdf para la Función de Probabilidad Acumulativa
        prb = (1/deltat)*(distr_t[ndis].cdf(c2) - distr_t[ndis].cdf(c1))
        prbblty.append(prb)
        # Nota: se divide entre deltat por ser la candidad de distribuciones
        # en el rango definido.
    
    prbblty_t = sum(prbblty)
    return prbblty_t
