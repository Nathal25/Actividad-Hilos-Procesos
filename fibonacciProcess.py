from multiprocessing import Process
from time import time
from fibonacci import fibo  # Importamos la función fibo desde el archivo fibonacci.py
import statistics  # Nuevo: Para calcular el promedio

# Nuevo: Función para calcular el promedio de los tiempos, excluyendo el más alto y el más bajo
def calculate_average_time(times):
    sorted_times = sorted(times)
    return statistics.mean(sorted_times[1:-1])

# Clase para crear un proceso que calcule el Fibonacci en una posición específica
class FiboWorker(Process):
    def __init__(self, vector, index):
        Process.__init__(self)
        self.vector = vector
        self.index = index

    def run(self):
        print(f"Proceso {self.index}: Calculando Fibonacci para la posición {self.index}, valor {self.vector[self.index]}")
        self.vector[self.index] = fibo(self.vector[self.index])
        print(f"Proceso {self.index}: Fibonacci calculado y almacenado en la posición {self.index}")

# Nuevo: Función que contiene la lógica principal del cálculo con procesos
def run_fibonacci():
    vector_size = 144
    vector = [33] * vector_size  #Inicializa un vector con 144 posiciones de valor 33

    processes = []  #Lista para manejar los procesos
    ts = time()  #Toma el tiempo de inicio

    #Crea y arranca un proceso por cada posición del vector
    for i in range(vector_size):
        process = FiboWorker(vector, i)
        process.start()
        processes.append(process)

    #Espera a que todos los procesos terminen
    for process in processes:
        process.join()

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