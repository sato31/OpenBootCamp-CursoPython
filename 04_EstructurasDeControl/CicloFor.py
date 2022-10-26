
#   FOR PARA RECORRER LISTAS
lista = [1, 2, 3, 'a', 5]

for valorActual in lista:
    print(valorActual)

#   FOR PARA BUSCAR UN ELEMENTO EN UNA LISTA
lista = ["hola", "mensaje", "adios"]

for palabra in lista:
    print("Palabra actual:", palabra)

    if palabra == "mensaje":
        print("He encontrado la palabra mensaje")
        break

#    IN
if "mensaje" in lista:
    print("He encontrado la palabra mensaje")

#   NOT IN
lista = ["hola", "adios"]
if "mensaje" not in lista:
    print("No hay palabra mensaje")

#   ORDENAR UNA LISTA
lista = [3, 4, 1, 2, 5]

listaOrdenada = sorted(lista)
print(listaOrdenada)

#   ORDENAR LISTA EN ORDEN INVERSO
listaOrdenada = sorted(lista, reverse=True)
print(listaOrdenada)

#   ORDENAR CARACTERES DE UNA LISTA
lista = ['A', 'a', 'p', 'P', 'z', 'Z']
listaOrdenada = sorted(lista, reverse=False)
print(listaOrdenada)

#   FOR CON ELSE
lista = ["hola", "mensaje", "adios"]

for palabra in lista:
    if palabra == "mensaje":
        print("Encuentro la palabra mensaje")
        break
else: 
    print("No se encuentra nada")
