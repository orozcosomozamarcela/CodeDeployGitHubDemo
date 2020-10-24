def guardar_puntajes(nombre_archivo, puntajess):

    with open(nombre_archivo, "w", newline= "") as f:

         for nombre, puntaje, tiempo in puntajess:
             print("estoy guardando")
             f.write(" {} , {},{}\n".format(nombre,puntaje, tiempo))

def recuperar_puntajes(nombre_archivo):

    puntajess = []
    with open(nombre_archivo, "r") as f:
        for linea in f:
            print("estoy leyendo", linea)

            nombre, puntaje, tiempo = linea.rstrip("\n").split(",")
            puntajess.append((nombre, int(puntaje),tiempo))



return puntajess
