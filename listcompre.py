# ejemplo 1 / modelo tradicional
# lista = []
# for numero in range (0,11):
# lista.append (numero ** 2)
# print (lista)
#Modelo suprimido en Lista
# lista_c = [numero ** 2 for numero in range (0,11)]
# print (lista_c)


# ejemplo 2, modelo tradicional
lista  = []
for  numero  in  range ( 0 , 11 ):
    if  numero  %  2  ==  0 :
        lista.append(numero ** 2)
        #Append, significa añadir en lista)
print ( lista )

#modelo suprimido en Lista
"""lista_c  = [ numero  ** 2  for  numero  in  range ( 0 , 11 ) if  numero  %  2  ==  0 ]
print ( lista_c )"""
