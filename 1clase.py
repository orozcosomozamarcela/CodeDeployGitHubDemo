#Ejercicio 1
#
# Crear un programa que imprima por pantalla el mensaje “Hello World!”.
print ("Hola mundo")
# Nota: se puede imprimir el dato puro o el dato almacenado en una variable, siempre es una buena práctica usar variables.

# Ejercicio 2
#
# Crear un programa que imprima por pantalla todos los números pares del 0 al 100.
for n in range(0,102):
	if n%2==0:
		print(n)
# la primera opcion da una lista en vertical y la segunda solucion da una lista horizontal, ambas son viables.
        #print([i for i in range(0,102) if i%2==0])

# Ejercicio 3
#
# Crear un programa que imprima por pantalla todos los números del 0 al 100 que sean divisibles por 3.
# aca la profe explica como creaba una funcion con def
def ejercicio3():
    for numero in range(0, 101):
        if numero % 3 == 0:
             print(numero)
#ejercicio3()
#cuando se utiliza funciones siempre al terminar el ejercicio se tiene que volver a poner el nombre de la funcion.


# Ejercicio 4
# Crear un programa que pida al usuario que ingrese dos números y luego el programa imprima por pantalla: en un renglón la suma de ellos, en otro la resta y en otro el producto.
#num1 = int(input("Ingrese un numero: "))
#num2 = int(input("Ingrese otro numero: "))
#suma = num1 + num2
#print (" La suma de los numeros es: ", suma)
#resta = num1 - num2
#print (" La resta de los numeros es: ", resta)
#producto = num1 * num2
#print (" El producto de los dos numeros es: ", producto)


# Ejercicio 5
#Crear un programa que pida al usuario 10 números enteros, los almacene en una lista, ordene los números dentro de la lista y #luego imprima por pantalla la lista completa y ordenada.
def ejercicio5():
    valorList = []
    for numero in range (10):
        valorList.append(int(input("Ingrese un numero entero: ")))
        #se puede hacer de esa forma append (metodo)mas rapido o sino como esta abajo escrito que es mas largo.
        #valor = int(input("Ingrese un numero entero"))
        #valorList.append(valor)
    print (valorList)
    valorList.sort()
    print (valorList)


ejercicio5()
#Para ordenar una lista se utiliza un metodo en este caso Sort.
# Ejercicio 6
#
# Crear un programa que le pida al usuario dos números enteros y luego: si el primero es mayor que el segundo, retorne 1, si el primero es menor que el segundo retorne -1 y si ambos números son iguales retorne 0.

def ejercicio6(num1, num2):
    if num1 > num2:
        return 1
    elif num1 == num2:
        return 0
    else:
        return -1

input1 = int(input("Ingrese un numero entero "))
input2 = int(input("Ingrese otro numero entero "))
resultado = ejercicio6(input1,input2)
print (resultado)
# cuando se pasa input1 e input2 quire decir que va a tomar num1 y num2, es lo mismo que escribir una u otra, no hace falta que se llamen igual, es mejor que no se llamen igual.


# Ejercicio 7
#
# Crear un programa que le pida al usuario ingresar dos números enteros y devuelva el punto medio entre ellos.
#
# Ejercicio 8
#
# Crear un programa que tome una lista de números enteros y devuelva dos listas ordenadas. La primera con los números pares y la segunda con los números impares.
#

# Ejercicio 9
#
# Crear un programa que solicite al usuario que ingrese su dirección mail. Imprimir un mensaje indicando si la dirección es válida o no. Una dirección se considerará válida si contiene el símbolo "@".

# Ejercicio 10
#
# Crear un programa que dado un número de DNI, retorne True si el número es válido y False si no lo es. Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.

# Ejercicio 11
#
# Crear un programa que, dado un string, retorne la longitud de la última palabra. Se considera que las palabras están separadas por uno o más espacios. También podría haber espacios al principio o al final del string pasado por parámetro.
def ejercicio11(userInput):
	palabraList = userInput.split()
	return len(palabraList[])

resultado = ejercicio11("Bienvenidos a Paradigmas de Programación")
print(resultado)







# Ejercicio 12
#
# En McDonald’s se pueden comprar patitas de pollo en 6, 9 o 20 unidades. Crear un programa que, a partir de un número, decida si es posible comprar esa cantidad de patitas.
#
#
