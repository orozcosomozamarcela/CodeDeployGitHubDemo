


import puntajess_csv

datos = [("Eliana", "103", "12:08:34"), ("Julieta","110", "11:23:12"),("Ana", "182", "23:11:11")]

puntajess_csv.guardar_puntajes("datos_flappyBird.csv", datos) # aca le agregamos .csv para que nos guarde en el formato con columnas y filas que es el que corresponde al csv en orden como base de datos.

datos_recuperados = puntajess_csv.recuperar_puntajes("datos_flappyBird.csv")

print(datos_recuperados)  # este print no es necessario solo es para que siempre muestren los cambios

"""datos = [("Oscar", "103", "12:08:34"), ("Carlos","110", "11:23:12"),("Miguel", "182", "23:11:11")]

puntajess_csv.guardar_puntajes("datos_flappyBird", datos)

datos_recuperados = puntajess_csv.recuperar_puntajes("datos_flappyBird") """ # aca si queremos podemos agregar todo esto pero recordar de corregir el archivo principal con la opcion "a" en vez de "w"
