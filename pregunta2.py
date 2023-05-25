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

    def __str__(self):
        return "Lo que quiero mostrar"
    
    def __repr__(self):
        return f"Pokemon: ({self.name},  Tipo: {self.tipo})"
    
    def calificacion(self, tipo):
        if self.tipo == "Fuego":
            PS = 60
            Ataque = 65
            Defensa = 55
            Ataque_Especial = 70
            Defensa_Especial = 60
            Velocidad = 80
        elif self.tipo == "Agua":
            PS = 70
            Ataque = 60
            Defensa = 75
            Ataque_Especial = 55
            Defensa_Especial = 70
            Velocidad = 50
        elif self.tipo == "Planta":
            PS = 65
            Ataque = 55
            Defensa = 60
            Ataque_Especial = 70
            Defensa_Especial = 65
            Velocidad = 45
        elif self.tipo == "Normal":
            PS = 45
            Ataque = 70
            Defensa = 50
            Ataque_Especial = 35
            Defensa_Especial = 50
            Velocidad = 85
        elif self.tipo == "Volador":
            PS = 50
            Ataque = 45
            Defensa = 50
            Ataque_Especial = 40
            Defensa_Especial = 40
            Velocidad = 70
        elif self.tipo == "Eléctrico":
            PS = 55
            Ataque = 70
            Defensa = 60
            Ataque_Especial = 65
            Defensa_Especial = 65
            Velocidad = 95

        return f"La calificación de {self.nombre} es {self.tipo}, por lo que sus PS son {PS}, su Ataque es {Ataque}, su Defensa es {Defensa}, su Ataque Especial es {Ataque_Especial}, su Defensa Especial es {Defensa_Especial} y su Velocidad es {Velocidad}"

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
        self.pokemon1 = Pokemon("Charizard", "Fuego", 60)
        self.pokemon2 = Pokemon("Blastoise", "Agua", 70)
        self.pokemon3 = Pokemon("Venusaur", "Planta", 65)
        self.pokemon4 = Pokemon("Pidgeot", "Volador", 50)
        self.pokemon5 = Pokemon("Pikachu", "Eléctrico", 55)

    def test_calificacion_fuego(self):
        expected_output = "La calificación de Charizard es Fuego, por lo que sus PS son 60, su Ataque es 65, su Defensa es 55, su Ataque Especial es 70, su Defensa Especial es 60 y su Velocidad es 80"
        self.assertEqual(self.pokemon1.calificacion("Fuego"), expected_output)

    def test_calificacion_agua(self):
        expected_output = "La calificación de Blastoise es Agua, por lo que sus PS son 70, su Ataque es 60, su Defensa es 75, su Ataque Especial es 55, su Defensa Especial es 70 y su Velocidad es 50"
        self.assertEqual(self.pokemon2.calificacion("Agua"), expected_output)

    def test_calificacion_planta(self):
        expected_output = "La calificación de Venusaur es Planta, por lo que sus PS son 65, su Ataque es 55, su Defensa es 60, su Ataque Especial es 70, su Defensa Especial es 65 y su Velocidad es 45"
        self.assertEqual(self.pokemon3.calificacion("Planta"), expected_output)

    def test_calificacion_volador(self):
        expected_output = "La calificación de Pidgeot es Volador, por lo que sus PS son 50, su Ataque es 45, su Defensa es 50, su Ataque Especial es 40, su Defensa Especial es 40 y su Velocidad es 70"
        self.assertEqual(self.pokemon4.calificacion("Volador"), expected_output)

    def test_calificacion_electrico(self):
        expected_output = "La calificación de Pikachu es Eléctrico, por lo que sus PS son 55, su Ataque es 70, su Defensa es 60, su Ataque Especial es 65, su Defensa Especial es 65 y su Velocidad es 95"
        self.assertEqual(self.pokemon5.calificacion("Eléctrico"), expected_output)

if __name__ == "__main__":
    unittest.main()
