#SOLUCION EJERCICIO 8
import csv

def show_main_menu():
    print('1. Guardar datos alumnos')
    print('2. Leer Datos alumnos CSV')
    print('0. Salir')

def show_secondary_menu():
    print('1. Continuar Cargando Datos en CSV')
    print('0. Salir')

def consulta_materias():
    alumnos = 'alumnos_materias.csv'
    materias = 'deuda_materias.csv'
    while True:
        while True:
            try:
                show_main_menu()
                option = int(input('Ingresar una opción:'))
                if 0 <= option <= 2:
                    break
                else:
                    print('Ingresar un valor mayor o igual cero.')
            except ValueError:
                print('Error: Ingresar un valor entero')
        if option == 0:
            break
        elif option == 1:
            cargar_datos(alumnos)
        elif option == 2:
            imprimir_materias_alumnos(alumnos, materias)

def cargar_datos(alumnos):
    datos = True
    while datos:
        lista_alumnos = []
        alumno = []
        fields = ['DNI', 'Apellido', 'Nombre', 'Año', 'Comision']

        for campo in fields:

            alumno.append(input(f"Ingrese {campo} del alumno: "))

        lista_alumnos.append(alumno)
        answer = input("Cargar más alumnos? Si/No: ")
        try:
            with open(alumnos, 'a', newline='') as file:
                file_guarda = csv.writer(file)
                file_guarda.writerows(lista_alumnos)
                return
        except IOError:
            print("Ocurrio un error con el archivo")

        while True:
            if answer == 'SI' or answer == 'si' or answer == 's':
                datos = True
                break
            elif answer == 'NO' or answer == 'no' or answer == 'n':
                datos = False
                break
            else:
                answer = input('Opción incorrecta. Ingrese "SI" para volver a intentar o "NO" para salir": ')


def imprimir_materias_alumnos(alumnos, materias):
    """ Abre los archivos de alumnos y materias, y por cada alumno imprime
        todas las materias que le corresponden. """
    try:
        materias_a = open(materias)
        alumnos_a = open(alumnos)
        materias_csv = csv.reader(materias_a)
        alumnos_csv = csv.reader(alumnos_a)

        # Empieza a leer
        alumno = next(alumnos_csv, None)
        materia = next(materias_csv, None)
        while (alumno):
            print("{}, {}".format(alumno[1], alumno[2]))
            if (not materia or materia[0] != alumno[0]):
                print("\tNo se registran materias")
            while (materia and materia[0] == alumno[0]):
                print("\t{}: {}".format(materia[1], materia[2]))
                materia = next(materias_csv, None)
            alumno = next(alumnos_csv, None)

        # Cierro los archivos
        materias_a.close()
        alumnos_a.close()
    except IOError:
        print("no hay datos cargados, por favor ingresa datos")

consulta_materias()
