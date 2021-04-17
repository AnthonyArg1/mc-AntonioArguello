importar  numpy  como  np
importar  copia

## Resolver por eliminación de Gauss Jordan la matriz inversa

# Hacer la diagonal principal y la parte de abajo de la matriz identidad
def  gaussJordan ( matriz ):
    n  =  0
    mientras que es  verdadero :
        # Cuando se termine el proceso, n será mayor que la longitud de la matriz
        si ( n  > =  len ( matriz )):
             matriz de retorno

        # Si la diagonal es 0, se cambia de posición con otra fila
        si ( matriz [ n ] [ n ] ==  0 ):
            isZero ( matriz , n )
            imprimir (
                f ' \ n Se cambiaron las filas de la matriz: \ n { np . asmatrix ( matriz ) } ' )

        # Si la diagonal es uno, se restan las filas para que se cree la matriz identidad
        elif ( matriz [ n ] [ n ] ==  1 ):
            subsAll ( matriz , n )
            print ( f ' \ n Se restaron filas de la matriz: \ n { np . asmatrix ( matriz ) } ' )
            n  + =  1

        # Cuando la diagonal no sea 1 o 0, se divide la fila para poder crear la fila con la diagonal 1
        otra cosa :
            dividir todo ( matriz , n )
            imprimir (
                f ' \ n Se dividió una fila de la matriz: \ n { np . asmatrix ( matriz ) } ' )

# Método para cambiar de posición las ecuaciones en caso de que el número en la diagonal principal sea 
def  isZero ( matriz , aux1 ):
    aux2  =  0
    mientras que es  verdadero :

        # Si no se puede resolver por Gauss Jordan, salta error
        si ( aux2  > =  len ( matriz ) - 1 ):
            imprimir (
                f'La última iteración de la matriz fue: \ n { np . asmatrix ( matriz ) } ' )
            subir  IndexError ( 'No se puede resolver el sistema por GaussJordan' )

        # Mover las filas por un auxiliar
        aux0  =  matriz [ aux2 + 1 ]
        matriz [ aux2 + 1 ] =  matriz [ aux2 ]
        matriz [ aux1 ] =  aux0

        # Si sigue siendo cero, que siga el bucle infinito
        si ( matriz [ aux1 ] [ aux1 ] ! =  0 ):
             matriz de retorno
        aux2  + =  1

# Método para dividir toda una fila y establecer el número de la diagonal principal como 1
def  divideAll ( matriz , n ):
    aux0  =  0
    aux1  =  matriz [ n ] [ n ]
    para el  número  en la  matriz [ n ]:
        matriz [ n ] [ aux0 ] =  número  /  aux1
        aux0  + =  1
     matriz de retorno

# Método para restar una fila que ya tenga su número de diagonal principal como 1 con las otras filas
def  subsAll ( matriz , n ):
    aux0  =  0
    mientras que es  verdadero :
        para  fila  en  rango ( len ( matriz )):

            # Si la columna a evaluar es si misma, saltarse ese paso
            si ( fila  ! =  n ):

                # Si ambos numeros son iguales, se restan las filas para que quede 0
                si ( matriz [ n ] [ n ] ==  matriz [ fila ] [ n ]):
                    para el  número  en el  rango ( len ( matriz [ n ])):
                        matriz [ fila ] [ número ] =  matriz [ fila ] [ número ] - \
                            matriz [ n ] [ número ]

                # Si un número en una fila ya es cero, se le suma a un iterador, si todas los números correspondientes son cero, acaba el método
                elif ( matriz [ fila ] [ n ] ==  0 ):
                    aux0  + =  1
                    si ( aux0  ==  len ( matriz )):
                         matriz de retorno

                # Si no es cero, pero tampoco es 1, multiplica la fila con el número correspondiente de la columna y después lo resta
                otra cosa :
                    aux1  =  copiar . copia profunda ( matriz )
                    para el  número  en el  rango ( len ( matriz [ n ])):
                        aux1 [ n ] [ número ] =  aux1 [ n ] [ número ] *  aux1 [ fila ] [ n ]
                    para el  número  en el  rango ( len ( matriz [ n ])):
                        aux1 [ fila ] [ número ] =  aux1 [ fila ] [ número ] -  aux1 [ n ] [ número ]
                    para el  número  en el  rango ( len ( matriz [ n ])):
                        matriz [ fila ] [ número ] =  aux1 [ fila ] [ número ]

# Método para crear una matriz de identidad
def  identityMatrix ( matriz ):
    llenar  = []
    matrixAux  = []
    para  n  en el  rango ( len ( matriz )):
        llenar . claro ()
        para  m  en  rango ( len ( matriz [ n ])):
            si ( n == m ):
                llenar . añadir ( 1 )
            otra cosa :
                llenar . añadir ( 0 )
        matrixAux . añadir ( copiar . copia profunda ( llenar ))
    return  matrixAux

# Método para concatenar una matriz identidad a otra matriz
def  concatenateMatrix ( matriz , identidad ):
    para  n  en el  rango ( len ( matriz )):
        para  m  en  rango ( len ( matriz [ n ])):
            matriz [ n ]. añadir ( identidad [ n ] [ m ])
     matriz de retorno

# Método para imprimir la matriz inversa (También sirve para retornarla) 
def  printInverse ( matriz ):
    n  =  len ( matriz )
    m  =  len ( matriz [ 0 ]) / 2
    llenar  = []
    matrixAux  = []

    para  un  en  rango ( int ( n )):
        llenar . claro ()
        para  b  en el  rango ( int ( m )):
            llenar . añadir ( matriz [ a ] [ b + int ( m )])
        matrixAux . añadir ( copiar . copia profunda ( llenar ))
        
    print ( f ' \ n \ n \ n \ n La matriz inversa es: \ n { np . asmatrix ( matrixAux ) } \ n ' )
    return  matrixAux


# Definir la matriz
matriz  = [[ 0 , 2 , 3 ], [ 4 , 6 , 7 ], [ 2 , - 2 , 6 ]]

# Crear una matriz identidad y concatenarla a la matriz inicial
identidad  =  identidadMatriz ( matriz )
matrix  =  concatenateMatrix ( matriz , identidad )

# Mostrar la matriz inicial
print ( f'La matriz inicial es: \ n { np . asmatrix ( matriz ) } ' )

# Resolver ecuación
gaussJordan ( matriz )
print ( f ' \ n \ n \ n \ n La matriz resuelta es: \ n { np . asmatrix ( matriz ) } \ n ' )

inverso  =  printInverse ( matriz )