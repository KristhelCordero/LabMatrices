import re

def validacionRangoMat(fila,columna,matriz):
    noMenoresCero=fila>=0 and columna>=0
    if len(matriz)>=fila and len(matriz[0])>=columna and noMenoresCero:
        return True
    return False
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
            if monto!=edificio[int(piso)-1][int(local)-1]:
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
    if matriz[int(piso)-1][int(local)-1]==0:
        return True
    return False

def definirRenta(piso,local,alquiler,matriz):
    matriz[int(piso)-1][int(local)-1]=alquiler
    return matriz

def imprimirOpcion1Aux(edificio):
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

def imprimirOpcion2Aux(edificio):
    estado=True
    while estado:
        piso=input("Ingrese el piso en el que se encuentra el local a modificar: ")
        local=input("Ingrese el número del local a modificar: ")
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
            print("¡¡¡Algo anda mal!!!\n El local no se encuentra alquilado\nPor favor ingrese un numero de local que pueda modificarse")
    return edificio

def imprimirOpcion3Aux(edificio):
    estado=True
    while estado:
        piso=input("Ingrese el piso en el que se encuentra el local a desalojar: ")
        local=input("Ingrese el número del local a desalojar: ")
        if determinarDisponLocal(piso,local,edificio)==False:
            contesta=contestacion('¿Está seguro que desea desalojar este local?')
            if not contesta:
                estado=contestacion('¿Desea continuar desalojando locales?')
            else:
                edificio=definirRenta(piso,local,0,edificio)
                print("El local se ha desalojado de manera correcta")
                estado=contestacion('¿Desea desalojar otro local?')
        else:
            print("¡¡¡Algo anda mal!!!")
            print("\nEl local no se encuentra alquilado\nPor favor ingrese un numero de local que si esté alquilado, para modificarlo")
    return edificio

def indicarIngresoXLocal(piso,local,edificio):
    if determinarDisponLocal(piso,local,edificio):
        print("\nEl local no está alquilado")
        return False
    return edificio[int(piso)-1][int(local)-1]

def indicarIngresoXPiso(piso,edificio):
    totalPiso= 0
    print("\nPiso #"+str(piso))
    for i in range(len(edificio[int(piso)-1])):
        print("Local #"+str(i+1))
        print("Monto de alquiler $: "+str(edificio[int(piso)-1][i]))
        totalPiso+=edificio[int(piso)-1][i]
    return totalPiso

def indicarIngresoXColumna(columna,edificio):
    totalColumna=0
    for i in range(len(edificio)):
        print("\nPiso #"+str(i+1))
        print("Local #"+str(columna))
        print("Monto de alquiler $: "+str(edificio[i][int(columna)-1]))
        totalColumna+=edificio[i][int(columna)-1]
    return totalColumna

def indicarIngresoTotal(edificio):
    total= 0
    for piso in range(len(edificio)):
        for i in range(len(edificio[piso])):
            print("\nPiso #"+str(piso+1))
            print("Local #"+str(i+1))
            print("Monto de alquiler $: "+str(edificio[piso][i]))
            total+=edificio[piso][i]
    return total
    
def imprimirOpcion4Aux(edificio):
    estado=True
    while estado:
        print("MENÚ".center(90,"="))
        print("Indique en qué formato desea ver los ingresos del edificio:")
        print("   1.Por local\n   2.Por piso\n   3.Por columna\n   4.Totalidad del edificio\n")
        opcion=input("Digite el número de la opción a escoger: ")
        #validar opcion
        if int(opcion)==1:
            #validar existencia piso y local
            repetirOpcion1=True
            while repetirOpcion1:
                piso=input("\nIngrese el numero de piso en el que se encuentra el local: " )
                local=input("Ingrese el número del local del cual desea saber los ingresos: ")
                total=indicarIngresoXLocal(piso,local,edificio)
                if total!=False:
                    print("\nEl ingreso del local es: "+str(total))
                    repetirOpcion1=False
                else:
                    repetirOpcion1=contestacion("¿Desea ingresar otro local?")
        elif int(opcion)==2:
            #validar existencia piso y local
            piso=input("\nIngrese el número del piso de la cual desea saber los ingresos: ")
            total=indicarIngresoXPiso(piso,edificio)
            print("\nPara un total de ingresos del piso de $: "+str(total))
        elif int(opcion)==3:
            #validar existencia piso y local
            columna=input("\nIngrese el número de la columna de la cual desea saber los ingresos: ")
            total=indicarIngresoXColumna(columna,edificio)
            print("\nPara un total de ingresos por columna de $: "+str(total))
        else:
            total=indicarIngresoTotal(edificio)
            print("\nPara un total de ganancias de $: "+str(total))
        estado=contestacion("Desea continuar consultando ingresos")
    return""

def calDisponiblesyOcupados(pmat):
    cantDisponibles=0
    cantOcupados=0
    for f in range(len(pmat)):
        for c in range(len(pmat[f])):
            if pmat[f][c]==0:
                cantDisponibles+=1
            else:
                cantOcupados+=1
    return [cantDisponibles,cantOcupados]
             
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

def imprimirOpcion5Aux(edificio):
    print("Reporte total del Edificio".center(90,"="))
    disponibles=calDisponiblesyOcupados(edificio)[0]
    ocupados=calDisponiblesyOcupados(edificio)[1]
    print("\nTotal de locales alquilados: "+str(ocupados)+", para un porcentaje de: "+str(round(calcularPorcentajeMat(ocupados,edificio),2))+"%")
    print("Total de locales desocupados: "+str(disponibles)+", para un porcentaje de: "+str(round(calcularPorcentajeMat(disponibles,edificio),2))+"%")
    return ""


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
        edificio=imprimirOpcion1Aux(edificio)
    elif int(opcion)==2:
        edificio=imprimirOpcion2Aux(edificio)
    elif int(opcion)==3:
        edificio=imprimirOpcion3Aux(edificio)
    elif int(opcion)==4:
        imprimirOpcion4Aux(edificio)
    #elif int(opcion)==5:
        imprimirOpcion5Aux(edificio)
    #else:
        #salir
        return ''
    
#print(imprimirOpcion4Aux([[500,200,0],
#                        [100,0,1500],
#                        [0,150,20]]))
print(imprimirOpcion5Aux([[100,100,10,0],
                        [100,10,00,0],
                        [0,100,00,0]]))







