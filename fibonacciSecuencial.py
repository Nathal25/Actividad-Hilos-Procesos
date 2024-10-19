from time import time
from fibonacci import fibo  # Importamos la función fibo desde el archivo fibonacci.py

def main():
    vector_size = 144
    vector = [33] * vector_size  #Se inicializa un vector con 144 posiciones de valor 33

    ts = time()  #Tomamos el tiempo de inicio

    #El ciclo calcula el valor de Fibonacci para cada posición del vector
    for i in range(vector_size):
        print(f"Calculando Fibonacci para la posición {i}, valor {vector[i]}")
        vector[i] = fibo(vector[i])
        print(f"Fibonacci de {vector[i]} calculado y almacenado en la posición {i}")

    print(f"Vector después de calcular Fibonacci: {vector}")
    print(f"Tiempo total: {time() - ts}")

if __name__ == "__main__":
    main()
