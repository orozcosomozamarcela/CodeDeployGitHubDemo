
""" aca primero que nada tenemos que importar csv"""

import csv
def guardar_puntajes(nombre_archivo, puntajess):

    with open(nombre_archivo, "w", newline= "") as archivo_texto:# aca la profe modifico el nombre de f por archivo_texto para tener otro nombre mas claro.

         archivo_csv = csv.writer(archivo_texto)    # comparado con el otro archivo de texto de puntajes aca se modifica. CSV es un objeto aca,se convierte en objeto. Cada vez que trabajamos con el objeto csv.writer y luego trabajmos con el objeto que nos devuelve archivo_csv lo devuelve como una lista.
         archivo_csv.writerows(puntajess) # comparado con el otro archivo de texto de puntajes aca se modifica. Con writerows se ppuede escribir muchas lineas, aca no tenemos que hacer ningun ciclo sino que se guardaria por liena directamente
         print(archivo_csv)

         # si yo quisiera trabajar archivo_csv como diccionario lo puedo hacer con el DictReader

def recuperar_puntajes(nombre_archivo):
    """Recupera los puntajes a partir del archivo provisto.
    Devuelve una lista con los valores de los puntajes.
    Pre: el archivo contiene los puntajes en el formato esperado,
    separados por comas.
    Post: la lista devuelta contiene los puntajes en el formato:
    [(nombre1,puntaje1,tiempo1),(nombre2,puntaje2,tiempo2)] ."""

    puntajess = []
    with open(nombre_archivo, "r", newline="") as f:
        archivo_csv= csv.reader(f)
        for nombre, puntaje, tiempo in archivo_csv:

            puntajess.append((nombre, int(puntaje),tiempo))

        return puntajess
