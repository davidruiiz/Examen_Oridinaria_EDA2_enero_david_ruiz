class Grafo:
    def __init__(self):
        self.vertices = {}

    def agregar_tarea(self, tarea, duracion):
        self.vertices[tarea] = []

    def agregar_conexion(self, tarea_origen, tarea_destino, duracion):
        if tarea_origen in self.vertices and tarea_destino in self.vertices:
            self.vertices[tarea_origen].append((tarea_destino, duracion))

    def obtener_minimo(self, distancias, visitados):
        minimo = float('inf')
        minimo_tarea = None

        for tarea in self.vertices:
            if not visitados[tarea] and distancias[tarea] < minimo:
                minimo = distancias[tarea]
                minimo_tarea = tarea

        return minimo_tarea

    def dijkstra(self, tarea_inicial):
        distancias = {tarea: float('inf') for tarea in self.vertices}
        distancias[tarea_inicial] = 0
        visitados = {tarea: False for tarea in self.vertices}

        for _ in range(len(self.vertices)):
            tarea_actual = self.obtener_minimo(distancias, visitados)
            visitados[tarea_actual] = True

            if tarea_actual is None:
                break

            for tarea_siguiente, duracion_arista in self.vertices[tarea_actual]:
                distancia = distancias[tarea_actual] + duracion_arista
                if not visitados[tarea_siguiente] and distancia < distancias[tarea_siguiente]:
                    distancias[tarea_siguiente] = distancia

        return distancias

if __name__ == '__main__':
    
    # Crear el grafo y agregar las tareas con sus respectivas duraciones
    grafo = Grafo()
    grafo.agregar_tarea('A', 20)
    grafo.agregar_tarea('B', 5)
    grafo.agregar_tarea('C', 40)
    grafo.agregar_tarea('D', 10)
    grafo.agregar_tarea('E', 5)
    grafo.agregar_tarea('F', 10)
    grafo.agregar_tarea('G', 20)
    grafo.agregar_tarea('H', 25)
    grafo.agregar_tarea('I', 35)
    grafo.agregar_tarea('J', 25)
    grafo.agregar_tarea('K', 15)
    grafo.agregar_tarea('L', 5)
    grafo.agregar_tarea('M', 25)

    # Agregar las conexiones entre tareas
    grafo.agregar_conexion('A', 'B', 5)
    grafo.agregar_conexion('B', 'C', 40)
    grafo.agregar_conexion('B', 'G', 20)
    grafo.agregar_conexion('C', 'H', 25)
    grafo.agregar_conexion('C', 'J', 25)
    grafo.agregar_conexion('C', 'K', 15)
    grafo.agregar_conexion('C', 'L', 5)
    grafo.agregar_conexion('D', 'F', 10)
    grafo.agregar_conexion('E', 'F', 10)
    grafo.agregar_conexion('G', 'H', 25)
    grafo.agregar_conexion('H', 'I', 35)
    grafo.agregar_conexion('I', 'M', 25)

    # Ejecutar el algoritmo de Dijkstra
    camino_mas_corto = grafo.dijkstra('A')

    # Ordenar las tareas por duración en orden ascendente
    camino_mas_corto = sorted(camino_mas_corto.items(), key=lambda x: x[1])

    # Imprimir el camino más corto para completar las tareas
    print("Camino más corto para completar las tareas:")
    for tarea, duracion in camino_mas_corto:
        print(f"Tarea: {tarea}, Duración: {duracion} minutos")

    # Obtener la duración mínima de la misión
    duracion_minima = max(camino_mas_corto, key=lambda x: x[1])[1]
    print(f"Duración mínima de la misión: {duracion_minima} minutos")
