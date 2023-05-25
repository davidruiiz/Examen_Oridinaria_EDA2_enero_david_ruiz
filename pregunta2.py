import random
import unittest

class Nodo(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Pokemon:
    def __init__(self, nombre, tipo, nivel):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel
        print(f"Se ha creado con éxito el Pokemon {self.nombre} de tipo {self.tipo} y nivel {self.nivel}.")
