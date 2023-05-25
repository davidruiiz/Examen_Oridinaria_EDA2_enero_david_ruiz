# Matriz de adyacencia del grafo

AG = [[0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
      [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
      [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
      [0, 0, 1, 0, 0, 0, 0, 0, 1, 1],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
      [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
      [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
      [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 1, 0, 1, 0, 0, 0, 0]]

def matrix_power(matrix, k):
    # Función para elevar una matriz a la potencia k
    result = [row.copy() for row in matrix]  # Copia inicial de la matriz
    for _ in range(k - 1):
        temp = [[0] * len(matrix[0]) for _ in range(len(matrix))]  # Inicializar una matriz temporal de ceros
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                for m in range(len(matrix)):
                    temp[i][j] += result[i][m] * matrix[m][j]  # Realizar la multiplicación de matrices
        result = temp  # Actualizar el resultado con la matriz temporal
    return result

def teletransportes():
    k = int(input("Ingrese el número de movimientos: "))
    AGk = matrix_power(AG, k)
    posibilidades = sum(sum(row) for row in AGk)  # Sumar todos los elementos de la matriz resultante
    print("El número de teletransportes válidos con", k, "movimientos es: ")
    return posibilidades

if __name__ == '__main__':
    print(teletransportes())
