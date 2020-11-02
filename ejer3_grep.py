"""Escribir un programa, llamado grep.py que reciba una expresión y un archivo e imprima las líneas del archivo que contienen la expresión recibida."""

def grep(archivo,expresion):
    try:
        with open (archivo, "r", newline = "") as f:

           for linea in f:
               linea = linea.rstrip("\n")
               if expresion in linea:
                 print(linea)

    except IOError:
        print("Hubo un error al abrir el archivo")

grep("ejercicio1_cut.txt", "error")
