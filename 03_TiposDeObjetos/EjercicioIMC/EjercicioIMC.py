# Escribe un programa en la consola de python que pida al usuario su peso (en kg) y estatura (en metros),
# calcule el índice de masa corporal y lo almacene en una variable, e imprima por pantalla la frase 
# Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales.

pesoKg = input("Ingresa tu peso en Kg: ")
estaturaM = input("Ingresa tu estatura en metros: ") 
imc = ( float(pesoKg) / (float(estaturaM) ** 2))
imc = round(imc, 2)
print('Tu indice de masa corporal es: ', imc )