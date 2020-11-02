"""Ejercicio 11.10.1. Escribir un programa, llamado head que reciba un archivo y un número N e
imprima las primeras N líneas del archivo."""

#EL EJERCICIO ESTE ESTA LEYENDO TODO EL CONTENIDO
def head (archivo, numero):

    with open(archivo, "r") as file:
        # cuando se abre el archivo sin poner "r" no hay problema porque el archivo automaticamente lo abre como texto pero es mejor ponerlo para guiarnos.
       lectura = file.readlines()   # con el metodo readlines se leen todas las lineas
       for linea in range(len(lectura)): # aca con el for que es la condicion va a leer toda la longitud con el modulo len
           if linea <= numero:  # aca ponemos la condicion para que nos imprima solo las primeras 3 lineas que le estamos pasando por parammetro
              print(lectura[linea])



#head("ejercicio1y2.txt", 3) # aca estamos llamando a la funcion y dentro poniendo el archivo que quiero que lea y luego el 3 indica que tiene que leer 3 lineas

"""recordar que cuando decimos que lea 3 lineas como en este ejemplo, estamos diciendo que lea inclusive la linea en blanco
hasta que llegue a la tercera linea dejar de leer."""


# OTRO EJEMPLO LEYENDO LINEA POR LINEA que seria mas lo que pide el enunciado. mas preciso digamos, aunque de las dos maneras estaria igual solo que con el primer ejemplo se gasta mas espacio de memoria.

def head (archivo, numero):
    contador= 0
    with open(archivo, "r") as file:

        while contador <= numero: # aca estamos utilizando el Whle en vez del For
            print(file.readline()) # aca lee linea por linea y no todo como en readlines
            contador += 1

head("ejercicio1y2.txt", 3)

"""Ejercicio 11.10.2. Escribir un programa, llamado cp.py, que copie todo el contenido de un ar-
chivo (sea de texto o binario) a otro, de modo que quede exactamente igual.

Nota: utilizar archivo.read(bytes) para leer como máximo una cantidad de bytes."""


def cp(archivo):    # este desarrollo es mas corto
    with open (archivo, "r") as file:
         lectura = file.readlines()

    with open ("copiaejercicio1y2.txt", "w") as file2:
         file2.writelines(lectura) # aca con el modulo WriteLines vamos a poder escribir varias lineas y lo que esta en parentesis "lectura" es lo que queremos escribir, en este caso le escribimos y enviamos todo el archivo lectura

cp("ejercicio1y2.txt")

 # en este ejemplo se va a copiar el archivo que se quiere copiar y se va a tener en documentos dos archivos, el original y el que se copia


#OTRO EJEMPLO DEL EJERCICIO ANTERIOR PARA QUE LEA POR LINEA, es mas largo este ejemplo

def cp(archivo):
    with open (archivo, "r") as file:
        with open ("copiaejercicio1y2.txt", "w") as file2:
            linea = file.readline()
            while linea != "":
               file2.write(linea)
               linea = file.readline()

cp("ejercicio1y2.txt")
