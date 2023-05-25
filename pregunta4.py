import unittest
import datetime

class Nodo(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Pokeball:

    def __init__(self, peso, nombre, precio, fecha_fabricacion):
        self.peso = peso
        self.nombre = nombre
        self.precio = precio
        self.fecha_fabricacion = fecha_fabricacion
        print("Se ha creado una pokeball exitosamente")

    def __str__(self):
        return f"La pokeball {self.nombre} pesa {self.peso} gramos y cuesta {self.precio} pesos"

class ListaPokeball:

    def __init__(self):
        self.head = None

    def insertar(self, pokeball):
        nuevo_nodo = Nodo(pokeball)
        if self.head is None:
            self.head = nuevo_nodo
        elif self.head.data.fecha_fabricacion > pokeball.fecha_fabricacion:
            nuevo_nodo.next = self.head
            self.head = nuevo_nodo
        else:
            actual = self.head
            while actual.next and actual.next.data.fecha_fabricacion < pokeball.fecha_fabricacion:
                actual = actual.next
            nuevo_nodo.next = actual.next
            actual.next = nuevo_nodo

    def mostrar(self):
        actual = self.head
        while actual:
            print(actual.data)
            actual = actual.next

    def modificar(self, pokeball, caracteristica, valor):
        actual = self.head
        while actual and actual.data.nombre != pokeball.nombre:
            actual = actual.next
        if actual:
            if caracteristica == "peso":
                actual.data.peso = valor
            elif caracteristica == "nombre":
                actual.data.nombre = valor
            elif caracteristica == "precio":
                actual.data.precio = valor
            elif caracteristica == "fecha_fabricacion":
                actual.data.fecha_fabricacion = valor
            else:
                print("Característica no encontrada")
        else:
            print("Pokeball no encontrada")


# creamos algunas pokeballs
pokeball1 = Pokeball(100, "Superball", 200, datetime.datetime(2023, 5, 10))
pokeball2 = Pokeball(80, "Ultraball", 300, datetime.datetime(2023, 4, 20))
pokeball3 = Pokeball(120, "Masterball", 500, datetime.datetime(2023, 6, 5))

# mostramos las pokeballs ordenadas por fecha de fabricación
lista_pokeballs = ListaPokeball()
lista_pokeballs.insertar(pokeball1)
lista_pokeballs.insertar(pokeball2)
lista_pokeballs.insertar(pokeball3)
lista_pokeballs.mostrar()

# modificamos el precio de una pokeball
lista_pokeballs.modificar(pokeball2, "precio", 350)
lista_pokeballs.mostrar()

# Experimentación


class Test(unittest.TestCase):

    def setUp(self):
        self.pokeball1 = Pokeball(100, "Superball", 200, datetime.datetime(2023, 5, 10))
        self.pokeball2 = Pokeball(80, "Ultraball", 300, datetime.datetime(2023, 4, 20))
        self.pokeball3 = Pokeball(120, "Masterball", 500, datetime.datetime(2023, 6, 5))
        self.lista_pokeballs = ListaPokeball()
        self.lista_pokeballs.insertar(self.pokeball1)
        self.lista_pokeballs.insertar(self.pokeball2)
        self.lista_pokeballs.insertar(self.pokeball3)

    def test_insertar(self):
        self.assertEqual(self.lista_pokeballs.head.data, self.pokeball2)
        self.assertEqual(self.lista_pokeballs.head.next.data, self.pokeball1)
        self.assertEqual(self.lista_pokeballs.head.next.next.data, self.pokeball3)

    def test_modificar(self):
        self.lista_pokeballs.modificar(self.pokeball2, "precio", 350)
        self.assertEqual(self.lista_pokeballs.head.next.data.precio, 350)

if __name__ == "__main__":
    unittest.main()