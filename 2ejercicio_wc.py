
"""Escribir un programa, llamado wc.py que reciba un archivo, lo procese e imprima por pantalla cuántas líneas, cuantas palabras y cuántos caracteres contiene el archivo."""


def wc(archivo): # hay que contar primero lineas, luego caracter y luego palabra porque sino no va a contar los caracteres de espacio.
    cant_lineas = 0
    cant_caracteres = 0
    cant_palabras = 0

    try:
        with open(archivo, "r", newline= "") as f:
            for linea in f:
                cant_lineas += 1
                linea = linea.rstrip("\n")# para sacarle el caracter del salto de linea y no me lo este contando
                cant_caracteres += len(linea)
                cant_palabras += len(linea.split())#separa la linea en la cant de n de elementos que se generen a partir de dividir ese string en los caracteres espacio que hayan


    except IOError:
        print("Hubo un error al abrir el archivo")

    print(f"cantidad de lineas:{cant_lineas}\ncantidad de palabras:{cant_palabras}\ncantidad de caracteres: {cant_caracteres}")

wc("ejercicio2_wc.txt")
