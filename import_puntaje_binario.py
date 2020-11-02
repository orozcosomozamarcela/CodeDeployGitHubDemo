import puntajes_binario

datos = [("Eliana ", "103", "12:08:34"),("Julieta", "110","15:20:15"),("Ana", "200","20:15:30")]

puntajes_binario.guardar_puntajes("datos_flappyBird", datos)
datos_recuperados = puntajes_binario.recuperar_puntajes("datos_flappyBird")

print(datos_recuperados)
