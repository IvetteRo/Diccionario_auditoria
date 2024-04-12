import time

arreglo = ["A", "B", "C", "D", "E", "F", "G", "I", "J", "K", "L", "M", "Ñ", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
contador = 0
palabra = ""
posicion = -1
arreglo1 = []

# Inicia el contador de tiempo
start_time = time.time()

for element in arreglo:
    for element1 in arreglo:
        for element2 in arreglo:
            for element3 in arreglo:
                palabra_actual = element + element1 + element2 + element3
                arreglo1.append(palabra_actual)  # Agrega la palabra actual a la lista
                if palabra_actual == "JAVA":
                    posicion = contador
                contador += 1

# Finaliza el contador de tiempo
end_time = time.time()

# Calcula el tiempo transcurrido
elapsed_time = end_time - start_time

print(arreglo1)
print("Última palabra generada:", palabra_actual)
print("Posición de 'JAVA':", posicion)
print("Tiempo transcurrido:", elapsed_time, "segundos")