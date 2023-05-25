class Teletransportes:
    def __init__(self, matrix):
        self.matrix = matrix

    def matrix_power(self, k):
        # Función para elevar una matriz a la potencia k
        result = [row.copy() for row in self.matrix]  # Copia inicial de la matriz
        for _ in range(k - 1):
            temp = [[0] * len(self.matrix[0]) for _ in range(len(self.matrix))]  # Inicializar una matriz temporal de ceros
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    for m in range(len(self.matrix)):
                        temp[i][j] += result[i][m] * self.matrix[m][j]  # Realizar la multiplicación de matrices
            result = temp  # Actualizar el resultado con la matriz temporal
        return result

    def calcular_posibilidades(self, k):
        AGk = self.matrix_power(k)
        posibilidades = sum(sum(row) for row in AGk)  # Sumar todos los elementos de la matriz resultante
        return posibilidades


if __name__ == '__main__':

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

    teletransportes = Teletransportes(AG)
    k = int(input("Ingrese el número de movimientos: "))
    posibilidades = teletransportes.calcular_posibilidades(k)
    print("El número de teletransportes válidos con", k, "movimientos es:", posibilidades)
