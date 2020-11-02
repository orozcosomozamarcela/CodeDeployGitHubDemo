import csv

#EN ESTE EJEMPLO DE CSV SE UTILIZA CUANDO TENEMOS TEXTOS CON COMAS (,)

def leer_cumples(archivo):# ACA SOLO LEEMOS LOS CUMPLES Y EN LA OTRA FUNCION SE GUARDAN LOS CUMPLES
    "Abre un archivo de texto o separado por comas e imprime sus columnas, y datos del cumpleañero"
    with open(archivo) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=";") # ACA SE TIENE QUE UTILIZAR delimiter Y EN () LO QUE SE QUIERA RECONOCER. EL CSV SE UTILIZA CON EL READER, ESTE CSV.READER NOS VA A DEVOLVER UN OBJETO DE TIPO CSV

        line = next(csv_reader, None) # EL NONE ES EL PARAMETRO QUE UTILIZA PARA CUANDO LLEGUE AL FINAL DE LA LINEA QUE ESTE LEYENDO Y YA NO HAYA MAS VALORES ENTONCES SI LLEGA AL FINAL Y NO HAY MAS VALORES NECESITA DEVOLVER ALGO, QUE VA A DEVOLVER LO QUE LE PASEMOS COMO SEGUNDO PARAMETRO QUE EN ESTE CASO ES NONE.
        #CON EL METODO next SE PUEDE MOVER EL PUNTERO HASTA SU SIGUIENTE VALOR, EL NEXT SIRVE PARA QUE EL PUNTERO SE MUEVA A LA SIGUIENTE LINEA Y ASI NO IMPRIMA EL TITULO JUNTO CON LA INFORMACION DE TEXTO SINO QUE LO IMPRIME COMO LINEA DE TITULO. EL NEXT SE UTILIZA EN LOS ARCHIVOS DE TEXTOS
        print(f'Los nombres de las columnas son {", ".join(line)}')#EL METODO JOIN SE UTILIZA PARA SEPARAR LOS VALORES DE UNA LISTA Y TRANSFORMARLOS EN STRINGS, AGARRO CADA UNO DE LS VALORES Y SEPARO EN ESTE CASO POR COMAS. ACA ESTAMOS IMPRIMIENDO EL TITULO.

        for row in csv_reader:
            print(f'\t{row[0]} trabaja en el area de {row[1]} y nació en {row[2]}.')
leer_cumples("cumpleaños.txt")



def guardar_cumples(cumples):
    "Guarda en un archivo CSV los cumples indicados"
    with open('empleados_delimiter.csv', mode='w') as employee_file:# EL ARCHIVO empleados_delimiter.csv ES UN ARCHIVO NUEVO QUE SE VA A CREAR Y DONDE VAMOS A GUARDAR LOS CUMPLES. ESTA EN OMDO ESCRITURA PORQUE VAMOS A ESCRIBIR
        employee_writer = csv.writer(employee_file, delimiter=";") # EN EL DELIMITER SINO SE PONE NADA VA A UTILIZAR POR DEFECTO LA COMA.
        # realmente no hace falta iterar aca pero queria usar writerow
        for employee in cumples: # POR CADA SUBLISTA [] DENTRO DE LA GRAN LISTA`[],[], LA GRAN LISTA ES TODO COMPLETO
            employee_writer.writerow(employee)


guardar_cumples("cumpleaños.txt")
guardar_cumples([['nombre', 'area', 'cumpleaños'],['Juan Carlos', 'Contabilidad', 'Noviembre, 5 de'], ['Roberto Carlos', 'Deportes', 'Enero, 7 de']])# aca se le agrego el titulo y hay que escribirlo aca para que aparezca
