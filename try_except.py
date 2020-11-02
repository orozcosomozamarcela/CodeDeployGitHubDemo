"""
archivo = None
try:
    archivo = open("miarchivo.txt") # aca va a tirar la exception de entrada y salida y porque no tengo en mi carpeta de Par un archivo llamado "miarchivo.txt"
    #procesar el archivo

except IOError:
    print("Error de entrada/salida.")
    #realizar prcesamiento adicional
except:
    print("generico")
# realizar procesamiento adicional
finally:
    #en el archivo abierto debemos cerrarlo
    print("llega al finally")
    if archivo and not archivo.closed:
        archivo.close()
"""
# procesar la excepción

#EN ESTE EJEMPLO ME AHORRO TENER QUE ESCRIBIR FINALLY, Y ME AHORRO LA ASIGNACION EXTRA. Y PUEDE ABRIR EL ARCHIVO DE MANERA CORRECTA.

try:
    with open("miarchivo.txt") as f:
        pass # es una palabra reservada para decir que mas adelante va a ver un codigo y asi no me produzca un error
        # procesar el archivo
except IOError:
    print("Error de entrada/salida.")
# realizar procesamiento adicional
except:
    print("generico")
# procesar la excepción
