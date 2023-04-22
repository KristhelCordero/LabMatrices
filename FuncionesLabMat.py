import re

def contestacion(mensaje):
    '''
    Funcionalidad: Pide al usuario una contestacion y se repite hasta que sea valida
    Entradas: 
    -Respuesta escrita por el usuario 
    Salidas:
    -Respuesta validada
    '''
    respuesta=''
    while not re.match('^[sSnN]$',respuesta):
        respuesta=input('\n'+str(mensaje)+'\nDigite S = si o N = no: ')
        if not re.match('^[sSnN]$',respuesta):
            print('Debe ingresar "S" o "N"')
    if re.match('^[sS]$',respuesta):
        return True            
    return False

def validacionMonto(monto,edificio,piso,local):
    estado=True
    while estado:
        if re.match('^\d+$',str(monto)):
            if monto!=edificio[int(piso)][int(local)]:
                return True
        else:
            print('El monto ingresado debe ser un número entero positivo')
    return False
            
def generarMatriz(filas,columnas):
    matriz=[]
    for i in range(int(filas)):
        matriz.append([])
        for y in range(int(columnas)):
            matriz[i].append(0)
    return matriz

def determinarDisponLocal(piso,local,matriz):
    if matriz[int(piso)][int(local)]==0:
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
            estado=contestacion('¿Desea alquilar otro local?')
        else:
            print("¡¡¡Algo anda mal!!!\n El local no se encuentra disponible\nPor favor ingrese un numero de local disponible")
    return edificio

def opcion2Aux(edificio):
    estado=True
    while estado:
        piso=input("Ingrese el piso en el que se encuentra el local a modificar: ")
        local=input("Ingrese el número del local a alquilar: ")
        if determinarDisponLocal(piso,local,edificio)==False:
            contesta=contestacion('¿Está seguro que desea alterar la renta actual del local?')
            if not contesta:
                estado=contestacion('¿Desea continuar modificando alquileres?')
            else:
                monto=input("Ingrese el nuevo monto del alquiler: ")
                if validacionMonto(monto,edificio,piso,local):
                    edificio=definirRenta(piso,local,monto,edificio)
                    print('¡El alquiler del local fue modificado satisfactoriamente!')
                    estado=contestacion('¿Desea continuar modificando alquileres?')
        else:
            print("¡¡¡Algo anda mal!!!\n El local no se encuentra disponible\nPor favor ingrese un numero de local disponible")
    return edificio

def opcion3Aux(edificio):
    return ''


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
    elif int(opcion)==2:
        edificio=opcion2Aux(edificio)
    elif int(opcion)==3:
        edificio=opcion3Aux(edificio)
    elif int(opcion)==4:
        opcion4Aux(edificio)
    elif int(opcion)==5:
        opcion5Aux(edificio)
    else:
        #salir
        return ''
    

        


print(opcion2Aux([[0,1,0],[0,0,0],[0,0,0]]))





