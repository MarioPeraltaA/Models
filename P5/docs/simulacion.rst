Módulo de simulación
====================

.. warning::
    El resultado de esta simulación es distinto a los datos de prueba utilizados para encontrar los _`parámetros` en el módulo de análisis no obstante, los parámetros :math:`\lambda` y :math:`\nu` son los mismo.

.. note::

    - Para que exista un estado estable, la tasa de partidas debe ser mayor que la de llegadas.
    - En una cola, solamente un movimiento o cambio de estado ocurre a la vez.

Los parámetros :math:`\lambda` y :math:`\nu` que recibe son los que devuelven respectivamente las funciones:

- :func:`cadena.analisis.llegada`
- :func:`cadena.analisis.servicio`

.. automodule:: cadena.simulacion
   :members:
   :undoc-members:
   :show-inheritance:

Ver los resultados de la simulación en :ref:`Simulación de sistema M/M/1 <simulacion>`