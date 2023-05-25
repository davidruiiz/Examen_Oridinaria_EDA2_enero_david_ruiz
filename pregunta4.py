import unittest

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


class TestListaPokeball(unittest.TestCase):

    def setUp(self):
        self.pokeball1 = Pokeball(50, "Pokeball1", 10, "2021-01-01")
        self.pokeball2 = Pokeball(30, "Pokeball2", 5, "2021-02-01")
        self.pokeball3 = Pokeball(40, "Pokeball3", 8, "2021-03-01")

        self.lista_pokeball = ListaPokeball()

    def test_insertar(self):
        self.lista_pokeball.insertar(self.pokeball1)
        self.assertEqual(self.lista_pokeball.head.data, self.pokeball1)
        self.assertIsNone(self.lista_pokeball.head.next)

        self.lista_pokeball.insertar(self.pokeball2)
        self.assertEqual(self.lista_pokeball.head.data, self.pokeball2)
        self.assertEqual(self.lista_pokeball.head.next.data, self.pokeball1)
        self.assertIsNone(self.lista_pokeball.head.next.next)

        self.lista_pokeball.insertar(self.pokeball3)
        self.assertEqual(self.lista_pokeball.head.data, self.pokeball2)
        self.assertEqual(self.lista_pokeball.head.next.data, self.pokeball3)
        self.assertEqual(self.lista_pokeball.head.next.next.data, self.pokeball1)
        self.assertIsNone(self.lista_pokeball.head.next.next.next)

    def test_modificar(self):
        self.lista_pokeball.insertar(self.pokeball1)
        self.lista_pokeball.insertar(self.pokeball2)
        self.lista_pokeball.insertar(self.pokeball3)

        self.lista_pokeball.modificar(self.pokeball2, "peso", 35)
        self.assertEqual(self.lista_pokeball.head.next.data.peso, 35)

        self.lista_pokeball.modificar(self.pokeball1, "nombre", "NuevaPokeball")
        self.assertEqual(self.lista_pokeball.head.next.next.data.nombre, "NuevaPokeball")

        self.lista_pokeball.modificar(self.pokeball3, "precio", 15)
        self.assertEqual(self.lista_pokeball.head.next.data.precio, 15)

        self.lista_pokeball.modificar(self.pokeball2, "fecha_fabricacion", "2022-01-01")
        self.assertEqual(self.lista_pokeball.head.next.data.fecha_fabricacion, "2022-01-01")

    def test_mostrar(self):
        self.lista_pokeball.insertar(self.pokeball1)
        self.lista_pokeball.insertar(self.pokeball2)
        self.lista_pokeball.insertar(self.pokeball3)

        # Redirigir la salida estándar a un StringIO para capturar la salida
        from io import StringIO
        import sys
        captured_output = StringIO()
        sys.stdout = captured_output

        self.lista_pokeball.mostrar()

        sys.stdout = sys.__stdout__  # Restaurar la salida estándar

        expected_output = "La pokeball Pokeball2 pesa 30 gramos y cuesta 5 pesos\n" \
                          "La pokeball Pokeball3 pesa 40 gramos y cuesta 8 pesos\n" \
                          "La pokeball Pokeball1 pesa 50 gramos y cuesta 10 pesos\n"
        self.assertEqual(captured_output.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
