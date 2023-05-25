def es_seguro(tablero, fila, columna):
    # Verifica si la posición está en la misma fila o columna
    for i in range(fila):
        if tablero[i] == columna or \
           abs(tablero[i] - columna) == abs(i - fila):
            return False

    return True

def n_pokebolas(tablero, fila, n):
    if fila == n:
        return True

    for columna in range(n):
        if es_seguro(tablero, fila, columna):
            tablero[fila] = columna

            if n_pokebolas(tablero, fila + 1, n):
                return True

            # Backtrack
            tablero[fila] = -1

    return False

def resuelve_n_pokebolas():
    n = int(input("Ingrese el número de reinas: "))
    tablero = [-1] * n
    if n_pokebolas(tablero, 0, n) is False:
        print("No hay solución")
        return False

    print(tablero)
    return True

if __name__ == '__main__':
    # Probamos la función
    resuelve_n_pokebolas()
