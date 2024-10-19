from threading import Thread
from time import time
from fibonacci import fibo  #Importamos la función fibo desde el archivo fibonacci.py

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

def main():
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

    print(f"Vector después de calcular Fibonacci: {vector}")
    print(f"Tiempo total: {time() - ts}")

if __name__ == "__main__":
    main()
