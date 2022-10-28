# CLASES ABSTRACTAS =>  DEFINNE UNA SERIE DE FUNCIONES QUE SERÁN COMUNES A OTRAS CLASES
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sonido(self):   # Metodo Abstracto
        pass

    def diHola(self):
        print("Hola")

# a = Animal()    # ERROR => Las clases abstractas no se pueden instanciar

class Perro(Animal):
    def sonido(self):
        print("Guau")

class Gato(Animal):
    def sonido(self):
        print("Miau")

p = Perro()
p.sonido()
p.diHola()

g = Gato()
g.sonido()
g.diHola()