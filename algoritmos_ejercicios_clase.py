

"""Realizar un algoritmo para cortar una pizza en 8 porciones, teniendo en cuenta que es 1 pizza, No puede ser pizza/8, y puede que necesite pasar alguna otra referencia. Luego realizar el algoritmo pero con recursividad."""

#resolución de la profe

"""from fractions import Fraction # esta opcion es para que aparezca 1/8, es decir una pizza cortada en 8 porciones

def cortadorPizza(pizza,original,porciones):
       for corte in range(porciones): # recursion es lo que antes utilizabamos como ciclico, o sea como for.
           pizza = pizza/2   # este paso sería la recursión
           if pizza == original/porciones:
              return pizza
print(cortadorPizza(1,1,8))"""

# Resolucion del mismo ejercicio pero por un compañero, de otra manera
"""

def cortadorPizza(pizza,original,porciones):
    if pizza == original/porciones:
         return pizza
    return exercisePizza(pizza / 2, original, porciones)  # este paso sería la recursión, cumple el mismo paso descripto arriba.

print (Fraction(cortadorPizza(1, 1, 8)))"""


"""Escribir un programa que pida una serie de números y luego imprima el cuadrado del mismo, utilizando compresión de listas."""

"""
def cuadrados():
    lista = []
    for i in range (4):
        lista.append(int(input(f" Ingrese el numero { i + 1}: ")))
    return [i * i for i in lista] # esta es la manera de escribir una listcomprenhension, lo que esta dentro del []

print (cuadrados())
"""

"""Escribir una función que reciba un número positivo n y devuelva la cantidad de dígitos que tiene, utilizando recursividad."""
# los digitos son las decenas , un digito es el equivalente a 10, por ejemmplo 123 cuantos digitos tiene, tiene 3
# el truco para este contador es utilizar una Variable como contador, para que en cada recursion o iteracion en caso que se elija
#for como iterativo. Siempre cuando usemos recursion tiene que ver algun tipo de chequeo con el cual salgamos de la recursion
#entonces probablemnte siempre tengamos un condicional.
"""
def contador_digitos(numero, contador):
    contador += 1
    numero = numero / 10 # aca se divide por 10 porque los digitos son siempre centena.
    if numero <= 1:
        return contador
    return contador_digitos(numero, contador)

print(contador_digitos(6, 0))
"""

"""Dado una lista anidada, por ejemplo : [1, ['a', 'b', 'c'], 2, 3, ['c', 'd', 'e']] , hacer un algoritmo que devuelva los elementos base en una lista y los de sublistas en otra. Deberá usar la función isinstance()."""

# isinstance en python es para chequear que tipo de datos se esta evaluando.

""""def separadorDeListas(lista):
    sub1 = lista.copy() # aca se estan copiando todos los valores que se encuentran en la lista original con la funcion copy que #nos permite que si modificamos los valores del sub1 no me cambie los valores de la lista original.Esto nos ahorra hacer un #For.
    sub2 = []

    for elemento in lista:
        if isinstance(elemento, list): # si elemento es del tipo lista entonces que me lo agregue.
            if len(sub2) > 0:
                sub2 += elemento # aca con el+= en las listas se le agrega o concatena que es lo mismo
            else:
                sub2 = elemento.copy()

            sub1.remove(elemento)

    return sub1, sub2

print(separadorDeListas([1, ['a', 'b', 'c'], 2, 3, ['c', 'd', 'e']]))
"""
