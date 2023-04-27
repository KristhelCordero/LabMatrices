#Elaborado por: Kristel Cordero y Kendall Piedra
#Fecha de creación: 22/4/2023 11:00am
#Ultima versión: 27/4/2023 1:00am
#Versión: 3.10.6 
def determinarDisponLocal(piso,local,matriz):
    '''
    Funcionalidad: Determina si el monto ingresado por el usuario es digito y diferente al anterior registrado 
    Entradas:
    - monto(int): nuevo alquiler ingresado por el usuario
    - piso(int): piso donde se encuentra el local 
    - local(int): número de local
    - edificio(list): matriz donde se encuentran registrados los alquileres
    Salidas:
    - True
    - False
    '''
    if matriz[int(piso)-1][int(local)-1]==0:
        return True
    return False

def generarMatriz(filas,columnas):
    '''
    Funcionalidad: Genera una matriz donde todos los valores dentro de las listas son 0 
    Entradas:
    - filas(int): cantidad de listas que conformarán la matriz
    - columanas(int): cantidad de 0's que tendrá cada lista dentro de la matriz
    Salidas:
    - matriz(list): matriz generada
    '''
    matriz=[]
    for i in range(int(filas)):
        matriz.append([])
        for y in range(int(columnas)):
            matriz[i].append(0)
    return matriz

def definirRenta(piso,local,alquiler,matriz):
    '''
    Funcionalidad: Modifica los montos de renta dentro de la matriz 
    Entradas:
    - alquiler(int): nueva renta ingresada por el usuario
    - piso(int): piso donde se encuentra el local 
    - local(int): número de local
    - matriz(list): matriz donde se encuentran registrados los alquileres
    Salidas:
    - matriz(list): matriz con los montos modificados
    '''
    matriz[int(piso)-1][int(local)-1]=alquiler
    return matriz

def calcularPorcentajeMat(pnum,pmat):
    '''
    Funcionalidad: calcula con un número ingresado que indica una cantidad de elementos su porcentaje dentro de la matriz
    Entradas:
    -pnum: numero de elementos a sacar porcentaje
    -matriz: matriz a comparar
    Salidas:
    - porcentaje de elementos ingresados comparado con el total de elementos de la matriz
    '''
    resultado=0
    totalElementos=0
    for f in range(len(pmat)):
        for c in range(len(pmat[f])):
            totalElementos+=1
    resultado=(pnum*100)/totalElementos
    return resultado

def calDisponiblesyOcupados(pmat):
    '''
    Funcionalidad: Realiza el cálculo de los locales que se encuentran disponibles y ocupados
    Entradas:
    - pmat(list): matriz con los datos de los alquileres 
    Salidas:
    - [cantDisponibles,cantOcupados](list): Lista con la cantidad de locales disponibles y desocupados 
    '''
    cantDisponibles=0
    cantOcupados=0
    for f in range(len(pmat)):
        for c in range(len(pmat[f])):
            if pmat[f][c]==0:
                cantDisponibles+=1
            else:
                cantOcupados+=1
    return [cantDisponibles,cantOcupados]