import pickle     # primero hay que importar le modulo pickle

def guardar_puntajes(nombre_archivo,puntajes):

    with open (nombre_archivo, "wb") as f: # aca tenemos que agregar la b porque es binario, los archivos binarios no son leibles para los humanos. hay que pasarlo a un formato que si se pueda, los archivos binarios no trabajan con salto de linea como los archivos de texto sino que trabaja con BYTES y ademas ahora estamos utilizando PICKLE para que sea mas rapido el uso del archivo binario y nos ayude.
        pickle.dump(puntajes, f) # el modulo pickle nos sirve para almacenar informacion no solo para utilizarla en el futuro sino tambien para guardar los datos que estan siendo utilizados en el momento. lo que esta en parentesis es puntajes que son lo datos que queremos guardar y la f es en el archivo que queremos hacer

def recuperar_puntajes(nombre_archivo):

    with open(nombre_archivo,"rb") as f:
        return pickle.load(f) # comparado con los archivos de texto y csv no se tienen que hacer ningun ciclo

"""en este ejemplo se esta guardandno y recuperando y se obtiene lo mismo que vemos en los archivos de texto, cuando vamos a abrir el archivo en la carpeta de nombre flappybird no se va a entender bien ya que aparece con codigos pero si aplicamos en la consola si se va a leer por el modulo pickle"""
