    # TUPLAS #
tupla = (1, 2, 3)
print(tupla)
# Las tuplas son inmutables
    # LISTAS #
lista = ['a', 'b', 'c']
print(lista)
# Las listas sin son mutables   

lista.append('x')   # Método para gregar un elemento a una lista
lista.append('y')
lista.append('z')
print(lista)

lista.remove('z')   # Método para eliminar el elemento de la lista
print(lista)

undostres = [1, 2, 3]
cuatrocincoseis = [4, 5, 6]
undostres.append(cuatrocincoseis)   # Crea una lista anidada
print(undostres)

vacio = []  # Lista vacia
print(vacio)

    # DICCIONARIOS #
diccionario = {
    "clave": "valor",
    "clave2": 15
}
print (diccionario)
print(diccionario['clave2'])    # Imprime valor de la clave especificada 

resultado = diccionario['clave2']
print(resultado)    # 15

diccionario['clave2'] = 99
print(diccionario['clave2'])    ## 99 
print(diccionario)

diccionario = { 'clave1': 1, 'clave2': 2, 'clave3': 3, 'clave4': 4 }
print(diccionario)

diccionario.pop('clave1')  #Elimina la clave especificada del dicionario
print(diccionario)

elementoViejo = diccionario.pop('clave4') # Guarda el elemento eleiminado en una variable
print(elementoViejo)

    # CONJUNTOS #
conjunto = {1, 2, 3, 1, 2, 3}
print(conjunto) # El conjunto no puede tener valores duplicados, por lo que solo imprimirá los elementos una vez

a = { 0, 2, 4, 6, 8}
b = { 1, 2, 3, 4, 5} 
a | b   # | => UNIÓN:  Une los dos conjuntos especificados
a & b   # & => INTERSECCIÓN: Muestra los valores que comparten los dos conjuntos
a - b   # - => DIFERENCIA: Muestra los valores que solo estan en 'a' y no en 'b'
a ^ b   # ^ => DIFERENCIA SIMETRICA: Muestra los valores únicos entre los 2 

    # ALGUNOS MÉTODOS #
miTexto = "hola, esto es un TextO"
print(miTexto.capitalize()) # Capitaliza la primera letra y las demas las hace minúsculas.
print(miTexto.title())      # Cada inicial de cada palabra la convierte a mayuscula.
print(miTexto.lower())      # Covierte todo el texto a minúsculas.
print(miTexto.upper())      # Convierte todo el texto a mayúsculas.
print(miTexto.replace('a', 'o'))    # Reemplaza las letras 'a' y las sustituye por 'o'
print(miTexto.replace('e', 'i'))    # Reeemplaza las letras 'e' por 'i'
print(miTexto.find("esto")) # Devuelve la posición del texto que recibio como parametro.
print(miTexto.split( ))     # Fragmenta la cadena de texto por cada espacio que encuentre y lo convierte en una lista
print(miTexto.split(','))   # Se le uede especificar el caracter donde se hará la fragmentación
print(miTexto.replace(',', ''))    #Reemplaza un caracter por otro, en este caso las comas por espacios.
print(miTexto.replace(',', '').lower().split()) # Combinación de metodos para convertir el texto a una lista.

listaTexto = ['hola', 'esto', 'es', 'un', 'texto']
print(' '.join(listaTexto)) # Une los elementos de una lista en una cadena agregando un caracter o string especificado entre ellos.

texto = '5'
type(texto)         # class 'str'
texto.isnumeric()   # True
texto = 'a'
texto.isnumeric()   #False

a = 5
b = 4
a - b   # 1
a * b   # 20
a % b   # 1
a // b  # Division
a ** b  # Potencia

a += 5
a -= 5
a += b
a -= b
a *= b
a /= b
a **= b








