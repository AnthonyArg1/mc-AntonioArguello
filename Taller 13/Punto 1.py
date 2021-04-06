def  vectorial Producto ( vector1 , vector2 ):
    prod  =  0
    # Verificacion
    if ( len ( vector1 ) ==  len ( vector2 )):
        para  n  en el  rango ( len ( vector1 )):
            prod  + =  vector1 [ n ] *  vector2 [ n ]

        print ( f'El producto vectorial es de: { prod } ' )
    otra cosa :
        print ( 'Los vectores no coinciden en tamaño, no se le pueden aplicar el producto vectorial' )


# ingreso de informacion y Definición de variables
aux1  =  int ( input ( 'Escriba el tamaño n de los vectores:' ))
vector1  = []
vector2  = []

# Completado de vector 1
para  n  en  rango ( aux1 ):
    aux2  =  int ( input ( f'Digite el número en la posición { n + 1 } del vector 1: ' ))
    vector1 . añadir ( aux2 )

# Completado de vector 2
para  n  en  rango ( aux1 ):
    aux2  =  int ( input ( f'Digite el número en la posición { n + 1 } del vector 2: ' ))
    vector2 . añadir ( aux2 )

vectorialProduct ( vector1 , vector2 )