"""Escribir una función guardar_datos que reciba un diccionario y un nombre de archivo, y guarde el contenido del diccionario en el archivo, con el formato clave, valor ."""

def guardar_datos(datos,archivo):
    try:
        with open(archivo, "w", newline="") as f:
            for dato in datos:
                f.write(f"{dato}, {datos[dato]}\n")

    except IOError:
        print("Hubo un error al abrir el archivo")

#datoss = {"nombre": "paola", "apellido": "Orozco"}

#guardar_datos(datoss, "ejercicio4.txt") # aca se creo el archivo ejercicio4.txt


"""Escribir una función cargar_datos que reciba un nombre de archivo, cuyo contenido tiene el formato clave, valor y devuelva un diccionario con el primer campo como clave y el segundo como valor."""

def cargar_datos(archivo):
    try:
        with open(archivo, "r", newline="") as f:
            linea = f.readline()
            diccionario = {}

            while linea:
                linea = linea.rstrip("\n")
                campos = linea.split(",")# aca al partir los dos valores lo separa desde la coma
                diccionario[campos[0]] = campos[1]
                linea = f.readline()

            return diccionario
    except IOError:
        print("Hubo un error al abrir el archivo")
datoss = {"nombre": "paola", "apellido": "Orozco"}

print(cargar_datos("ejercicio4.txt"))
