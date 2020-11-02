"""Escribir un programa, llamado cut.py, que dado un archivo de texto(puede ser: .txt,.md,.load,etc), un delimitador, y una lista de campos, imprima solamente esos campos, separados por ese delimitador."""
# Como es un archivo de texto lo podemos resolver con el metodo readline comun o lo podemos hacer con ayuda del modulo csv pero lo mas simple seria resolverlo sin el modulo de csv.
# en este ejercicio vamos a tener de ejemplo saber los IPS

"""def cut(archivo,campos,delimitador):

    try:
        with open(archivo, "r",newline= "") as f: # la f es el nombre de la variable que va a contener el archivo abierto.
            linea = f.readline() # esto siempre nos va a devolver un string
            campos_seleccionados = []   # aca primero tenemos que generar esta lista
            while linea: # mientras linea no sea una linea vacia va a iterar una y otra vez
                lista_temp = linea.split(delimitador)# split sino le pasamos ningun parametro por defecto corta al string en todos los espacios(palbras) que encuentra, pero en este caso tenemos que pasar el delimitador
                for campo in campos: # campos son los campos que le pasamos por parametro mas abajo
                    try: #esta validacion la agregamos aca(*)
                        campos_seleccionados.append(lista_temp[campo])# hasta si lo probamos el ciclo esta iterando continuamente sobre la misma linea, tenemos que pasarle entonces tiene que pasar a la siguiente linea como se ve abajo se pasa de linea
                         # aca se pone esto fuera del for pero dentro del while para que lea la proxima linea para que no siga iterando
                    except IndexError:
                        print(f"El campo {campo} no existe")
                linea = f.readline()

                    # aca se puede hacer con un if desde try hasta print(f"el campo....no existe), quedaria asi:
                    #if campo < len(lista_temp):
                    #    campos_seleccionados.append(lista_temp[campo])
                    #else:
                    #    print(f"El campo {campo} no existe")
                #linea = f.readline()


        for item in campos_seleccionados:
            print(item)

    except IOError:
           print("Hubo un problema con el archivo")


cut("ejercicio1_cut.txt", [0, 1], "-") """# aca le modifique el delimitador

# sino usaramos el modulo csv como podriamos usar para dividir un string y nos devuelva una lista, es con Split vamos a obtener una lista con n cantidad de elementos que se obtuvieron al eliminar el delimitador que le pasamos, hacemos esto para obtner los campos 0 , 1 , 2 en este ejemplo

# si cambiamos el simbolo del delimitador entonces los campos pueden ser mas o menos dependiendo del delimitador, en el caso de un delimitador de Espacio nos dara mas campos y si ponemos en el parametro [5] entonces si va a existir ese campo pero en el guion medio (-) no y si ponemos 5 como parametro y (espacio) vamos a tener un error de indice, entonces tenemos dos opciones con la Validacion o la exceptcion(try,except que siemmpre tienen que ir juntos , except IndexError)(*)

# hacemos el mismo ejercicio utilizando CVS

import csv

def cut(archivo,campos,delimitador):

    try:
        with open(archivo, "r",newline= "") as f:
            lectura = csv.reader(f, delimiter = delimitador)

            linea = next(lectura, None)

            campos_seleccionados = []

            while linea:#aca no tengo lista temporal directamente la lista
                for campo in campos:
                    #try:                                                           campos_seleccionados.append(linea[campo])                                            except IndexError:                                                                                 print(f"El campo {campo} no existe")                                                               linea = next(lectura, None)

                    if campo < len(linea):
                       campos_seleccionados.append(linea[campo])
                    else:
                       print(f"El campo {campo} no existe")
                linea = next(lectura, None)

        for item in campos_seleccionados:
            print(item)

    except IOError:
        print("Hubo un problema con el archivo")


cut("ejercicio1_cut.txt", [0,5], "-")
