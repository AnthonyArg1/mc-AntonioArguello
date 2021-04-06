importar  numpy  como  np

# Método para llenar la matriz
def  fillMatrix ( fila , columna ):
    matriz  = []

    # Se hace una lista de listas, en las que cada lista equivale a una fila de la matriz
    para  n  en  rango ( fila ):
        aux  = []
        para  m  en  rango ( columna ):
            aux . append (
                int ( input ( f'Digite el número de la posición { n } , { m } de la matriz: ' )))
        matriz . añadir ( aux )

    print ( f ' \ n La matriz creada es la siguiente: \ n { np . asmatrix ( matriz ) } \ n ' )
    return  np . asmatrix ( matriz )

# Método para el producto escalar de un entero y una matriz
def  pointMatrix ( escalar , original_matrix ):
    matriz  =  matriz_original . copiar ()
    para  n  en  gama ( matriz . forma [ 0 ]):
        para  m  en el  rango ( matriz . forma [ 1 ]):
            matriz [ n , m ] = matriz [ n , m ] *  escalar
    imprimir ( f ' { matriz } \ n ' )

# Método para la suma de dos 
def  sumMatrix ( matriz1 , matriz2 ):
    if ( matriz1 . forma  ==  matriz2 . forma ):
        matriz  =  np . ceros (( matriz1 . forma [ 0 ], matriz1 . forma [ 1 ]))
        para  n  en  gama ( matriz . forma [ 0 ]):
            para  m  en el  rango ( matriz . forma [ 1 ]):
                matriz [ n , m ] =  matriz1 [ n , m ] +  matriz2 [ n , m ]
        imprimir ( f ' { matriz } \ n ' )
    otra cosa :
        print ( 'Las matrices no coinciden en tamaño, no se puede realizar la suma' )

# Definir tamaños
filas1  =  int ( input ( 'Defina las filas de la matriz 1:' ))
columnas1  =  int ( input ( 'Defina las columnas de la matriz 1:' ))

filas2  =  int ( input ( 'Defina las filas de la matriz 2:' ))
columnas2  =  int ( input ( 'Defina las columnas de la matriz 2:' ))

# Digitar datos con el método para llenar la matriz
print ( ' \ n Digitado de datos de la matriz 1 \ n \ n ' )
matriz1  =  fillMatrix ( rows1 , columns1 )

print ( ' \ n \ n Digitado de datos de la matriz 2 \ n \ n ' )
matrix2  =  fillMatrix ( filas2 , columnas2 )

# Imprimir la matriz
imprimir ( f'Matriz A: \ n  { matriz1 } \ n ' )
imprimir ( f'Matriz B: \ n  { matriz2 } \ n ' )

# Operación 3A
imprimir ( 'Matriz 3A:' )
pointMatrix ( 3 , matriz1 )

# Operación 4B
imprimir ( 'Matriz 4B:' )
pointMatrix ( 4 , matriz2 )

# Operación A + B
imprimir ( 'Matriz A + B:' )
sumMatrix ( matriz1 , matriz2 )

# Operación B x A
imprimir ( 'Matriz BxA:' )
prueba :
    imprimir ( np . cruz ( matriz2 , matriz1 ))
excepto :
    print ( 'Las matrices no cumplen con las condiciones para poder realizar el producto vectorial' )