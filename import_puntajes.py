import puntajess


datos = [("Eliana", "103", "12:08:34"), ("Julieta","110", "11:23:12"),("Ana", "182", "23:11:11")]
#va leyendo cada tupla(Eliana,.....)
#luego la otra tupla(Julieta,.....)
puntajess.guardar_puntajes("datos_flappyBird", datos)

datos_recuperados = puntajess.recuperar_puntajes("datos_flappyBird")

print(datos_recuperados)  # este print no es necessario solo es para que siempre muestren los cambios

datos = [("Oscar", "103", "12:08:34"), ("Carlos","110", "11:23:12"),("Miguel", "182", "23:11:11")]  #(*) aca cambiamos los datos que queremos que agregue pero antes tenemos que eliminar el archivo "datos_flappyBird" que tenemos en la ruta documentos, entonces posterior se agregaran los nuevos datos que estoy pasando.

puntajess.guardar_puntajes("datos_flappyBird", datos)

datos_recuperados = puntajess.recuperar_puntajes("datos_flappyBird") # y aca se tiene que volver a llamar el archivo puntaje.

print(datos_recuperados)  # este print no es necessario solo es para que siempre muestren los cambios


# Aca para enviar a Consola y probar si funcionó tenemos que poner la direccion de ruta de este archivo.
