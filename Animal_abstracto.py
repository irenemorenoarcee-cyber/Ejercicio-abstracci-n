from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

        @abstractmethod
        def hacer_ruido(self):
            pass

        @abstractmethod
        def moverse(self):
            pass

        def presentarse(self):
            return f"Soy {self.nombre}, {self.hacer_ruido()}, y {self.moverse()}"

class Perro(Animal):
    def hacer_ruido(self):
        return "GUAU"
    def moverse(self):
        return "Me muevo a cuatro patas"

class Ave(Animal):
    def hacer_ruido(self):
        return "Pío Pio"
    def moverse(self):
        return "Vuelo"
 
for Animal in [Perro("Winnie"), Ave("Piolín")]:
    print(Animal.presentarse())
