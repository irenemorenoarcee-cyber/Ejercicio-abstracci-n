class Animal:
    def __init__(self, nombre_animal):
        self.nombre = nombre_animal

    def hacer_ruido(self):    
        print("Hacer ruido")

class Perro(Animal):
    def __init__(self, nombre_perro, raza, color):
        self.nombre = nombre_perro
        self.raza = raza
        self.color = color
    def pasear_perro(self):
        print("Sacar perro a pasear")
    def hacer_ruido(self):
            print("Hacer GUAU")
    
class Gato(Animal):
    def __init__(self, nombre_gato, raza):
        self.nombre = nombre_gato
        self.raza = raza
    def hacer_ruido(self):
        print("Hacer miau")
class Pez(Animal):
    pass

granja = [Perro("Winnie", "Teckle", "Negro"), Gato("Tera", "Común"), Pez("Nemo")]

for Animal in granja:
    Animal.hacer_ruido()

