    # CREACIÓN DE LA CLASE
class Dino:
    _encendido = True           # ATRIBUTOS

    def enciende(self):         # METODOS
        self._encendido = True

    def apaga(self):
        self._encendido = False
    
    def isEncendido(self):
        return self._encendido

    # SE CREA UN OBJETO (UNA INSTANCIA DE LA CLASE)
dinosaurio1 = Dino()
    # SE USA EL METODO apaga EN EL OBJETO dinosaurio1
dinosaurio1.apaga()
    # SE HACE USO DE UN METODO QUE DEVUELVE EL VALOR DE UN ATRIBUTO DEL OBJETO 
print(dinosaurio1.isEncendido())

dinosaurio2 = Dino()
dinosaurio2.enciende()
print(dinosaurio2.isEncendido())


#   CLASE ESTATICA
class Estatica:
    numero = 1

    def incrementa():
        Estatica.numero += 1

Estatica.incrementa()
print(Estatica.numero)
