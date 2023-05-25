class TableroPokebolas:
    def __init__(self, n):
        self.n = n
        self.tablero = [-1] * n

    def es_seguro(self, fila, columna):
        # Verifica si la posición es segura (no hay conflictos)
        for i in range(fila):
            # Verifica si hay una pokebola en la misma columna o en la misma diagonal
            if self.tablero[i] == columna or abs(self.tablero[i] - columna) == abs(i - fila):
                return False

        return True

    def coloca_pokebolas(self, fila):
        if fila == self.n:
            return True

        for columna in range(self.n):
            if self.es_seguro(fila, columna):
                self.tablero[fila] = columna

                if self.coloca_pokebolas(fila + 1):
                    return True

                # Retroceder (backtrack)
                self.tablero[fila] = -1

        return False

    def resuelve_puzzle_pokebolas(self):
        if self.coloca_pokebolas(0) is False:
            print("No hay solución")
            return False

        print(self.tablero)
        return True


if __name__ == '__main__':
    
    n = int(input("Ingrese el número de pokebolas: "))
    tablero_pokebolas = TableroPokebolas(n)
    tablero_pokebolas.resuelve_puzzle_pokebolas()