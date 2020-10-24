
def guardar_puntajes(nombre_archivo, puntajess):
    """Guarda la lista de puntajes en el archivo.
    Pre:nombre_archivo corresponde a un archivo válido,
    puntajes corrresponde a una lista de tuplas de 3 elementos.
    Post: se guardaran los valores en el archivo,
    separados por comas."""

    with open(nombre_archivo, "w", newline= "") as f: # aca la profe modifica la opcion "w" por la opción "a",ya que en "w" cada vez que corramos el archivo puntajes se pueda TRUNCAR, entonces en ese caso usamos la opcion "a" cuando ponemos la opcion"a" se coloca en la ultima posicion donde estaba solamente, de ahi en mas es parecido a la opcion"w". Y luego cambia en el otro archivo que se llama import_puntajes.py, cambia los datos que se pasaron. Entonces en el archivo de import_puntajes modificamos los datos (*)contunua la explicacion en el otro archivo de impo...
         for nombre, puntaje, tiempo in puntajess:
             print("estoy guardando")
             f.write(" {} , {},{}\n".format(nombre,puntaje, tiempo))

def recuperar_puntajes(nombre_archivo):
    """Recupera los puntajes a partir del archivo provisto.
    Devuelve una lista con los valores de los puntajes.
    Pre: el archivo contiene los puntajes en el formato esperado,
    separados por comas.
    Post: la lista devuelta contiene los puntajes en el formato:
    [(nombre1,puntaje1,tiempo1),(nombre2,puntaje2,tiempo2)] ."""

    puntajess = []
    with open(nombre_archivo, "r") as f:
        for linea in f:
            print("estoy leyendo", linea) # ACA VA A GUARDAR LINEA POR LINEA, CON SALTO DE LINEA, O TUPLA COMO QUIERA LLAMARSE A LA LINEA
            nombre, puntaje, tiempo = linea.rstrip("\n").split(",")
            puntajess.append((nombre, int(puntaje),tiempo))



return puntajess
