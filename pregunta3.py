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


