# "" "

Una empresa de autopistas tiene instalada una camara en el peaje que cuenta el numero de vehiculos que pasa, y unas gomas en el piso que cuentan el numero de ruedas de esos vehiculos.
Se pide elaborar un algoritmo que a partir del numero de vehiculos y el numero de ruedas extraiga la cantidad de coches y motos que pasan por allí
# "" "
#autos de 4 ruedas y motos de 2 ruedas.
# entonces por ejemplo seria:

#vehiculos = 3 (ponele un auto  + 2 motos) # Primero tenemos que saber la cant de motos y cant de autos
##ruedas = 10 # coches *4 + motos * 2 # cant de ruedas en total
#, ligado al ejemplo de arriba.
# entonces en codigo seria:

def coches_motos(vehiculos, ruedas):
    for coche in range (1, vehiculos +1): # el 1 al principio quiere decir que va a empezar ahi y lo que continua es la finalización., el +1 es para que no reste el rango, por ejemplo si es 65  que os de la cuenta exacta de 65 y no que nos reste uno y nos de 64. # mas alla de la cant de operaciones que le pusimos, observamos que la cant de operaciones que realiza esta atada a la cant de datos que le pasemos, y eso nos da un ORDEN DE COMPLEJIDAD        n

        for moto in range (1, vehiculos+1): # orden de complejidad n
            print (f"cantidad coches  {coche }  y motos {moto} y de vehiculos { vehiculos}")
            if((coche + moto == vehiculos) and (coche*4+moto*2==ruedas)): # en las operacion y condiciones no importa cuantas operaciones haga de 20,1000 , etc sino que hace en conclusion una sola operacion que esta atada al for de mas arriba, por lo tanto es constante y es 1 ya que se va a multiplica 1*1 .
               print(f" {coche * 4 } +  {moto * 2 } = {ruedas}")
            return coche, moto


# ENTONCES EL ORDEN DE COMPLEJIDAD QUE NOS DA ES O(N2), O SEA QUE CUADRATICA. PERO TAMBIEN SABEMOS QUE SI BIEN VEHICULOS = COCHES + MOTOS . TAMBIEN PUEDE SIMPLIFICARSE A: MOTOS = VECHICULOS - COCHES, ENTONCES AHI SOLO TENDRIAMOS QUE USAR UN FOR Y POR LO TANTO UNA SOLA N. ESTA EXPLICACION ES PARA TERNELO EN CUENTA. Y QUEDARIA POR EJEMPLO: for coche in range (1, vehiculos +1):
                                                                               # moto = vehiculos - coche     y con esta simplificacion nos quedaria O(n) que es la lineal, estariamos haciendo lo mismo. A su vez tambin podriamos seguir simplificando, en este caso las Ruedas junto a Vehiculos, por lo que quedaria de :
                                                                               #motos = vehiculos - coches
                                                                               #ruedas = coche*4+moto*2 y simplificamos quedando todo junto en :
                                                                              #aca estamos utilizando el metodo de sustitucion y de igualdad mutiplicando todo * 2
                                                                               #ruedas = coches * 4 + (vehiculos - coches) * 2
                                    # entonces va quedando: ruedas/2 = coches*4/2+ (vehiculos - coches)*2/2
                                #entonces queda: ruedas/2 = coches * 2 + vehiculos - coches
                                #entonces utilizamos metodo de igualdad:  coches *2 + vehiculos - coches =  ruedas /2
                                #entonces queda : coches = ruedas/2 - vehiculos       ACA LLEGAMOS A NUESTRA MINIMA EXPRESION DE ECUACION, OBTENEMOS CON ESTA SIMPLIFICACION LA CANT DE COCHES Y

coches_motos(6,20)



EN ESTE EJEMPLO TENEMOS LA SIMPLIFICACION HASTA LINEAL

# ORDEN DE COMPLEJIDAD = O (n) lineal
def  cochesYmotosLineal ( vehiculos , ruedas ):
    para  coche  en  rango ( vehiculos  +  1 ): # N
        moto  =  vehiculos  -  coche
        print ( f "cantidad coches { coche } y motos { moto } y de vehiculos {  vehiculos } " )

        if (( coche  +  moto  ==  vehiculos ) y ( coche  *  4  +  moto  *  2  ==  ruedas )):
            print ( f " { coche  *  4 } + { moto * 2 } = { ruedas } " )
            volver  coche , moto

cochesYmotosLineal ( 6 , 20 )

EN ESTA QUEDA CONSTANTE, LA PROFE HIZO QUE SEA AL FINAL LA SIMPLIFICACION DEL EJERCICIO Y QUE QUEDARA ASI:

# ORDEN COMPLEJIDAD ES : O (1) constante, YA QUE 1*1*1 ES 1

def  cochesYmotos ( vehiculos , ruedas ):
    coche  =  ruedas / 2  -  vehiculos  # 1
    moto  =  vehiculos  -  coche  # 1
    print ( f "cantidad coches { coche } y motos { moto } y de vehiculos {  vehiculos } " )

    if ( int ( coche ) +  int ( moto ) ==  vehiculos ): # 1
        print ( f " { int ( coche ) *  4 } + { int ( moto ) * 2 } = { ruedas } " )
        return  int ( coche ), int ( moto )

cochesYmotos ( 6 , 20 )





HICIMOS LOS TRES TIPOS DE ORDEN DE COMPLEJIDAD QUE EXPLICÓ LA PROFE, PRIMERO EL ORDEN DE COMPLEJIDAD CUADRATICA, LUEGO LA LINEAL Y POR ULTIMO LA CONSTANTE.




ESTO SERíA LA LÓGICA DE MATEMÁTICAS

x+y1 = 3

x+y = 3-1
x+y = 2   # ponele que sea el resultado de los vehiculos para el primer ejercicio.

# para el segundo ejercicio seria, ponele:

4x+2y = 10
# Simplificando quedaria

4x+2y = 10

y diviendo en cada lado de la igualdad, sacamos la mitad de cada conjunto, entonces seria:

2x+y = 5

Entonces quedarian 2 ecuaciones con 2 incognitas

x + y = 2
2x+y = 5

Entonces podemos restar ambas ecuaciones que quedaria:

x = 3

y, sustituyendo el valor de x en cualquiera de las dos ecuaciones del sistema, obtenemos el valor de y:

y =

Por lo tanto, podemos concluir diciendo que hay
