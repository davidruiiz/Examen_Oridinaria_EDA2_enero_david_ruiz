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


    def calificacion(self):
        if self.tipo == "Electrico":
            PS= 35
            Ataque= 55
            Defensa= 40
            Ataque_Especial= 50
            Defensa_Especial= 50
            Velocidad= 90
        elif self.tipo == "Fuego":
            PS= 39
            Ataque= 52
            Defensa= 43
            Ataque_Especial= 60
            Defensa_Especial= 50
            Velocidad= 65
        elif self.tipo == "Agua":
            PS= 44
            Ataque= 48
            Defensa= 65
            Ataque_Especial= 50
            Defensa_Especial= 64
            Velocidad= 43
        elif self.tipo == "Planta":
            PS= 45
            Ataque= 49
            Defensa= 49
            Ataque_Especial= 65
            Defensa_Especial= 65
            Velocidad= 45
        elif self.tipo == "Volador":
            PS= 40
            Ataque= 45
            Defensa= 40
            Ataque_Especial= 35
            Defensa_Especial= 35
            Velocidad= 56
        elif self.tipo == "Normal":
            PS= 30
            Ataque= 56
            Defensa= 35
            Ataque_Especial= 25
            Defensa_Especial= 35
            Velocidad= 72

        return f"La calificacion de {self.nombre} es {self.tipo}, por lo sus PS son {PS}, su Ataque es {Ataque}, su Defensa es {Defensa}, su Ataque Especial es {Ataque_Especial}, su Defensa Especial es {Defensa_Especial} y su Velocidad es {Velocidad}"

class ListaPokemon:
    def __init__(self):
        self.head = None

    def insertar(self, pokemon):
        new_node = Nodo(pokemon)
        if self.head is None:
            self.head = new_node
        elif self.head.data.nivel < pokemon.nivel:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None and current.next.data.nivel > pokemon.nivel:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def mostrar(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

class TestPokemon(unittest.TestCase):

    def setUp(self):
        self.pikachu = Pokemon("Pikachu", "Electrico", 2)
        self.charmander = Pokemon("Charmander", "Fuego", 5)
        self.squirtle = Pokemon("Squirtle", "Agua", 7)
        self.bulbasaur = Pokemon("Bulbasaur", "Planta", 9)
        self.pidgey = Pokemon("Pidgey", "Volador", random.randint(10, 100))

    def test_calificacion(self):
        self.assertEqual(self.pikachu.calificacion(), "La calificacion de Pikachu es Electrico, por lo sus PS son 35, su Ataque es 55, su Defensa es 40, su Ataque Especial es 50, su Defensa Especial es 50 y su Velocidad es 90")

if __name__ == '__main__':
    unittest.main()

# Crear una lista con un numero arbitrario de objetos tipo Pokemon
lista_pokemon = [
    Pokemon("Pikachu", "Electrico", 2),
    Pokemon("Charmander", "Fuego", 5),
    Pokemon("Squirtle", "Agua", 7),
    Pokemon("Bulbasaur", "Planta", 9),
    Pokemon("Pidgey", "Volador", random.randint(10, 100))
]

# Recorrer los elementos de la lista y ejecutar el metodo calificacion de cada objeto
for pokemon in lista_pokemon:
    print(pokemon.calificacion())
