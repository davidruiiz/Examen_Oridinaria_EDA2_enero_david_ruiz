class Pokemon:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        print(f"Se ha creado el Pokemon {self.nombre} de tipo {self.tipo}.")

    def clasificacion(self):
        print("Clasificación del Pokemon:")
        print("- PS")
        print("- Ataque")
        print("- Defensa")
        print("- Ataque Especial")
        print("- Defensa Especial")
        print("- Velocidad")

if __name__ == "__main__":

    pokemon1 = Pokemon("Pikachu", "Eléctrico")
    pokemon1.clasificacion()
