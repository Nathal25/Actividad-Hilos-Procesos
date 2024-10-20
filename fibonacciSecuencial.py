from time import time
from fibonacci import fibo  # Importamos la función fibo desde el archivo fibonacci.py
import statistics  # Nuevo: Para calcular el promedio

# Nuevo: Función para calcular el promedio de los tiempos, excluyendo el más alto y el más bajo
def calculate_average_time(times):
    sorted_times = sorted(times)
    return statistics.mean(sorted_times[1:-1])

# Nuevo: Función que contiene la lógica principal del cálculo secuencial
def run_fibonacci():
    vector_size = 144
    vector = [33] * vector_size  #Se inicializa un vector con 144 posiciones de valor 33

    ts = time()  #Tomamos el tiempo de inicio

    #El ciclo calcula el valor de Fibonacci para cada posición del vector
    for i in range(vector_size):
        print(f"Calculando Fibonacci para la posición {i}, valor {vector[i]}")
        vector[i] = fibo(vector[i])
        print(f"Fibonacci de {vector[i]} calculado y almacenado en la posición {i}")

    execution_time = time() - ts
    print(f"Vector después de calcular Fibonacci: {vector}")
    return execution_time  # Nuevo: Retornamos el tiempo de ejecución

def main():
    num_runs = 5  # Nuevo: Número de ejecuciones
    execution_times = []  # Nuevo: Lista para almacenar los tiempos de ejecución

    for i in range(num_runs):
        print(f"\nEjecución {i+1}:")
        execution_time = run_fibonacci()
        execution_times.append(execution_time)
        print(f"Tiempo de ejecución: {execution_time:.5f} segundos")

    average_time = calculate_average_time(execution_times)

    print(f"\nTiempos de ejecución: {execution_times}")
    print(f"Promedio de los 3 tiempos centrales: {average_time:.5f} segundos")

if __name__ == "__main__":
    main()