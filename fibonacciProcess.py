from multiprocessing import Process
from time import time
from fibonacci import fibo  # Importamos la función fibo desde el archivo fibonacci.py

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

def main():
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

    print(f"Vector después de calcular Fibonacci: {vector}")
    print(f"Tiempo total: {time() - ts}")

if __name__ == "__main__":
    main()
