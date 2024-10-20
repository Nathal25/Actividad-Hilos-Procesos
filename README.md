# SO-Actividad-Hilos-Procesos

En este repositorio se encuentran los códigos que permiten procesar los elementos de un vector de longitud 144.
El programa calcula el valor de Fibonacci para cada una de las posiciones del vector (Inicializadas con el valor 33).

## Conclusiones

Después de realizar las ejecuciones de las tres versiones del programa (Secuencial, con Hilos, con Procesos), los tiempos promedio, eliminando el tiempo más alto y más bajo, fueron los siguientes:

- Versión Secuencial: 225.0253382436676 segundos.
- Versión con Hilos:  234.3737680912018 segundos.
- Versión con Procesos: 268.336030403773 segundos.

 ## Versión con Thread.

-El vector mostrará 144 veces el número 3524578 (que es el 33º número de Fibonacci).

-El tiempo total será el tiempo que tomó ejecutar todo el proceso, en segundos.

-El tiempo de ejecución variará dependiendo de la potencia de procesamiento de la máquina, pero debería ser significativamente menor que la versión secuencial debido al paralelismo.

Es importante notar que:

-El orden exacto de los mensajes de los hilos puede variar en cada ejecución debido a la naturaleza concurrente del programa.

-Aunque los hilos se ejecutan en paralelo, el cálculo de Fibonacci para cada número es intensivo, por lo que aún puede tomar un tiempo considerable.

-La salida final (el vector y el tiempo) será consistente entre ejecuciones, pero el tiempo puede variar ligeramente

 ## Versión con Process.

-El vector mostrará 144 veces el número 3524578 (que es el 33º número de Fibonacci).

-El tiempo total será el tiempo que tomó ejecutar todo el proceso, en segundos.

-Es importante notar algunas diferencias clave con respecto a la versión de hilos:

-Orden de ejecución: Debido a que cada elemento tiene su propio proceso, el orden de los mensajes puede ser aún más aleatorio que en la versión con hilos.

-Rendimiento: Dependiendo del sistema, esta versión podría ser más rápida o más lenta que la versión con hilos. Los procesos tienen más sobrecarga que los hilos, pero también pueden aprovechar mejor los sistemas con múltiples núcleos o procesadores.

-Uso de recursos: Esta implementación utilizará significativamente más recursos del sistema que la versión con hilos, ya que cada proceso tiene su propio espacio de memoria.

-Consistencia: Al igual que con los hilos, el resultado final (el vector) será consistente entre ejecuciones, pero el tiempo y el orden de los mensajes pueden variar.

 ## Versión Secuencial:

-El vector mostrará 144 veces el número 3524578 (que es el 33º número de Fibonacci).

-El tiempo total será el tiempo que tomó ejecutar todo el proceso, en segundos.

-Es importante notar algunas diferencias clave con respecto a las versiones de hilos y procesos:

-Orden de ejecución: Los mensajes aparecerán en orden estricto, desde la posición 0 hasta la 143, sin entremezclarse.

-Rendimiento: Esta versión será significativamente más lenta que las versiones paralelas (hilos y procesos) en sistemas con múltiples núcleos, ya que no aprovecha el paralelismo.

-Uso de recursos: Esta implementación utilizará menos recursos del sistema que las versiones paralelas, ya que solo se está ejecutando un hilo/proceso a la vez.

-Consistencia: El resultado final (el vector) y el orden de los mensajes serán idénticos en cada ejecución. Solo el tiempo total podría variar ligeramente.

-Simplicidad: Esta versión es la más simple de entender y depurar, ya que no hay complejidades adicionales introducidas por la concurrencia o el paralelismo.
