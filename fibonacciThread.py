from threading import Thread
from time import time
from fibonacci import fibo  #Importamos la función fibo desde el archivo fibonacci.py
import statistics  # Nuevo: Para calcular el promedio

# Nuevo: Función para calcular el promedio de los tiempos, excluyendo el más alto y el más bajo
def calculate_average_time(times):
    sorted_times = sorted(times)
    return statistics.mean(sorted_times[1:-1])

# Clase para crear un hilo que procese 12 elementos del vector
class FiboWorker(Thread):
    def __init__(self, vector, start_idx, end_idx, thread_id):
        Thread.__init__(self)
        self.vector = vector
        self.start_idx = start_idx
        self.end_idx = end_idx
        self.thread_id = thread_id

    def run(self):
        for i in range(self.start_idx, self.end_idx):
            print(f"Thread {self.thread_id} procesando posición {i}, valor {self.vector[i]}")
            self.vector[i] = fibo(self.vector[i])
            print(f"Thread {self.thread_id} calculó Fibonacci para posición {i}: {self.vector[i]}")

# Nuevo: Función que contiene la lógica principal del cálculo con hilos
def run_fibonacci():
    vector_size = 144
    vector = [33] * vector_size  #Se inicializa un vector con 144 posiciones de valor 33
    num_threads = 12
    elements_per_thread = vector_size // num_threads

    threads = []  #Lista para manejar los hilos
    ts = time()  #Tomamos el tiempo de inicio

    #Crear y arranca 12 hilos, cada uno procesando 12 elementos del vector
    for i in range(num_threads):
        start_idx = i * elements_per_thread
        end_idx = start_idx + elements_per_thread
        thread = FiboWorker(vector, start_idx, end_idx, i)
        thread.start()
        threads.append(thread)

    #Espera a que todos los hilos terminen
    for thread in threads:
        thread.join()

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