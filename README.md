# Probabilistic Methods of Signal and System Analysis

* Mario R. Peralta A.

Documentación completa en: `PX/docs/_build/html/index.html`.

---

Los proyectos tienen un paradigma de programación funcional y crea un paquete de Python por medio del trabajo colaborativo con Git, y además cada proyecto incluye la creación una página web con documentación, creada con ayuda de Sphinx.<br>

*Funcionalidad*: la revisión de la funcionalidad está en el archivo `revision.py`. Este archivo es una demostración del proyecto para mostrar los resultados apropiados según el desarrollo de cada función y las decisiones tomadas en cuanto a sus argumentos de entrada. Los resultados y análisis se muestran en la última sección el documento llamado `reporte.md`.

---

## `P3` - Proyecto 3
> Introducción y Objetivos

El Instituto Costarricense de Electricidad (ICE), por medio del Centro Nacional de Control de la Energía (CENCE), publica los datos de consumo de potencia del Sistema Eléctrico Nacional (SEN) por medio de *servicios web* (API) de acceso libre y gratuito.<br>
Entre las posibles solicitudes de datos está la información de consumo diario de potencia, registrado hora a hora para un periodo particular, que puede ser obtenida en formato JSON. <br>
Este proyecto tiene el objetivo de determinar lo siguiente:

1. Un modelo de la distribución de consumo de potencia para *una hora particular del día*, junto con su visualización y estadísticas.
1. Una comparación entre las distribuciones de consumo de potencia de *dos horas particulares del día*, por medio del cálculo numérico de una correlación y una visualización conjunta.
1. Un modelo del *consumo semanal de energía* y una deducción de los parámetros de la distribución que modela el *consumo anual de energía*.


## `P4` - Proyecto 4
> Introducción y Objetivos

Los datos de consumo eléctrico cada hora son, desde el punto de vista teórico, **procesos aleatorios**, de forma que complementaremos el trabajo que ya fue hecho en el Proyecto `P3` con algunos análisis nuevos. <br>
Sea $P(t)$ una **secuencia aleatoria** dada por el valor de consumo de potencia (MW) del Sistema Eléctrico Nacional, medido cada hora por un periodo de *hasta* 24 horas.

Este proyecto tiene el objetivo de analizar la secuencia aleatoria $P(t)$ de consumo de potencia diaria, en cuatro secciones distintas:

- Función de densidad de probabilidad
- Estacionaridad y momentos
- Ergodicidad
- Características espectrales

## `P4` - Proyecto 5
> Introducción y Objetivos

Este es un ejercicio con los conceptos de las cadenas de Markov y los procesos de nacimiento y muerte, utilizando las herramientas de programación y cálculo numérico de Python.<br>
Sea un proceso modelado como un sistema M/M/1, donde la entrada de clientes es una corriente de Poisson con parámetro $\lambda$ y el nodo de servicio está modelado con un parámetro $\nu$. <br>

1. En primer lugar, es necesario realizar un estudio de la intensidad de las solicitudes al sistema, para encontrar el parámetro $\lambda$.

1. En segundo lugar, es necesario realizar un estudio del tiempo de servicio a cada solicitud, para encontrar el parámetro $\nu$.

1. Seguidamente, es posible realizar una simulación, el análisis del servicio provisto y el diseño del sistema para satisfacer ciertos parámetros de servicio.