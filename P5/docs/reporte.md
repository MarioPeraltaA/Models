# Teoría de colas

- Mario Roberto Peralta Amador, B75626

*Fundamentos teóricos, Documentación y Resultados del proyecto.*

La documentación completa está en `docs/_build/html/index.html`.

```{eval-rst}
.. _theory-label:
```

## 1. Fundamentos teóricos
>  Conceptos de las cadenas de Markov y los procesos de nacimiento y muerte. <br>

### 1.1 El proceso de nacimiento y muerte en tiempo continuo
Estas son las dos suposiciones básicas de un proceso de nacimiento y muerte: la primera es si al tiempo $t$ la máquina (sistema) está en el estado $i$, permanece en ese estado por un tiempo aleatorio que es exponencialmente distribuido con parámetro $\Omega_{i}$; así, el tiempo de espera promedio en el estado $i$ es el recíproco $\frac{1}{\Omega_{i}}$. $\Omega_{i}$ depende del estado $i$, pero no depende de otras características; por ejemplo, $\Omega_{i}$ no depende de si la máquina estaba en estado $k$ o estado $j$. El estado $i$ pudiera ser absorbente: esto significa que una vez que la máquina entra al estado $i$, permanecerá siempre ahí. Si esto último es así, entonces $\Omega_{i} = 0$; es decir, el tiempo de espera promedio es $\frac{1}{\Omega_{i}} \to \infty$. <br>
La segunda suposición de un proceso de nacimiento y muerte es que cuando la máquina sale del estado $i$, cambia al estado $i + 1$ o al estado $i − 1$, con probabilidades que no dependen de qué tan largo la máquina estuvo en el estado $i$ o de otros detalles tales como el tiempo $t$ o del estado de la máquina antes de que cambiara al estado $i$, se definen las probabilidades de transisción:

$$
\begin{equation}
\begin{split}
p_{i} & = P({\textrm{próximo estado es i + 1} | \textrm{último estado es i}}) \\
q_{i} & = P({\textrm{próximo estado es i - 1} | \textrm{último estado es i}}) \\
 & = 1 - p_{i}
\end{split}
\end{equation}
$$

La segunda suposición mencionada significa que $p_{i}$ y $q_{i}$ dependen solamente del estado $i$ y no de otros detalles del proceso.<br>
Las dos suposiciones constituyen una generalización de la *propiedad de la falta de memoria*.<br>
En particular, si el estado al tiempo $t$ es $X_{t} = i$, entonces es completamente irrelevante si ha estado en el estado $i$ por varios años o si acaba de cambiar al estado $i$, para predecir cuando se mudará del estado $i$ a $i + 1$ o $i - 1$. *La suposición de que dado el estado presente, el futuro del proceso es independiente del pasado es denominada la suposición de Markov.* En resumen, un proceso de nacimiento y muerte en tiempo continuo consiste de una máquina que puede cambiar entre estados en un espacio de estados $S$. <br>
**Nota:** El paquete `cadena` supone que ningún estado es absorbente.
### 1.2 Colas
De lo anterior se tiene que $X_{t}$ denota el estado ocupado al tiempo $t$ para $t \geq 0$. La máquina (sistema) permanece en el estado $i$ por un periodo de tiempo (el tiempo de espera o permanencia) que es exponencialmente distribuido con parámetros $\Omega_{i}$ (tiempo de espera promedio $\frac{1}{\Omega{i}}$). Cuando la máquina cambia, cambia a los estados $i + 1$, $i − 1$ con probabilidades respectivas $p_{i}$, $q_{i}$ = $1 − p_{i}$. **Colas** son una subclase de procesos de nacimiento y muerte, la máquina consiste de clientes y servidores. Puede haber uno o más servidores. Clientes arriban de acuerdo a una corriente Poisson con parámetro $\lambda$. $\lambda$ clientes arriban, en promedio, por unidad de tiempo. Los tiempos de servicio son aleatorios, pero se supone que están exponencialmente distribuidos con parámetro $\nu$, luego el tiempo medio de servicio es $\frac{1}{\nu}$. $X_{t}$, por extensión, es la longitud de la cola en el tiempo $t$, en general se definen los parámetros de permanencia y de transición para colas de cierta cantidad de servidores; asumiendo que en una cola, solamente un movimiento o cambio de estado ocurre a la vez: <br>

* La cola de un servidor y para $i \geq 1$

$$
\begin{equation}
\begin{split}
\Omega_{0} & = \lambda \qquad \qquad p_{0} = 1 \qquad \qquad q_{0} = 0 \\
\Omega_{i} & = \lambda + \nu \qquad \textrm{ } p_{i} = \frac{\lambda}{\lambda + \nu} \qquad \textrm{ } q_{i} = \frac{\nu}{\lambda + \nu} \\
\end{split}
\end{equation}
$$

* La cola de *s* servidores y para $i \geq s$

$$
\begin{equation}
\begin{split}
\Omega_{0} & = \lambda \qquad \qquad \textrm{  } p_{0} = 1 \qquad \quad \quad \textrm{ } \textrm{ } q_{0} = 0 \\
\Omega_{1} & = \lambda + \nu \quad \quad \textrm{ } \textrm{ } p_{1} = \frac{\lambda}{\lambda + \nu} \quad \quad \textrm{ } \textrm{ } q_{1} = \frac{\nu}{\lambda + \nu} \\
\Omega_{2} & = \lambda + 2\nu \qquad p_{2} = \frac{\lambda}{\lambda + 2\nu} \qquad q_{2} = \frac{2\nu}{\lambda + 2\nu} \\
\Omega_{i} & = \lambda + s \nu \qquad p_{i} = \frac{\lambda}{\lambda + s\nu} \qquad \textrm{ } q_{i} = \frac{s\nu}{\lambda + s\nu} \\
\end{split}
\end{equation}
$$

* La cola con infinito números de servidores y espacio de estados:

$$
S = \{ 0, 1, 2, ..., N \}
$$

$$
\begin{equation}
\begin{split}
\Omega_{0} & = \lambda \qquad \qquad \textrm{  } p_{0} = 1 \qquad \quad \quad \textrm{ } \textrm{ } q_{0} = 0 \\
\Omega_{1} & = \lambda + \nu \quad \quad \textrm{ } \textrm{ } p_{1} = \frac{\lambda}{\lambda + \nu} \quad \quad \textrm{ } \textrm{ } q_{1} = \frac{\nu}{\lambda + \nu} \\
\Omega_{2} & = \lambda + 2\nu \qquad p_{2} = \frac{\lambda}{\lambda + 2\nu} \qquad q_{2} = \frac{2\nu}{\lambda + 2\nu} \\
\Omega_{i} & = \lambda + i \nu \qquad \textrm{ } p_{i} = \frac{\lambda}{\lambda + i\nu} \qquad \textrm{ } q_{i} = \frac{i\nu}{\lambda + i\nu} \\
\vdots \text{ } & = \qquad \qquad  \qquad \textrm{ } \vdots \qquad \qquad  \qquad \quad \vdots \\
\Omega_{N} & =  N \nu \qquad \quad p_{N} = 0 \qquad \quad \quad \textrm{ } q_{N} = 1 \\
\end{split}
\end{equation}
$$

```{eval-rst}
.. _vector-s-s:
```
### 1.3 El vector de probabilidad de estado estable
Después de que el proceso de nacimiento y muerte evoluciona por algún tiempo, se llega a la estabilidad (convergencia). Esto significa que el estado del proceso se vuelve menos y menos dependiente de su estado inicial $X_{0}$ en el tiempo $0$. El proceso seguirá cambiando estados pero habrá una probabilidad bien definida $\phi_{i}$ con la que el proceso estará en el estado $i$.
Las probabilidades $\phi_{i}$ de estado estable satisfacen, para $i = 1, 2, \cdots$

$$
\begin{equation}
\phi_{i} = \frac{\Omega_{i-1}p_{i-1}}{\Omega_{i}q_{i}} \phi_{i-1}
\end{equation}
$$

Para expresar cada $\phi_{i}$ en términos de $\phi_{0}$. Entonces se usa la normalización:

$$
\begin{equation}
\sum_{i} \phi_{i} = 1
\end{equation}
$$

Para que exista un estado estable, la tasa de partidas $\nu$ debe ser mayor que la de llegadas $\lambda$, el paquete `cadena` asume que es así. Se definen las probabilidades de estado $i$-ésimo en términos de $\phi_{0}$:
* Para la cola de servidor único: Sistema M/M/1. Sea $\rho = \frac{\lambda}{\nu}$:

$$
\begin{equation}
\phi_{i} = \rho^{i}\phi_{0}
\end{equation}
$$

Donde: $\phi_{0} = 1 - \rho$.

* Para la cola de $s$ servidores: Sistema M/M/s. Sea $\varepsilon = \frac{\lambda}{s \nu} = \frac{\rho}{s}$:

$$
  \phi_{i} =
\begin{cases}
\frac{(s \varepsilon)^{i}}{i!} \phi_{0},  & i < s \\
\frac{s^{s}\varepsilon^{i}}{s!} \phi_{0}, & i \geq s
\end{cases}
$$

Donde:

$$ 
\phi_{0} = \left [ \sum_{k = 0}^{s - 1}\left ( \frac{\left ( s \varepsilon \right )^{k}}{k!} + \frac{\left ( s \varepsilon \right )^{s}}{s!\left ( 1 - \varepsilon \right )}\right ) \right ]^{-1}
$$

* Para la cola de infinitos servidores:

$$
\begin{equation}
\phi_{i} = \frac{\rho^{i}}{i!} \phi_{0}
\end{equation}
$$

Donde: $\phi_{0} = e^{-\rho}$. <br>

Por otro lado, la longitud esperada de la cola en estado estable o sea, **número promedio de clientes en el sistema** considerando que en el estado estable, la longitud $L$ de la cola es $i$ con probabilidad $\phi_{i}$ para $i = 0, 1, 2, \cdots$.
Y además sea $E[L_{q}]$ el número promedio de espacios que los clientes esperan en fila (cuando el servidor está ocupado) antes de ser atendidos y recibir el servicio:

* M/M/1

$$
\begin{equation}
E[L] = \frac{\lambda}{\nu - \lambda}
\end{equation}
$$

Donde:

$$
E[L_{q}] = \rho E[L]
$$

* M/M/s

$$
\begin{equation}
E[L] = \rho + \frac{\varepsilon \left( s \varepsilon \right)^{s}}{s! \left( 1 - \varepsilon \right)^{2}}\phi_{0}
\end{equation}
$$

Donde:

$$
E[L_{q}] = E[L] - \rho
$$

* Infinitos servidores

$$
\begin{equation}
E[L] = \rho
\end{equation}
$$

## 2. Paquete
> Descripción y objetivos del paquete.<br>

El paquete cuenta con los módulos: `analisis`, `simulacion`, `servicio` y `dimensionamiento`; para suministrar una serie de funciones que permitan el análisis de Cadenas de Markov en tiempo continuo particularmente el proceso de nacimiento y muerte. <br>
El paquete importa el archivo `clientes.csv` el cual especifica el tiempo de llegada (en segundos desde el inicio de la simulación) de los primeros $N$ clientes de un sistema, el intervalo de tiempo (segundos) entre el cliente y el anterior y la duración del servicio (segundos) prestado a cada uno. Nótese que no está especificado el tiempo en que son atendidos, únicamente el tiempo de la llegada, ya que el momento de la atención es variable: puede suceder antes o después, dependiendo de la fila (clientes en espera) en el sistema. <br>
Se asume que `clientes.csv` es un conjunto de datos proveniente de un proceso de nacimiento y muerte modelado como un sistema M/M/1, donde la entrada de clientes es una corriente de *Poisson* con parámetro $\lambda$ y el nodo de servicio presenta una distribución exponencial cuyo parámetro es $\nu$ pero que además exite estado estable (la serie del vector del probabilidad converge a uno) es decir $\nu$ > $\lambda$. Luego el paquete permite:

- Encontrar parámetro de tiempo de permanencia y probabilidades de transición de un sistema M/M/1 o M/M/s y de cantidad de estados indefinidos o sea $i = 0, 1, 2, \cdots$ (pero no infinitos).

- Simular y visualizar un sistema M/M/1 de parámetros de intensidad dados.

- Para un sistema M/M/1, calcular la probabilidad del estado $i$-ésimo y el porcentaje de tiempo que ha de presentarse una fila (clientes en espera) de más de $L_{q}$ espacios.

- Dimensionar la capacidad de un sistema con base en la previsión de solicitudes recibidas ("clientes") por segundo y bajo ciertos parámetros de calidad del servicio.


## 3. Módulos y sus funciones
> Contenido del paquete. <br>

### 3. 1 `analisis.py`
Funciones:
1. `llegada()`: Parámetro de llegada.
1. `servicio()`: Parámetro de servicio.
1. `parametros()`: Permanencia y probabilidades de transición del estado $i$.

### 3. 2 `simulacion.py`
Funciones:
1. `sistema()`: Simula una secuencia de llegadas y salidas de clientes al sistema.
1. `visualizacion()`: Grafica el comportamiento del sistema.

### 3. 3 `servicio.py`
Funciones:
1. `estados()`: Para estados definidos, obtiene el vector de estado estable.
1. `probabilidad()`: En general, probabilidad de estado de cada estado.
1. `fila()`: Porcentaje de tiempo que "Lq" clientes o más esperan en fila.

### 3. 4 `dimensionamiento.py`
Funciones:
1. `t_servicio()`: Para M/M/1, tiempo promedio de servicio que cumple criterio.
1. `probabilidades()`: Probabilidades de estado sistema M/M/s.
1. `servidores()`: Para M/M/s encuentra número de servidores mínimos requeridos.
1. `tiempo()`: Para M/M/s, tiempo promedio de servicio que cumple criterio.

```{eval-rst}
.. _resultados-label-target:
```
## 4. Resultados
> Análisis de resultados y conclusiones. <br>

Para la base de datos `clientes.csv` provista los resultados al llamar cada función fueron:
### 4. 1 Parámetros de sistema M/M/1
Con las funciones `llegada()` y `servicio()` se encuentra que los parámetro de intensidad de llegada y servicio son: 0.0350 y 0.0488 respectivamente, luego se cumple que $\nu$ > $\lambda$. <br>
Para observar el comportamiento de las probabilidades de transición se implementa, mediante un lazo for, la función `parametros()` hasta el estado $i$ = 5 (inclusivo), con un servidor $s = 1$ y asumiendo que el espacio de estados es indefinido; es decir $q_{N} = 1$ no ocurre (ver cola con infinitos servidores), se obtiene:<br>

El parámetro de permanencia:

$$
\{ \Omega_{i} \}_{0}^{5} = [0.0350, 0.0839, 0.0839, 0.0839, 0.0839, 0.0839]
$$

Probabilidades de transición:

$$
\begin{equation*}
\begin{split}
\{p_{i} \}_{0}^{5} &= [ 1, 0.4178, 0.4178, 0.4178, 0.4178, 0.4178] \\
\{q_{i} \}_{0}^{5} &= [ 0, 0.5822, 0.5822, 0.5822, 0.5822, 0.5822]
\end{split}
\end{equation*}
$$

Note que se cumple $q_{i} = 1 - p_{i}$ y que a partir de $i \geq 1$ los parámetros de permanencia $\Omega_{i}$ y probabilidades de transisción $p_{i}$, $q_{i}$; se mantienen constantes ya que se trata de un único servidor.

```{eval-rst}
.. _simulacion:
```
### 4. 2 Simulación de sistema M/M/1
Conocidos los parámetros $\lambda$ y $\nu$ de cierta distribución exponencial con la función `sistema()` se genera un proceso de nacimiento y muerte con datos que son generados aleatoriamente, y con `visualizacion()` se grafican:

```{eval-rst}
.. figure:: respuesta.svg
   :alt: Proceso de nacimiento y muerte M/M/1
   :height: 200px
   :width: 400px
   :align: center

   Dinámica sistema M/M/1

   Comportamiento típico de clientes en fila que entran y salen con un servidor disponible.
```

En la gráfica se presenta, por ejemplo, un pico casi a la hora 7hr, esto quiere decir que fue el momento en que cierto cliente esperó en fila la mayor cantidad de tiempo en de todo lo que duró el sistema.

### 4. 3 Análisis vector de estado estable y tiempo de espera promedio.
La función `probabilidad()` permite encontrar un expresión general para calcular la probabilidad de un estado arbitrario con esto, se procedió a calcular, por ejemplo, la del estado $i = 5$ que resultó en un 5.3750%, se cumple, gracias a la convergencia (estado estable), que cuanto más grande sea el estado $i$ o sea la longitud de la cola $L$ menos probable es su ocurrencia. Por otro lado con la función `fila()` se verifica que el 36.9635% del tiempo los clientes hacen fila de al menos $L_{q} = 2$ espacios (lo que en general esperan) antes de ser atendidos.

### 4. 4 Diseño
Sea el criterio de calidad de servicio implementado: <br>
*Se desea que el 99% del tiempo no se presente una fila de 5 o más espacios de clientes que esperan a ser atendidos.* <br>

Si sólo hay un servidor entonces la función `t_servicio()` determina que tal servidor debe demorar 15 segundos como máximo en asistir a cada cliente para cumplir criterio.
En cambio, si se desea averiguar la cantidad mínima de servidores requeridos para satisfacer criterio con la intensidad de servicio con que el sistema cuenta actualmente la función `servidores()` encuentra que son 5, finalmente en caso de que se desee aumentar la cantidad de servidores a 3; gracias a la función `tiempo()` se ve que la implicación sería que cada cliente podría ser asistido 20 segundos.

## 5. Referencias
> Material de apoyo.<br>

1. Romero Chacón, J. *Modelos probabilísticos de señales y sistemas*.
