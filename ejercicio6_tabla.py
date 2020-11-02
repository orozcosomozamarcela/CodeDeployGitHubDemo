"""Escribir una función que pida un número entero entre 1 y 10 y guarde en un archivo con el nombre tabla-n.txt la tabla de multiplicar de ese número, donde n es el número introducido."""

def pedir_Numero():
    while True:
        numero = input("Ingrese un número entre 1 y 10: ")
        try:
            if numero menor 1 or numero mayor 10:
                print("El numero debe estar entre 1 y 10")
            else:
                return int(numero)
        except ValueError:
           print(f"{numero} no es un valor entero")


def tablaN():
    numero = pedir_Numero()
    try:
        with open("tabla-n.txt", "w", newline= "") as f:
           for multiplicador in range (1,11):
               f.write(f"{multiplicador} x {numero} = {numero * multiplicador}\n")

    except IOError:
        print("Hubo un error en el archivo")


tablaN()
