# Procesos aleatorios

Segundo ciclo del 2022.

- Mario R. Peralta A., B75726

*Fundamentos teóricos, Documentación y Resultados del proyecto*

La documentación completa está en `docs/_build/html/index.html`.

## 1. Fundamentos teóricos
> Fundamentos Matemáticos. <br>

### 1. Función de densidad de una proceso aleaotrio

Se selecciona una variable aleatoria $P$ para el consumo de potencia en Megawatt (Mw) con una distribución *genlogistic* a una hora particular; se hizo ésta selección con base en la experiencia del proyecto tres P3 donde se pudo ver una predominancia de distribuciones como: **asymmetric Laplace**, **genlogistic** o **pearson3** (entre otras) para la demanda de electricidad a una hora específica, por tanto se asumirá que la distribución de $P$ para una hora arbitraria será genlogistic, por su flexibilidad, la cual tiene la siguiente función de distribución de probabilidad (PDF) estandarizada. <br>

$$
f_{X}(x) = c\frac{e^{-x}}{(1+e^{-x})^{c+1}}
$$

Para $x \geq 0, c > 0$ donde $c$ es un parámetro. O en su forma explícita, haciendo $x = (p - l) / s$ y dividiendo la forma estándar entre $s$: <br>

$$
f_{P}(p) = c\frac{e^{-\left( \frac{p-l}{s}\right )}}{s(1+e^{-\left( \frac{p-l}{s}\right )})^{c+1}}
$$

Donde $P$ es la variable aleatoria de consumo de potencia en [Mw]. $p$ es la potencia. $l$ y $s$ los parámetros `loc` y `scale` respectivamente.
Luego, aunque la distribución que describe a $P$ es la misma, a lo largo de $p$, los parámetro $c$, $l$ y $s$ cambian con respecto al tiempo es decir: $c = c(t)$, $l = l(t)$ y $s = s(t)$ de tal manera que:

$$
f_{P}(p) = f_{P, T}(p, t) = P(t) = c(t)\frac{e^{-\left( \frac{p-l(t)}{s(t)}\right )}}{s(t)(1+e^{-\left( \frac{p-l(t)}{s(t)}\right )})^{\left(c(t)+1 \right)}}
$$

donde la familia de todas las funciones de $P(t)$ se denomina un **proceso aleatorio**.

### 1. 2. Momentos

Las funciones de correlación y covarianza cuantifican el grado de relación lineal entre un mismo proceso aleatorio en distintos de tiempo (auto) y entre dos procesos distintos (cruzada).
Sus propiedades tienen interpretaciones importantes en el procesamiento de señales.
Se define la autocorrelación para el proceso estocástico $X(t)$:

$$
R_{XX}(t_{1}, t_{2}) = E[ X_{1} X_{2}]
$$

Por otro lado si $\tau = t_{2} - t_{1}$ la función de autocovarianza (momento conjunto central de orden dos) de $X(t)$ se define como:


$$
C_{XX}(t,t + \tau ) = R_{XX}(t,t + \tau )-E[X(t)]E[X(t + \tau )]
$$

### 1. 3. Estacionaridad

Un proceso aleatorio se dice que es estacionario si todas sus propiedades estadísticas no cambian con el tiempo.
Muchos problemas prácticos requieren que se trate con la función de autocorrelación y el valor medio de un proceso aleatorio. Las soluciones se simplifican mucho si tales cantidades no dependieran del tiempo absoluto. La estacionaridad de segundo orden es suficiente para garantizar estas características. Empero, es a menudo más restrictivo que necesario y es deseable una forma más *relajada* de estacionaridad. La forma más útil es el *proceso estacionario en sentido amplio*, definido como aquel que cumple los siguientes criterios:

$$
E[X(t)]=\bar{X}
$$

$$
E[X(t)X(t + \tau )]=R_{XX}(\tau )
$$

Mientras que la ergodicidad establece la igualdad entre el promedio estadístico y el promedio temporal de un proceso aleatorio. Es una nueva forma de estacionaridad que simplifica el análisis del proceso aleatorio. Sea el operador de promedio temporal:

$$
A[\bullet] = \lim_{T \rightarrow \infty}\frac{1}{2T}\int_{-T}^{+T} \left[\bullet \right]  dt
$$

El valor $\bar{x} = A\left[x(t)\right]$ representa el promedio temporal de una función muestra. La función de autocorrelación temporal es denotada por $\mathscr{R}_{XX}(\tau)=A[x(t)x(t+\tau)]$. Los procesos para los que los promedios temporales igualan a los estadísticos se denominan ergódicos, luego:

$$
\bar{x} = \bar{X}
$$

$$
\mathscr{R}_{XX}(\tau)=R_{XX}(\tau)
$$

Sin embargo en el análisis de datos no es conveniente trabajar con las funciones de densidad.
[Augmented Dickey–Fuller test](https://en.wikipedia.org/wiki/Augmented_Dickey%E2%80%93Fuller_test) es un tipo de prueba estadística llamada [Unit Root test](https://en.wikipedia.org/wiki/Unit_root_test)

La intuición detrás de una prueba de raíz unitaria es que determina la fuerza de una secuencia se define por una tendencia.

Hay una serie de pruebas de raíz unitaria y el Dickey-Fuller aumentado puede ser uno de los más ampliamente utilizados. Utiliza un modelo autorregresivo y optimiza un criterio de información a través de múltiples valores de retardo diferentes.

La hipótesis nula de la prueba es que la serie temporal puede ser representada por una raíz unitaria, que no es estacionaria (tiene alguna estructura dependiente del tiempo). La hipótesis alternativa (rechazando la hipótesis nula) es que la serie temporal es estacionaria. <br>

**Hipótesis nula (H0):** Si no se rechaza, sugiere que la serie temporal tiene una raíz unitaria, lo que significa que no es estacionaria. Tiene una estructura dependiente del tiempo. <br>
**Hipótesis alternativa (H1):** La hipótesis nula es rechazada; sugiere que la serie temporal no tiene una raíz unitaria, lo que significa que es estacionaria. No tiene una estructura dependiente del tiempo.

Interpretamos este resultado utilizando el valor *p* de la prueba. Un valor *p* por debajo de un umbral (como 5%) sugiere que rechazamos la hipótesis nula (estacionaria), de lo contrario un valor *p* por encima del umbral sugiere que no podemos rechazar la hipótesis nula (no estacionaria).

* p-value > 0.05: No se puede rechazar la hipótesis nula (H0), los datos tienen una raíz de unidad y no son estacionarios.
* p-value <= 0.05: Rechaza la hipótesis nula (H0), los datos no tienen una raíz unitaria y son estacionarios.

### 1. 4. Espectro

Cuando los procesos estocásticos describen señales (funciones unidimensionales en el tiempo), es posible analizarlos según sus características espectrales, es decir, relativas a la frecuencia.
Al tratarse de una secuencia aleatoria nos referimos a señales de tiempo discreto. Nuestros datos suelen ser muestreados y finitos, por lo que el procesamiento en tiempo discreto es el que utilizamos en la práctica.
Consideremos una señal discreta $\vec{x} = (x_{1}, \cdots, x_{N})$, donde $N$ es la longitud de la señal. Esto puede ser la señal completa o un solo miembro del agregado. Además, supongamos que la señal se muestra a la frecuencia $F_{s} = \frac{1}{\Delta t}$, donde $\Delta t$ el intervalo de la muestra en horas, entonces la duración de la señal está dada por $T = (N-1)\Delta t$. Ésto nos conduce a la definición de densidad espectral de potencia para tiempo discreto a la frecuencia $f$: <br>

$$
\mathcal{S}_{xx}(f) =
$$

$$
\frac{\left( \Delta t \right)^{2}}{T} \left |  \displaystyle\sum\limits_{n=1}^{N} x_{n}e^{-j2\pi f n \Delta t} \right| ^{2}
$$

## 2. Paquete `proceso`
> Descripción general del paquete. <br>

### **Obtiene la base de datos, grafica de proceso y probabilidad.** <br>

* Contiene todas las funciones necesarias para solicitar
la base de datos del servidor API del CENCE, analizar
una secuencia aleatoria, obtener su función de densidad
y asumiendo que la distribución es genlogistic generar
los parámetros de las distribuciones en el tiempo para
una gráfica 3D de la secuencia aleatoria.

### **Calcula autocorrelación y autocovarianza.** <br>

* Para una secuencia aleatoria dada calcula el grado de linealidad
y disperción gracias al concepto de momentos.

### **Para una secuencia aleatoria se evalúa cuan dependiente del tiempo és.** <br>

* Gracias a los conceptos de proceso Estacionario en el Sentido Amplio
(wss) y Ergodicidad (conociendo el promedio temporal) es posible
estimar cuan estacionaria es las secuencia aleatoria dada.

### **Densidad Espectral de Potencia a partir de funcion muestra.** <br>

* Por la definición matemática de la densidad espectral de potencia (spd)
calcula la función y gráfica cuando los datos son finitos y discretos.

## 3. Módulos y sus Funciones
> Contenido del paquete. <br>

El paquete cuenta con cuatro módulos a saber: `proceso`, `momento`, `estacionaridad` y `espectro`:
### 3. 1 `proceso`
1. `datos_demanda()`: Solicita datos de potencia [MW] consumida.
1. `datos_hora()`: Obtener los datos de consumo de potencia de una hora particular.
1. `demanda()`: Arreglo de muestras.
1. `parametros()`: Parámetros de la distribución de consumo de cada hora.
1. `modelo_parmtrs()`: Modelo polinómico de los parámetros como función del tiempo.
1. `plot_parmtrs()`: Grafica comparativa entre parámetros reales y aproximados.
1. `plotpdf_datos_modelo()`: Compara las distribuciones resultantes.
1. `densidad()`: Conjunto de distribuciones que describen la secuencia aleatoria.
1. `plot_p_hora()`: Grafica del proceso aleatorio en un instante.
1. `grafica()`: Grafica 3D de la secuencia aleatoria.
1. `probabilidad()`: Encuentra la probabilidad de ocurrencia de un valor.

### 3. 2 `momentos`
1. `momentos()`: Calcular autocorrelación y autocovarianza.

### 3. 3 `estacionaridad`
1. `wss()`: Determina si el proceso aleatorio dado es *wss*.
1. `prom_temporal()`: Dada una función muestra determina el promedio temporal.
1. `ergodicidad()`: Determina si un proceso es ergódico.

### 3. 4 `espectro`
1. `psd()`: Calcula y grafica la Densidad Espectral de Potencia *(psd)*.

## 4. Resultados
> Análisis de resultados y conclusiones. <br>

### 4. 1 `proceso`

Gracias a la función `modelo_parmtrs()` del módulo proceso se encuentran los modelos continuos en función del tiempo de los parámetros del proceso aleatorio para una familia de distribuciones `genlogistic` definida en la sección Fundamentos teóricos.

$$
c(t) = 0.21 - 0.06t - 0.89t² +
0.48t³ + 4.35t⁴ - 1.72t⁵ -
3.08t⁶ + 1.24t⁷
$$

$$
loc(t) = 1578.10 + 73.59t - 913.80t² +
1627.63t³ + 635.63t⁴ - 2417.37t⁵ -
224.04t⁶ + 757.14t⁷
$$

$$
scale(t) = 18.33 - 2.27t - 13.04t² +
10.25t³ + 88.90t⁴ + 26.12t⁵ -
71.55t⁶ - 34.73t⁷
$$

```{eval-rst}
.. figure:: figs/pfig_1.svg
   :alt: parmtr c
   :height: 200px
   :width: 400px
   :align: center

   Parámetro *c*

   Modelo polinómico aproximado en tiempo continuo de *c*
```

```{eval-rst}
.. figure:: figs/pfig_2.svg
   :alt: parmtr loc
   :height: 200px
   :width: 400px
   :align: center

   Parámetro *loc*

   Modelo polinómico aproximado en tiempo continuo de *loc*
```

```{eval-rst}
.. figure:: figs/pfig_3.svg
   :alt: parmtr scale
   :height: 200px
   :width: 400px
   :align: center

   Parámetro *scale*

   Modelo polinómico aproximado en tiempo continuo de *scale*
```

Mientras que la secuencia aleaoria resultante es:

```{eval-rst}
.. figure:: figs/p3D.svg
   :alt: Grafica de secuencia 3D
   :height: 200px
   :width: 450px
   :align: center

   Secuencia aleatoria

   Evolución de la *PDF* de demanda de potencia a lo largo de las horas.
```

En la que se observa que cuando el día comienza (horas 0:00, 1:00 y 3:00am) hay bastantes personas consumiendo poca potencia [MW], pero cuanto más avanza el día hay un desplazamiento positivo en el eje de consumo de potencia no obstante la demanda decae, es decir hay algunas personas consumiendo bastante electricidad hasta que se llega aproximadamente a la hora 13:00, donde aunque comienza a decaer un poco el consumo de [MW] la demanda se mantiene lo que significa que hay algunas personas consumiendo mucha potencia. Al caer la hora 20:00 hasta las 23:00 se observa un aumento en la demanda pero de menor potencia, o sea muchas personas consumiento algo de energía. Lo cual tiene sentido si se tiene en cuenta que Las Industrias mayormente son de horario matutino (7:00-14:00) y produncen un consumo pico sin que por ello implique un aumento en la población.

Por otro lado gracias a la función `densidad()` y `probabilidad()` del mismo módulo es posible determinar por ejemplo la probabilidad de registrar un consumo de potencia $800 < C < 900$ [MW] entre las 7:00 am y las 10:59 am, la que resulta en un valor de $0.4944$%, que tiene sentido ya que en horas matutinas es cuando más potencia se consume, por lo que se mecionó anteriormente, con un consumo promedio superior a los 1 300 [MW], de ahí que le evento de que ocurra un consumo tan escaso en horas matutina sea poco probable. La probabilidad hubiera aumentado se repite el experimento en horas de la madrugada de 0:00 a 3:59 am y de hecho lo hace con una nueva probabilidad del $13.7985$ \%.

### 4. 2 `momento`

Para la autocorrelación y autocovarianza basta con evaluar la misma variable aleatoria (consumo de potencia a una hora particular) en horas diferentes de la misma secuencia $P(t)$, por consistencia se toman las horas sugeridas: 7:00am y 11:00am con la función del mismo nombre `momento()` con los resultados:

$$
\begin{align*}
R_{XX} &= 1763866.9174\\
C_{XX} &= 11061.3470
\end{align*}
$$

Es arriesgado concluir que tan lineal es toda la secuencia aleatoria a partir de dos horas solamente. Para asegurarse del grado de linealidad es necerio profundizar en el análisis de estacionaridad de al menos una función muestra como se realiza en el módulo a continuación.

### 4. 3 `estacionaridad`

De las funciones `wss()` y `ergodicidad()` se determina que el proceso es ambos: Estacionario en el Sentido Amplio y Ergódico, esto implica al menos:<br>

    - La secuencia genera una serie de observaciones estacionarias.

    - Tanto el valor medio como la varianza se mantienen constantes.

    - La secuencia no exhibe una tendencia. 

    - La secuencia no exhibe estacionaridad sólo por momentos.

    - Estrictamente estacional, o sea que la unión de las distribuciones
      depende solamente del lapso de tiempo entre dos instantes
      de tiempo arbitrarios.


### 4. 4 `espectro`

Aprovechando que el proceso sólo depende de $\Delta t$ la función `spd()` utiliza la definición de densidad espectral de potencia mostrada en la sección de Fundamentos Teóricos para obtener la función de $S_{PP}(f)$ en el dominio de la frecuencia $f$. En la gráfica se distingue el impulso típico de funciones espectrales.

```{eval-rst}
.. figure:: figs/psdplot.svg
   :alt: Grafica psd
   :height: 200px
   :width: 400px
   :align: center

   Densidad espectral de potencia (psd)

   En el dominio de la frecuencia la potencia es la misma que en el dominio del tiempo.

```

Por medio de la siguiente definición es posible corroborar que la potencia promedio de la secuencia $P$ se puede calcular en el dominio de la frecuencia o del tiempo, con la función `prom_temporal()` se optiene menos de un 5% de error.

$$
P_{PP} = \frac{1}{2\pi} \int_{-\infty}^{+\infty} \mathcal{S}_ {PP}(\omega)d\omega \\
$$

$$
P_{PP} = \lim_{T \rightarrow \infty}\frac{1}{2T}\int_{-T}^{+T} E\left[X^2(t) \right]  dt
$$

## 5. Referencias

1. [scipy.stats.genlogistic](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.genlogistic.html)
1. [Augmented Dickey–Fuller test](https://en.wikipedia.org/wiki/Augmented_Dickey%E2%80%93Fuller_test)
1. [Unit root test](https://en.wikipedia.org/wiki/Unit_root_test)
1. [Stationary Data Tests](https://pythondata.com/stationary-data-tests-for-time-series-forecasting/)
