Módulo de dimensionamiento
==========================

.. important::
   El número de servidores :math:`s` y el parámetro de tiempo de servicio :math:`\nu` pueden ser ajustados individualmente o en conjunto.

Se define una constante de proporcionalidad :math:`E` que depende de la probabilidad acumulada si se contara con :math:`s` servidores unicamente, para ello saca el complemento de la probabilidad que devuelve la función auxiliar :py:func:`cadena.dimensionamiento.probabilidades`.

.. math:: E = \frac{\phi_{L} + D -1}{D \phi_{L}}

Tal que :math:`E \phi_{L} = \frac{P}{100}` donde :math:`D` es la proporción de probabilidades entre criterio y obtenida con :math:`s` servidores y :math:`P` es el porcentaje de probabilidad que define el usuario.

.. automodule:: cadena.dimensionamiento
   :members:
   :undoc-members:
   :show-inheritance:
