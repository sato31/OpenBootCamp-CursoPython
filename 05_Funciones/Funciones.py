#   FUNCI
# ÓN SIN PARÁMETROS
def miFuncion():
    print("Nombre")

miFuncion()


#   FUNCIÓN CON PARAMETROS
def funcionConParametros(nombre):
    print("Hola", nombre)

funcionConParametros("Victor")


#   FUNCIONES DENTRO DE UNA FUNCIÓN
def matematicas(a, b):
    def suma( a, b ):
        print ( a + b )
    def resta( a, b ):
        print( a - b )

    suma( a, b )
    resta( a, b )

matematicas(5, 3)


#   AMBITO DE LAS VARIABLES
#   VARIABLES DECLARADAS DENTRO DE LA FUNCIÓN SOLO SE PUEDEN UTILIZAR DENTRO DE LA FUNCIÓN
def mifuncionvar(nombre):
    hoyHace = 6.0
    print("Hola,", nombre, "la temperatura es de", hoyHace)

mifuncionvar("Victor")


#   VARIABLES GLOBALES
#   SE PUEDEN USAR DENTRO Y FUERA DE LA FUNCIÓN
temperatura = 12.0
def mifunciontempe(nombre):
    print("Hola,", nombre, "la temperatura es de", temperatura)

mifunciontempe("Victor")


#   VARIABLE SHADOWING
#   CUANDO EXISTE UNA VARIABLE GLOBAL Y SE DECLARA DENTRO DE UNA FUNCIÓN UNA VARIABLE CON
#   EL MISMO NOMBRE, ESTA SOLO CAMBIA DE VALOR MIENTRAS SE USA EN LA FUNCIÓN, CUANDO SE SALE
#   DE LA FUNCIÓN ESTA VUELVE A TOMAR EL VALOR QUE TENIA ANTES DE LA INVOCACIÓN DE LA FUNCIÓN.
hoyHace = 12.0
def mifuncionshad(nombre):
    # global hoyHace    #Se puede declarar global dentro de la función para evitar el shadowing
    hoyHace = 6.0
    print("Hola,", nombre, "la temperatura es de", hoyHace)

mifuncionshad("Victor")
print(hoyHace)


#   PARÁMETROS OPCIONALES
def miFuncionParam(nombre="Juan"):  # Se le indica un parametro por defecto
    print("Hola", nombre)

miFuncionParam()
miFuncionParam("Victor")    # Si se invoca y contiene un parámetro, entonces el parametro por defecto se ignora

#   *args   #Crea una tupla de valores de los parámetros
def suma(*args):
    resultado = 0

    for arg in args:
        resultado += arg

    print(resultado)

suma(9, 9)

#   **kwargs    => Crea un diccionario con los valores de los parámetros
def suma(**kwargs):
    print(kwargs)

suma(vivienda="piso", coche="rojo")


# RETURN    => Devuelve un valor de la función
def suma(a, b):
    return a + b

resultado = suma( 2, 4 )
print(resultado)


#   DEVOLVIENDO MAS DE UN VALOR
def operaciones( a, b ):
    return a+b, a-b, a*b, a/b

resultado = operaciones(2, 4)   # Devuelve multiples valores almacenados en una tupla
print(resultado)

#   DEVOLVIENDO MULTIPLES VALORES ALMACENDOS EN CADA UNO EN UNA VARIABLE
def operaciones( a, b ):
    return a+b, a-b, a*b, a/b

sum, resta, multi, divi = operaciones(2, 4)   # Devuelve multiples valores almacenados cada uno en una variable
print(sum)
print(resta)
print(multi)
print(divi)


#   FUNCIÓN ANONIMA
anonima = lambda nombre, nombre2: print("hola", nombre, "adios", nombre2)
anonima("pepe", "juan")

