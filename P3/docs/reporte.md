# Variables aleatorias múltiples

Segundo ciclo del 2022

- Mario Roberto Peralta A., B75626

*Fundamentos teóricos, Documentación y Resultados del proyecto.*

La documentación completa está en `docs/_build/html/index.html`.

## 1. Fundamentos teóricos
>  Conceptos de las cadenas de Markov y los procesos de nacimiento y muerte. <br>

A pesar del título, nuestro estudio hará énfasis sobre la teoría de dos variables aleatorias.
Si bien el estudio será restringido a dos variables aleatorias, la generalización a tres o más variables será evidente y podrá llevarse a cabo sin dificultad.<br>
Supóngase que dos variables aleatorias $X$ e $Y$ están definidas sobre un espacio $S$ de muestras, donde valores específicos de $X$ e $Y$ se denotan por $x$ e $y$, respectivamente. Cualquier par ordenado de números $(x,y)$ puede considerarse un punto aleatorio en el plano $xy$. El punto puede tomarse como un valor espec ́ıfico de un vector aleatorio.
El plano de todos los puntos $(x,y)$ en los intervalos de $X$ e $Y$ puede considerarse un nuevo espacio de muestras. Es un espacio vectorial donde los componentes de cualquier vector son los valores de las variables aleatorias $X$ e $Y$. Se le puede llamar al espacio de muestras resultante **espacio producto bidimensional**, y se le da el símbolo $S_{J}$.
Como en el caso de una variable aleatoria, defínase los eventos $A$ y $B$ por

$$
A = \{X \leq x\} \qquad B = \{Y \leq y\}
$$

El evento $A \cap B$ definido en $S$ corresponde al evento conjunto $\{X \leq x \textrm{  e  } Y \leq y\}$ definido en $S_{J}$, el cual se escribe $\{X \leq x, Y \leq y\}$.

### 1.1 Función acumulativa conjunta

Las funciones $F_{x}(x)$ y $F_{y}(y)$ obtenidas de esta manera se llaman funciones de distribución acumulativas *marginales*. Con respecto a esto, obsérvese que $F_{X,Y}(x, y) = P\{X \leq x, Y \leq y \} = P(A \cap B)$. Si se hace que $y \rightarrow \infty$, esto equivale a hacer $B = \{Y \leq y\}$ el evento cierto; es decir, $B = \{Y \leq \infty \} = S$. Además, dado que $A \cap B = A \cap S = A$, entonces se tiene $F_{X,Y}(x, \infty) = P(A \cap S) = P(A) = P\{X \leq x\} = F_{X}(x)$, Una prueba similar puede establecerse para $F_{Y}(y)$.

### 1.2 Función de densidad probabilística conjunta

Para dos variables aleatorias $X$ e $Y$, la función de densidad probabilística conjunta (función de densidad conjunta), $f_{X,Y}(x, y)$, está definida por la segunda derivada de la funció de distribución acumulativa conjunta dondequiera que esta exista,

$$
f_{X,Y}(x, y) = \frac{\partial^{2} F_{X,Y}(x, y)}{\partial x \partial y}
$$

Las funciones $f_{X}(x)$ y $f_{Y}(y)$ se llaman funciones de densidad probabilística *marginal* o, simplemente, funciones de densidad marginal.

$$
f_{X}(x) = \frac{dF_{X}(x)}{dx}
$$

$$
f_{Y}(y) = \frac{dF_{Y}(y)}{dy}
$$

### 1.3 Teorema de límite central

Convergencia en la distribución. Considérese $X_{1}, ..., X_{N}$ variables aleatorias *independientes e idénticamente distribuidas* `iid`, con media común $\mu_{X_{i}} = \mu$ y desviación estándar $\sigma_{X_{i}} = \sigma$. Sea además

$$
S_{N} = X_{1} + \cdots + X_{N}
$$
La **suma** de ellas. Según el teorema del límite central:

$$
S_{N} \sim \mathcal{N}\left(N \mu,\,\sigma \sqrt{N}\right)
$$

conforme $N \rightarrow \infty$, donde $N \mu$ es la media y $\sigma \sqrt{N}$ la desviación estándar de la distribución normal.

### 1.4 Correlación de dos variables aleatorias

El momento de segundo orden $m_{11} = E[XY]$ es denominado la **correlación** de $X$ y $Y$. Recibe el símbolo especial $R_{XY}$ por su importancia.

$$
R_{XY} = m_{11} = E[XY]
$$

Coeficiente de correlación de *Pearson*

$$
\rho = \frac{C_{XY}}{\sigma_{X} \sigma_{Y}}
$$

donde $C_{XY}$ es la covarianza. $\sigma_{X}$ y $\sigma_{Y}$ corresponden a la desviación estandar de cada variable aleatoria $X$ e $Y$. Para un $\rho$ cuanto más cercano a $1$ implica que todos los puntos de datos se encuentran en una línea para la que $Y$ aumenta a medida que $X$ aumenta, y viceversa para $-1$. Un valor de $0$ implica que no hay dependencia lineal entre las variables.

Interpretaciones posibles:<br>
* "La correlación es el grado en el cual dos o más cantidades están linealmente asociadas".
* Pero (fundamental) "**correlación no implica causalidad**".

## 2. Paquete: `consumo`
> Descripción y objetivos del paquete.<br>

Este proyecto tiene el objetivo de determinar lo siguiente:

1. Un modelo de la distribución de consumo de potencia para *una hora particular del día*, junto con su visualización y estadísticas.
1. Una comparación entre las distribuciones de consumo de potencia de *dos horas particulares del día*, por medio del cálculo numérico de una correlación y una visualización conjunta.
1. Un modelo del *consumo semanal de energía* y una deducción de los parámetros de la distribución que modela el *consumo anual de energía*.

## 3. Módulos y sus funciones
> Contenido del paquete. <br>

### 3. 1 `potencia.py`
1. `datos_demanda()`: Importar y extraer datos necesarios para análisis.
1. `datos_hora()`: Consumo de potencia de una hora arbitraria.
1. `modelo_hora()`: Modelo probabilístico de mejor ajuste y sus parámetros.
1. `estadisticas_hora()`: Momentos a partir de los datos.
1. `visualizacion_hora()`: Histograma de demanda de potencia a una hora.

### 3. 2 `correlacion.py`
1. `correlacion_horas()`: Coeficiente de correlación (de Pearson).
1. `visualizacion_horas()`: Histograma bivariado de distribución.

### 3. 3 `energia.py`
1. `energia_semanal()`: Energía total consumida por períodos de siete días.
1. `modelo_energia_semanal()`: Modelo probabilístico de demanda de energía semanal.
1. `modelo_energia_anual()`: Modelo probabilístico de consumo de energía anual.

### 3. 4 `solicitud.py`
1. `datos_consumo()`: Solicita datos de potencia [MW] consumida.
1. `datos_hora()`: Obtener los datos de consumo de potencia de una hora particular.
1. `demanda()`: Arreglo de muestras de consumo cada hora.

```{eval-rst}
.. _results-target:
```

## 4. Resultados
> Análisis de resultados y conclusiones. <br>

Gracias a las funciones del módulo `potencia` e importando los datos de consumo del año 2019 se ve que la distribución de demanda de potencia a la hora, arbitraria, 19:00 es *Pearson3*, en la figura se muestra su PDF, cuyos parámetros de modelo son:

 - *skew*: -0.7770
 - *loc*: 1530.6454
 - *scale*: 88.0676

Y con la función `estadisticas_hora()` sus momentos, obtenenidos a partir de los datos, y no de la distribución anterior:

 - *media*: 1530.6454
 - *varianza*: 7541.6996
 - *desviación estandar*: 86.8430
 - *inclinación*: -0.5539
 - *kurtosis*: -0.0414

Por otro lado con el módulo `correlacion` y tomando dos horas arbitrarias 18:00 y 10:00 como variables aleatorias (v.a) diferentes $H_{x}$ y $H_{y}$ respectivamente, se obtiene que el coeficiente de Pearson es de $0.7338$ interpretándose como una buena linealidad entre ambas v.a. En la figura se observa su histograma conjunto.

```{eval-rst}
.. figure:: imgs/hr19.svg
   :alt: pdf consumo a una hora
   :height: 200px
   :width: 400px

   Mejor distribución *Pearson3*

   Función de densidad probabilística (PDF) del consumo de potencia a una hora particular.
```

```{eval-rst}
.. figure:: imgs/histHxHy.svg
   :alt: histograma bivariado
   :height: 200px
   :width: 400px

   Histograma bivariado

   Histograma bivariado (conjunto) para las variables aleatorias :math:`H_{x}` y :math:`H_{y}`.
```

Finalmente con el módulo `energia` se obtiene que la distribución de mejor ajuste que representa el consumo de energía semanal es *Skewcauchy* cuya PDF se muestra en la figura, y parámetros de modelo son:

- *a*: $0.3171$
- *loc*: $211933.0126$
- *scale*: $3296.8808$

```{eval-rst}
.. figure:: imgs/weekly_dist.svg
   :alt: pdf demanda energía semanal
   :height: 200px
   :width: 400px

   Mejor distribución *Skewcauchy*

   Función de densidad probabilística (PDF) del consumo de energía semanal.
```

```{eval-rst}
.. figure:: imgs/yearly_normdist.svg
   :alt: pdf demanda energía anual
   :height: 200px
   :width: 400px

   Deducción modelo anual
   Aproximación de la distribución Normal de consumo energético anual. Asumiendo que el consumo durante todas las semanas fue ``iid``.
```

Con dicha distribución se generan datos para aproximar la distribución de consumo energético anual, que según el teorema del límite central converge a una distribución normal la cual se muestra en la figura y cuyos parámetros de modelo en megajoule [MW] son:
 - *media*: $37235479.5297$
 - *desviación estándar*: $1678642.2756$
## 5. Referencias
> Material de apoyo. <br>

1. Romero Chacón, J. *Modelos probabilísticos de señales y sistemas*.