Módulo de análisis
==================

.. important:: Ningún estado es absorbente.

    - Los datos analizados especifican el tiempo de llegada (en segundos desde el inicio de la simulación) de los primeros  𝑁  clientes de un sistema, el intervalo de tiempo (segundos) entre el cliente y el anterior y la duración del servicio (segundos) prestado a cada uno.
    - Los estados son: :math:`i \geq 0` y el sistema posee cantidad **indefinida** de estados posibles (después del estado estable siempre puede generar cola), pero no infinitos.

.. automodule:: cadena.analisis
   :members:
   :undoc-members:
   :show-inheritance:
