
#   WHILE SIMPLE
contador = 1

while contador <= 10:
    print("contador vale", contador)
    contador += 1

#   WHILE CON CONDICIONANTE
contador = 1

while contador <=10 :
    if contador % 2 == 0:
        print(contador, "es un número par")
    contador +=1

#   WHILE CON BREAK: DETIENE EL BUCLE
contador = 1

while contador <= 10:
    print("contador vale", contador)

    if contador == 5:
        print("Rompo el bucle")
        break

    contador += 1

#   WHILE CON CONTINUE: FORZAR LA SIGUIENTE ITERACIÓN
contador = 0
while contador <= 10:
    contador += 1

    if contador % 2 == 0:
        print(contador, "es un numero par")
        continue    # Se da la instrucción de que no se ejecute la siguiente linea y realiza la siguiente iteración

    print("Estoy aqui, porque contador vale,", contador, "y no se ha disparado el continue")

print("Fuera del While")