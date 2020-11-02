import csv


def prestamos_dnis__prestamo(archivo_prestamos):
    """ Recorre un archivo csv, con la información almacenada en el
    formato: dni,año,_prestamo,venta """

    # Inicialización

    prestamos = open(archivo_prestamos)
    prestamos_csv = csv.reader(prestamos)

    # Saltea los encabezados
    next(prestamos_csv)

    item = next(prestamos_csv, None)
    total = 0

    while item:
        # Inicialización para el bucle de dni
        dni = item[0]
        total_dni = 0
        print("dni {}".format(dni))
        prestacion = item[1]
        total_prestacion = 0

        while item and item[0] == dni and item[1] == prestacion:
            _prestamo, saldo = item[1], float(item[2])
            print("\t\tTotal del prestamo {}: {:.2f}".format(_prestamo, saldo))
            total_prestacion += saldo
            # Siguiente registro
            item = next(prestamos_csv, None)

        # Final del bucle de dni
        print("Total para el dni {}: {:.2f}\n".format(dni, total_dni))
        total += total_dni

    # Final del bucle principal
    print("Total general: {:.2f}".format(total))

    # Cierre del archivo
    prestamos.close()


prestamos_dnis__prestamo("prestaciones.csv")
