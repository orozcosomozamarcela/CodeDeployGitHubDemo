"""Cree un programa que:
a-Contenga un menú de opciones a ejecutar con las siguientes acciones.
b-Permita el guardado de datos en un archivo csv llamado vendedores, cuyo formato será Apellido, Nombre, Fecha de ingreso, Antigüedad, Comisiones
c-Permita la lectura de datos de los vendedores con su información, mostrando en cada línea un vendedor de la siguiente manera:
{Nombre Apellido} trabaja en la empresa desde { Fecha de ingreso} y lleva comisionado {Comisiones}"""

#7 b
"""import os.path

def eje7_guardar(archivo, campos):
    guardar = "si"
    lista_vendedores = []
    while guardar == "si":
        vendedor = {}

        for campo in campos:
            vendedor[campo] = input(f"Ingrese {campo} del vendedor: ")
        lista_vendedores.append(vendedor)
        guardar = input("Desea seguir agregando vendedores? Si/No")

    try:
        archivo_existe = os.path.isfile(archivo)
        with open(archivo, 'a', newline='') as file:
            file_guarda = csv.DictWriter(file, fieldnames=campos)

            if not archivo_existe:
                file_guarda.writeheader()

            file_guarda.writerows(lista_vendedores)
            print("se guardo correctamente")
            return
    except IOError:
        print("Ocurrio un error con el archivo")

#7 c
def eje7_cargar(archivo):
    try:
        with open(archivo,'r', newline='') as file:
             lectura_csv = csv.DictReader(file)
            campos = lectura_csv.fieldnames

            for linea in lectura_csv:
                print(f"{linea[campos[1]]} {linea[campos[0]]} trabaja en la empresa desde {linea[campos[2]]} y lleva comisionado {linea[campos[4]]}")
            return
    except IOError:
        print("Ocurrio un error con el archivo")

# 7 a
def ejercicio7():
    ARCHIVO = "vendedores.csv"
    CAMPOS = ['Apellido', 'Nombre', 'Fecha de ingreso', 'Antigüedad', 'Comisiones']

    while True:
        print("Elija una opcion: \n 1.Guardar datos \n 2.Cargar datos \n 3.Salir")
        opcion = input("")

        if opcion == "3":
            exit()
        if opcion == "1":
            eje7_guardar(ARCHIVO, CAMPOS)
        if opcion == "2":
            eje7_cargar(ARCHIVO)
        else:
            print("Por favor elija una opcion valida")

ejercicio7()


#7 b listas
def eje7_guardar_listas(archivo, campos):
    guardar = "si"
    lista_vendedores = []
    while guardar == "si":
        vendedor = []

        for campo in campos:
            vendedor.append(input(f"Ingrese {campo} del vendedor: "))
        lista_vendedores.append(vendedor)
        guardar = input("Desea seguir agregando vendedores? Si/No")

    try:
        with open(archivo, 'w', newline='') as file:
            file_guarda = csv.writer(file)
            file_guarda.writerows(lista_vendedores)
            print("se guardo correctamente")
            return
    except IOError:
        print("Ocurrio un error con el archivo")

#7 c listas
def eje7_cargar_listas(archivo):
    try:
        with open(archivo,'r', newline='') as file:
            lectura_csv = csv.reader(file)

            for linea in lectura_csv:
                print(f"{linea[1]} {linea[0]} trabaja en la empresa desde {linea[2]} y lleva comisionado {linea[4]}")
            return
    except IOError:
        print("Ocurrio un error con el archivo")

# 7 a listas
def ejercicio7_listas():
    ARCHIVO = "vendedores_listas.csv"
    CAMPOS = ['Apellido', 'Nombre', 'Fecha de ingreso', 'Antigüedad', 'Comisiones']

    while True:
        print("Elija una opcion: \n 1.Guardar datos \n 2.Cargar datos \n 3.Salir")
        opcion = input("")

        if opcion == "3":
            exit()
        if opcion == "1":
            eje7_guardar_listas(ARCHIVO, CAMPOS)
        if opcion == "2":
            eje7_cargar_listas(ARCHIVO)
        else:
            print("Por favor elija una opcion valida")

ejercicio7_listas()
"""
