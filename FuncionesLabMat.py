import re

def contestacion():
    '''
    Funcionalidad: Pide al usuario una contestacion y se repite hasta que sea valida
    Entradas: 
    -Respuesta escrita por el usuario 
    Salidas:
    -Respuesta validada
    '''
    respuesta=''
    while not re.match('^[sSnN]$',respuesta):
        respuesta=input('\n¿Desea alquilar otro local?\nDigite S = si o N = no: ')
        if not re.match('^[sSnN]$',respuesta):
            print('Debe ingresar "S" o "N"')
    if re.match('^[sS]$',respuesta):
        return True            
    return False

def generarMatriz(filas,columnas):
    matriz=[]
    for i in range(int(filas)):
        matriz.append([])
        for y in range(int(columnas)):
            matriz[i].append(0)
    return matriz
def determinarDisponLocal(piso,local,matriz):
    if matriz[piso][local]==0:
        return True
    return False

def definirRenta(piso,local,alquiler,matriz):
    matriz[piso][local]=alquiler
    return matriz

def opcion1Aux(edificio):
    estado=True
    while estado:
        piso=input("Ingrese el piso en el que se encuentra el local a alquilar: ")
        local=input("Ingrese el número del local a alquilar: ")
        if determinarDisponLocal(piso,local,edificio):
            monto=input("Ingrese el monto del alquiler: ")
            edificio=definirRenta(piso,local,monto,edificio)
            print("El alquiler del local fue registrado correctamente")
            estado=contestacion()
        else:
            print("¡¡¡Algo anda mal!!!\n El local no se encuentra disponible\nPor favor ingrese un numero de local disponible")
    return edificio

def EyS():
    print("Bienvenido al Sistema de Administración de Locales".center(90,"="))
    cantPisos=input("Por favor ingrese la cantidad de pisos de su edificio: ")
    cantLocales=input("Por favor ingrese la cantidad de locales por piso: ")
    edificio=generarMatriz(cantPisos,cantLocales)
    print("\nMenú".center(90,"="))
    print("\n   1. Alquilar local\n   2. Modificar renta de un local\n   3. Desalojar local")
    print("\n   4. Indicar ingreso por alquiler\n   5. Reporte total del edificio\n   6. Salir\n")
    opcion=input("Ingrese la opción deseada: ")
    if int(opcion)==1:
        edificio=opcion1Aux(edificio)
    elif int(opcion)==2:'''
        edificio=opcion2Aux(edificio)
    elif int(opcion)==3:
        edificio=opcion3Aux(edificio)
    elif int(opcion)==4:
        opcion4Aux(edificio)
    elif int(opcion)==5:
        opcion5Aux(edificio)
    else:
        #salir'''
    

        








EyS()






