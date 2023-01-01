"""Revision de la funcionalidad del paquete `consumo`.

Aquí se llaman todas las funciones de los módulos del paquete para
verificar sus resultados.

Secciones:

    - *A. Potencia*: Importa los datos y analiza el modelo
      probabilístico de una hora particular del día.
    - *B. Correlación*: Obtiene los datos de dos horas diferentes
      que son consideradas como dos variables aleatorias para
      un posterior análisis de su correlación (grado de linealidad).
      Además se muesta un histograma bivariado de ambas
      variables aleatorias.
    - *C. Energía*: Se obtiene la energía a partir de la potencia
      consumida para análisis de su modelo semanal y, por teorema
      de límite central, determinar la distribución (PDF) de
      demanda de energía anual
      así como sus parámetros respectivos.

"""
from consumo import potencia, correlacion,  energia
# -------------------
# SECCION A: Potencia
# -------------------

# 1. Función datos demanda:

# Crear objecto df (DataFrame)
df = potencia.datos_demanda('demandaMW_2019.json')

# 2. Consumo a una hora específica

# Datos de consumo a lo largo de 365 días a una hora arbitraria
hr = 19
dias = 365
data_hora, _, _ = potencia.datos_hora(hr, dias, df)

# 3. Modelo probabilístico y distribución
# de consumo de potencia a la hora especificada.

# Con los datos obtenidos en la función anterior
# Mostrar mejores distribuciones (PDF):
modelo = potencia.modelo_hora(data_hora)

# Mostrar al usuario el modelo y distribución de mejor ajuste
# así como sus parámetros.
print(('Parámetros de distribución que modelan el consumo'),
      ('de potencia a las {}:00 horas es: '.format(hr)),
      (modelo[2]))

# 4. Estadísticas del mejor modelo de consumo de potencia
# a la hora especificada.

mmts = potencia.estadisticas_hora(data_hora)
print('\n ** Principales Estadísticas: ** \n')
print('\t Media: {:0.4f}'.format(mmts[0]))
print('\t Varianza: {:0.4f}'.format(mmts[1]))
print('\t Desviación estándar: {:0.4f}'.format(mmts[2]))
print('\t Inclinación: {:0.4f}'.format(mmts[3]))
print('\t Kurtosis: {:0.4f}'.format(mmts[4]))

# 5. Gráfica de histograma de consumo de potencia
# a la hora especificada.
potencia.visualizacion_hora(data_hora)

# ----------------------
# SECCIÓN B: Correlación
# ----------------------

# 6. Coeficiente de correlación (de Pearson)
# entre dos horas específicas e.g. 18:00 y 10:00
# a lo largo de un periodo de días deseado 365.
H_x = 18
H_y = 10
n_dias = 365
data_horas, r = correlacion.correlacion_horas(H_x, H_y, n_dias, df)

# Mostrar coeficiente
print(
    ('\nEl coeficiente de correlación (de Pearson)'),
    ('es\t: {:0.4f} \n'.format(r)))

# 7. Graficar histograma bivariado

# Llamar función, usar como argumentos los campos (columnas)
# del arreglo de los datos de consumo a las dos horas dadas,
# creado en la función anterior: data_horas
correlacion.visualizacion_horas(data_horas[:, 0], data_horas[:, 1])

# ------------------
# SECCIÓN C: Energía
# ------------------

# 8. Energía (MJ) total consumida por semanas

# Definir número de semanas.
wk = 52

# Mostrar el total de energía eléctrica demandada
# hasta la semana requerida
print('\nEnergia total en [MJ] a lo largo de {} semanas'.format(wk))
print('es: {:0.4f}'.format(energia.energia_semanal(wk, df)))

# 9. Modelo probabilístico y distribución
# de consumo de energía (MJ) semanal.

# Mostrar la distribución y el modelo con los parámetros de mejor ajuste:
print(('El modelo y parámetros de distribución de consumo'),
      ('de energía a la semana es: \n'),
      ('\t', energia.modelo_energia_semanal(wk, df)[2]))

# 10. Modelo probabilístico y distribución
# de consumo de energía (MJ) al año.

# Llamar función con argumento de 52 semanas, es decir un año:
total_sem = 52
_, media, stand, = energia.modelo_energia_anual(total_sem)

# Mostrar los parámetros de la distribución Normal:
print(
    ('La distribución normal de consumo anual [MJ] tiene como parámetros:\n'),
    ('\t media: {:0.4f}\n').format(media),
    ('\t desviación estándar: {:0.4f}').format(stand))
