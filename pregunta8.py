class NodoHuffman:
    def __init__(self, caracter, frecuencia, izquierdo=None, derecho=None):
        self.caracter = caracter
        self.frecuencia = frecuencia
        self.izquierdo = izquierdo
        self.derecho = derecho

    def __lt__(self, other):
        return self.frecuencia < other.frecuencia

    @staticmethod
    def construir_arbol_huffman(frecuencias):
        nodos = []
        for caracter, frecuencia in frecuencias.items():
            nodos.append(NodoHuffman(caracter, frecuencia))
        while len(nodos) > 1:
            nodos.sort(key=lambda x: x.frecuencia)
            nodo_izquierdo = nodos.pop(0)
            nodo_derecho = nodos.pop(0)
            nodo_padre = NodoHuffman(None, nodo_izquierdo.frecuencia + nodo_derecho.frecuencia)
            nodo_padre.izquierdo = nodo_izquierdo
            nodo_padre.derecho = nodo_derecho
            nodos.append(nodo_padre)
        return nodos[0]

    def codificar_mensaje(self, mensaje):
        codificacion = {}
        self.generar_codificacion(self, '', codificacion)
        mensaje_codificado = ''
        for caracter in mensaje:
            mensaje_codificado += codificacion[caracter]
        return mensaje_codificado

    def generar_codificacion(self, nodo, codigo_actual, codificacion):
        if nodo.caracter is not None:
            codificacion[nodo.caracter] = codigo_actual
        else:
            self.generar_codificacion(nodo.izquierdo, codigo_actual + '0', codificacion)
            self.generar_codificacion(nodo.derecho, codigo_actual + '1', codificacion)

    def decodificar_mensaje(self, mensaje_codificado):
        mensaje_decodificado = ''
        nodo_actual = self
        for bit in mensaje_codificado:
            if bit == '0':
                nodo_actual = nodo_actual.izquierdo
            else:
                nodo_actual = nodo_actual.derecho
            if nodo_actual.caracter is not None:
                mensaje_decodificado += nodo_actual.caracter
                nodo_actual = self
        return mensaje_decodificado

def espacio_ocupado(frecuencias, mensaje_codificado):
    return len(frecuencias) * 8 + len(mensaje_codificado) / 8


# Experimentación:

if __name__ == "__main__":
    
    frecuencias = {'T': 0.15, 'O': 0.15, 'A': 0.12, 'E': 0.10, 'H': 0.09, 'S':0.07, 'P': 0.07, 'M': 0.07, 'N': 0.06, 'C': 0.06, 'D': 0.05, 'Z': 0.04, 'K': 0.03, ',': 0.03}
    mensaje = "HAZTE,CON,TODOS,POKEMON"
    arbol_huffman = NodoHuffman.construir_arbol_huffman(frecuencias)
    mensaje_codificado = arbol_huffman.codificar_mensaje(mensaje)
    mensaje_decodificado = arbol_huffman.decodificar_mensaje(mensaje_codificado)
    print(f"Mensaje original: {mensaje}")
    print(f"Mensaje codificado: {mensaje_codificado}")
    print(f"Mensaje decodificado: {mensaje_decodificado}")
    print(f"Espacio ocupado: {espacio_ocupado(frecuencias, mensaje_codificado)} bytes")
