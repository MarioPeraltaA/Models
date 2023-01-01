"""Aquí se verfican todos los módulos del paquete proceso.

Módulos: proceso, momentos, estacionaridad y espectro.
Secciones:

    - A: Función de densidad de probabilidad
    - B: Momentos
    - C: Estacionaridad
    - D: Características espectrales

"""
from proceso import proceso, momentos, estacionaridad, espectro
import numpy as np

# -----
# SECCIÓN A: Función de densidad de probabilidad
# -----

# 0. Datos de demanda de potencia

# Preguntar al usuario el periodo deseado:
inicial = input('Ingrese la fecha inicial: ')
final = input('Ingrese la fecha final: ')
# Solicitar al usuario el periodo en días
num_dias = input('Cantidad de días para el consumo a una hora particular: ')
n_d = int(num_dias)

# Crear objecto df (DataFrame)
df = proceso.datos_demanda(inicial, final, n_d)

# Solicitar horas al día
hrs = int(input('Cantidad de horas del día (24hrs): '))

# Verificar dato ingresado es correcto
while (hrs < 0) or (hrs > 24):
    print('El argumento del parámetros *horas debe estar entre 0 y 24.')
    hrs = int(input('Ingrese un argumento válido: '))

# Llamar función demanda()
secuencia_datos = proceso.demanda(hrs, n_d, df)

# Obtener parámetros a lo largo del tiempo.
parmtrs_datos = proceso.parametros(secuencia_datos, hrs)

# Llamar función para encontrar los modelos
# de los parámetros como función del tiempo.
polyn = int(input('Introduzca el orden del modelo deseado (0-10): '))
mdls_parmtrs, _ = proceso.modelo_parmtrs(parmtrs_datos, polyn)

# Graficar los parámetros reales así como sus modelos
proceso.plot_parmtrs(parmtrs_datos, mdls_parmtrs, hrs, polyn)

# Graficar la distribución resultante
# usando modelo real y aproximado:
print('Digite la hora (0-23) para la que desea comparar pdf resultante')
print('con los datos reales y con el modelo aprox de parámetros.')
pic = int(input('Comparar distribuciones a la hora: '))
proceso.plotpdf_datos_modelo(parmtrs_datos, mdls_parmtrs, pic)

# 1. Función de densidad del proceso aleatorio
# Definir dominio del tiempo de la función de densidad del proceso
# Se recomienda un día entero: 0 a 24 hrs (exclusivo).
taxi = int(input('Ingrese una hora inicial del soporte (0): '))
taxf = int(input('Ingrese una hora final del soporte (24): '))
distr_t, rango = proceso.densidad(parmtrs_datos, taxi, taxf)

# Graficar en el rango especificado en la función <desidad()>
hora = int(input('Ingrese una hora dentro del rango establecido: '))
proceso.plot_p_hora(distr_t, rango, hora)

# 2. Gráfica 3D de la secuencia aleatoria
proceso.grafica(distr_t, rango)

# 3. Probabilidad de tener un consumo c1 < C < c2 en t1 < T < t2

# Definir en una tupla los límites del intervalo C: c1 y c2
C = (800, 900)

# Definir en una tupla los límites del intervalo T: t1 y t2
T = (7, 11)

# Llamar función probabilidad
prbblty = proceso.probabilidad(distr_t, C, T)

print('La probabilidad (en porcentaje) es: {:0.4%}.'.format(prbblty))

# -----
# SECCIÓN B: Momentos
# -----
# 4. Autocorrelación

# Verificar la autocorrelación entre las horas: 7:00am y 11:00am
Rxx, _ = momentos.momentos(7, 11, secuencia_datos)
print('La autocorrelación Rxx es: {:0.4f}'.format(Rxx))

# 5. Autocovarianza

# Verificar la autocovarianza entre las horas: 7:00am y 11:00am
_, Cxx = momentos.momentos(7, 11, secuencia_datos)
print('La autocovarianza Cxx es: {:0.4f}'.format(Cxx))

# -----
# SECCIÓN C: Estacionaridad
# -----

# 6. Estacionaridad en sentido amplio
# Identificar si el proceso dado es estacionario en el sentido amplio
# con un 5% de confiabilidad.
est_s_a = estacionaridad.wss(secuencia_datos)
print(est_s_a)

# 7. Promedio temporal
# Calcular promedio temporal en el día 2019-05-15.
prom_t_fs = estacionaridad.prom_temporal(134, secuencia_datos)
print('El promedio temporal el día dado es {:0.4f} [MW]'.format(prom_t_fs))

# 8. Ergodicidad
# Identificar si el proceso es ergódico o no
# con un 5% de tolerancia:
erg = estacionaridad.ergodicidad(secuencia_datos)
print(erg)

# -----
# SECCIÓN D: Características espectrales
# -----

# 9. Función de densidad espectral de potencia
# Graficar la función espectral de potencia:
# en el día 2019-05-15
secuencia_datos = np.loadtxt('datos_consumohr.csv')
Sxx, fxx = espectro.psd(134, secuencia_datos)

# Verificación:
# Potencia promedio a partir del psd
P_promf = (1/(2*np.pi)) * np.trapz(Sxx, fxx)

# Potencia promedio a partir del promedio temporal
P_promt = estacionaridad.prom_temporal(134, secuencia_datos)

# Error:
error = (P_promf - P_promt) / (P_promt)

# Mostrar error en porcentaje
print('El error de potencia promedio es: {:0.4%}'.format(error))
