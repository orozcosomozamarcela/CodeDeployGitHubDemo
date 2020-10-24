
""" aca primero que nada tenemos que importar csv"""

import csv
def guardar_puntajes(nombre_archivo, puntajess):

    with open(nombre_archivo, "w", newline= "") as archivo_texto:# aca la profe modifico el nombre de f por archivo_texto para tener otro nombre mas claro.

         archivo_csv = csv.writer(archivo_texto)    # comparado con el otro archivo de texto de puntajes aca se modifica. CSV es un objeto aca,se convierte en objeto
         archivo_csv.writerows(puntajess) # comparado con el otro archivo de texto de puntajes aca se modifica. Con writerows se ppuede escribir muchas lineas, aca no tenemos que hacer ningun ciclo sino que se guardaria por liena directamente
         print(archivo_csv)

def recuperar_puntajes(nombre_archivo):

    puntajess = []
    with open(nombre_archivo, "r") as f: # recordar que al utilizar este formato with open....... se abre y se cierra el archivo. no hay necesidad de estar guardandolo a parte
         archivo_csv = csv.reader(f)    # comparado con el otro archivo de texto de puntajes aca se modifica
         for nombre, puntaje, tiempo in archivo_csv:
             puntajess.append((nombre, int(puntaje),tiempo))
    print("estoy leyendo", linea)


""" en este ejemplo y en el otro ejemplo se esta guardando en byte y en texto ya que estamos agregando texto en los nombres que esribimos y numeros de puntajes."""

return puntajess
