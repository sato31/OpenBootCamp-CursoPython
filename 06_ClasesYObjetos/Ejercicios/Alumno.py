# En este segundo ejercicio, tendréis que crear un programa que tenga una clase 
# llamada Alumno que tenga como atributos su nombre y su nota. 
# Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y 
# mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Alumno:

    def inicializaAlumno(self, nombre, nota):   # Se inicializan los atributos con un método
        self.nombre = nombre
        self.nota = nota
    
    def imprimeAlumno(self):           
        print("Nombre: ", self.nombre)
        print("Nota:", self.nota)
    
    def resultadosAlumno(self):
        if self.nota >= 6:
            print("El alunmo", self.nombre, "ha aprobado")
        else:
            print("El alumno", self.nombre, "ha reprobado")

alumno1 = Alumno()  # Se crean 2 instancias de la clase alumno
alumno2 = Alumno()

alumno1.inicializaAlumno("Luis", 5.99)  # Se le pasan los parametros de cada alumno
alumno2.inicializaAlumno("Carlos", 8)

alumno1.imprimeAlumno()     # Imprime los valores y resultado del primer alumno.
alumno1.resultadosAlumno()

alumno2.imprimeAlumno()     # Imprime los valores y resultado del segundo alumno.
alumno2.resultadosAlumno()