
    # HERENCIA
class Juguete:
    _encendido = True           # ATRIBUTOS

    def __init__(self):
        print("Estoy en el constructor de la clase juguete")

    def enciende(self):         # METODOS
        print("Enciendo el aparato")
        self._encendido = True

    def apaga(self):
        print("Apago el aparato")
        self._encendido = False
    
    def isEncendido(self):
        return self._encendido

class Potato(Juguete):      # Potato Hereda de Juguete
    def quitarOreja(self):
        pass

    def ponerOreja(self):
        pass

p = Potato()
p.enciende()
print(p.isEncendido())
p.apaga()
print(p.isEncendido())


# class Dino(Potato, Juguete):    # Herencia Multiple
class Dino(Juguete):
    color = None
    nombre = None

    def __init__(self, nombre):     # Se declara el constructor
        # Juguete.__init__(self)
        super().__init__(nombre)
        print("Estoy en el constructor de la clase Dino()")

    def __del__(self):          # Destructor => Se invoca cuando no hay mas referencias a la clase
        print("Estoy en el destructor de la clase", self.__class__)

    def verEscamas(self):
        pass

p = Dino("midnosaurio") 