archivo = open("alumnos.txt")

print(archivo)

linea = archivo.readline()
linea2 = archivo.readline() # para poder ver lo escrito dentro del archivo, con readline escribe una sola linea y sucsivamente.
# imprime todas las lineas.
#lineas = archivo.readlines() # aca solo cambiamos por readlines, el agregar el plural con la s va a bajar todo lo que esta dentro #del archivo, pero lo baja uno seguidos de otra palabra con el salto de linea incluido /n
#
# print(lineas)

## for linea in archivo:# se puede utulizar este for para no escribir linea = achivo.readline y da el mismo resultado
print(linea, linea2)
# print(lineas)
#archivo.close()  # se cierra  al final de terminar el archivo sino va a tirar error
#
# de la manera mas abajo usada es lo mas practico de abrir y cerrar un archivo al mismo tiempo.
with open("alumnos.txt", 'w') as archivo: # es una de las maneras mas conocidas de trabajar con un archivo abierto, este #primero que es como un ciclico, diga: mientras que el archivo de texto que querramos este abierto se trabaja y cuando sale del #bloque With se cierra automaticamente. Ver que agregamos un tercer parametro que es el a+ y anterior esta la r y w.
    #i = 1
    #for linea in archivo:
    #    linea = linea.rstrip("\n")  # se usa rstrip para remover el salto de linea(o caracter)y ademas le agregamos por cada linea #que estamos imprimiendo le agregamos el contador
        #print("{}: {}".format(i, linea))
        #print(f"{i}: {linea}") # es lo mismo escribirlo asi que lo que esta escrito arriba
        #i += 1

    archivo.write("hola\n") # modo de solo lectura, si ¡ponemos este codigo no me va a dejar escribir
    archivo.write("julieta\n") # se agrega la barra invertida y n para que nos escriba el salto de pagina

    archivo.writelines("paola, marcela") # aca podemos agregar mas de un nomre en la misma linea
