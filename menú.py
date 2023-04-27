import re
from archivos import *
from funciones import *
#Validaciones
def validacionRangoMat(fila,columna,matriz):
    '''
    Funcionalidad: Determina si la fila y columna ingresadas existen en la matriz
    Entradas:
    - fila(int): dato ingresado por el usuario
    - columna(int): dato ingresado por el ussuario 
    - matriz(list): matriz base en la que se debe comprobar que exista la columna y fila ingresadas
    Salidas:
    - True
    - False
    '''
    noMenoresCero=int(fila)>0 and int(columna)>0
    if len(matriz)>=int(fila) and len(matriz[0])>=int(columna) and noMenoresCero:
        return True
    return False

def esDigito(num):
    '''
    Funcionalidad: Determina si un dato ingresado es un dígito o no
    Entradas:
    - num(str): dato ingresado por el usuario
    Salidas:
    - True
    - False
    '''
    if re.match("^\d+$",str(num)):
        return True
    return False

def validarDigitos(pnum,tope):
    '''
    Funcionalidad: verifica que el dato ingresado sea un dígito entre 1 y el tope
    Entradas: 
    -pnum: numero a validar
    Salidas:
    -True
    -False
    '''
    if re.match('^[1-'+str(tope)+']$',str(pnum)):
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
    if esDigito(monto):
        if monto!=edificio[int(piso)-1][int(local)-1]:
            return True
        else:
            print("El monto ingresado debe ser diferente al actual") 
    else:
        print('El monto ingresado debe ser un número entero positivo')
    return False

#Funciones de Entrada y salida

def imprimirOpcion1Aux(edificio):
    '''
    Funcionalidad: Imprime y Realiza los cambios necesarios a la matriz en caso de que el usuario elija la opción 1
    Entradas:
    - edificio(list): matriz donde se encuentran registrados los alquileres
    Salidas:
    - edificio(list): matriz con los alquileres nuevos registrados 
    '''
    estado=True
    while estado:
        piso=input("Ingrese el piso en el que se encuentra el local a alquilar: ")
        local=input("Ingrese el número del local a alquilar: ")
        if not(esDigito(piso)and esDigito(local)):
            print("\nDebe ingresar numero entero\n")
            return imprimirOpcion1Aux(edificio)
        if validacionRangoMat(piso,local,edificio):
            if determinarDisponLocal(piso,local,edificio):
                constante=True
                while constante:
                    monto=input("Ingrese el monto del alquiler: ")
                    if validacionMonto(monto,edificio,piso,local):
                        constante=False
                edificio=definirRenta(piso,local,monto,edificio)
                print("El alquiler del local fue registrado correctamente")
            else:
                print("\nEl local no se encuentra disponible")
                print("\nPor favor ingrese un numero de local disponible")
        else:
            print("\nEl local ingresado no existe, por favor verifique que: ")
            print("El número de piso este entre 1-"+str(len(edificio))+"\nEl número de local este entre 1-"+str(len(edificio[0]))+"\n")
        estado=contestacion("¿Desea continuar alquilando locales?")
    return edificio

def imprimirOpcion2Aux(edificio):
    '''
    Funcionalidad: Imprime y Realiza los cambios necesarios a la matriz en caso de que el usuario elija la opción 2
    Entradas:
    - edificio(list): matriz donde se encuentran registrados los alquileres
    Salidas:
    - edificio(list): matriz con los alquileres nuevos registrados 
    '''
    estado=True
    while estado:
        piso=input("Ingrese el piso en el que se encuentra el local a modificar: ")
        local=input("Ingrese el número del local a modificar: ")
        if not(esDigito(piso)and esDigito(local)):
            print("\nDebe ingresar numero entero\n")
            return imprimirOpcion2Aux(edificio)
        if validacionRangoMat(piso,local,edificio):
            if determinarDisponLocal(piso,local,edificio)==False:
                contesta=contestacion('¿Está seguro que desea alterar la renta actual del local?')
                if contesta:
                    constante=True
                    while constante:
                        monto=input("Ingrese el nuevo monto del alquiler: ")
                        if validacionMonto(monto,edificio,piso,local):
                            constante=False
                    edificio=definirRenta(piso,local,monto,edificio)
                    print('¡El alquiler del local fue modificado satisfactoriamente!')
            else:
                print("\nEl local no se encuentra alquilado\nPor favor ingrese un numero de local que pueda modificarse")
        else:
            print("El local ingresado no existe, por favor verifique que: ")
            print("El número de piso este entre 1-"+str(len(edificio))+"\nEl número de local este entre 1-"+str(len(edificio[0]))+"\n")
        estado=contestacion("¿Desea continuar modificando alquileres?")
    return edificio

def imprimirOpcion3Aux(edificio):
    '''
    Funcionalidad: Imprime y Realiza los cambios necesarios a la matriz en caso de que el usuario elija la opción 3
    Entradas:
    - edificio(list): matriz donde se encuentran registrados los alquileres
    Salidas:
    - edificio(list): matriz con los alquileres nuevos registrados 
    '''
    estado=True
    while estado:
        piso=input("Ingrese el piso en el que se encuentra el local a desalojar: ")
        local=input("Ingrese el número del local a desalojar: ")
        if not(esDigito(piso)and esDigito(local)):
            print("\nDebe ingresar numero entero\n")
            return imprimirOpcion3Aux(edificio)
        if validacionRangoMat(piso,local,edificio):
            if determinarDisponLocal(piso,local,edificio)==False:
                contesta=contestacion('¿Está seguro que desea desalojar este local?')
                if not contesta:
                    print("El local no se ha desalojado")
                else:
                    edificio=definirRenta(piso,local,0,edificio)
                    print("El local se ha desalojado de manera correcta")
            else:
                print("\nEl local no se encuentra alquilado\nPor favor ingrese un numero de local que si esté alquilado, para desalojarlo")
        else:
            print("El local ingresado no existe, por favor verifique que: ")
            print("El número de piso este entre 1-"+str(len(edificio))+"\nEl número de local este entre 1-"+str(len(edificio[0]))+"\n")
        estado=contestacion("¿Desea continuar desalojando locales?")
    return edificio

def indicarIngresoXLocal(piso,local,edificio):
    '''
    Funcionalidad: Indica los ingresos que genera un local específico 
    Entradas:
    - piso(int): piso en el que se encuentra ubicado el local
    - local(int): número de local a indicar sus ingresos 
    - edificio(list): matriz donde se encuentran registrados los alquileres
    Salidas:
    - edificio[int(piso)-1][int(local)-1](list): ingresos del local especificado
    '''
    if not validacionRangoMat(piso,local,edificio):
        print("El local ingresado no existe, por favor verifique que: ")
        print("El número de piso este entre 1-"+str(len(edificio))+"\nEl número de local este entre 1-"+str(len(edificio[0]))+"\n")
        return False    
    if determinarDisponLocal(piso,local,edificio):
        print("\nEl local no está alquilado")
    return edificio[int(piso)-1][int(local)-1]

def indicarIngresoXPiso(piso,edificio):
    '''
    Funcionalidad: Indica los ingresos que genera un piso específico
    Entradas:
    - piso(int): piso a determinar cuantos ingresos generan
    - edificio(list): matriz donde se encuentran registrados los alquileres
    Salidas:
    - totalPiso(int): ingresos totales generados por el piso especficado 
    '''
    if not validacionRangoMat(piso,1,edificio):
        print("El local ingresado no existe, por favor verifique que: ")
        print("El número de piso este entre 1-"+str(len(edificio)))
        return False
    totalPiso= 0
    print("\nPiso #"+str(piso))
    for i in range(len(edificio[int(piso)-1])):
        print("Local #"+str(i+1))
        print("Monto de alquiler $: "+str(edificio[int(piso)-1][i]))
        totalPiso+=int(edificio[int(piso)-1][i])
    return totalPiso

def indicarIngresoXColumna(columna,edificio):
    '''
    Funcionalidad: Indica los ingresos que genera una columna en específico
    Entradas:
    - columna(int): columna a determinar los ingresos que genera
    - edificio(list): matriz donde se encuentran registrados los alquileres
    Salidas:
    - totalPiso(int): ingresos totales generados por la columna especficada
    '''
    if not validacionRangoMat(1,columna,edificio):
        print("El local ingresado no existe, por favor verifique que: ")
        print("El número de columna este entre 1-"+str(len(edificio[0])))
        return False
    totalColumna=0
    for i in range(len(edificio)):
        print("\nPiso #"+str(i+1))
        print("Local #"+str(columna))
        print("Monto de alquiler $: "+str(edificio[i][int(columna)-1]))
        totalColumna+=int(edificio[i][int(columna)-1])
    return totalColumna

def indicarIngresoTotal(edificio):
    '''
    Funcionalidad: Indica los ingresos que genera en total todo el edificio
    Entradas:
    - edificio(list): matriz donde se encuentran registrados los alquileres
    Salidas:
    - total(int): Ingresos totales generados por el edificio
    '''
    total= 0
    for piso in range(len(edificio)):
        for i in range(len(edificio[piso])):
            print("\nPiso #"+str(piso+1))
            print("Local #"+str(i+1))
            print("Monto de alquiler $: "+str(edificio[piso][i]))
            total+=int(edificio[piso][i])
    return total

def imprimirMenuOpcion4():
    '''
    Funcionalidad: Imprime el menú de la opción 4 y le d ala opción de escoger al usuario
    Entradas:
    - N/A
    Salidas:
    - opción(int): opción deseada por el usuario 
    '''
    print("\n"+"MENÚ DE INGRESOS".center(90,"="))
    print("Indique en qué formato desea ver los ingresos del edificio:")
    print("   1.Por local\n   2.Por piso\n   3.Por columna\n   4.Totalidad del edificio\n   5.Salir\n")
    opcion=input("Digite el número de la opción a escoger: ")
    if validarDigitos(opcion,5):
        return opcion
    print("Debe ingresar un numero del 1 al 5")
    return imprimirMenuOpcion4()
    
def imprimirOpcion4Aux(edificio):
    '''
    Funcionalidad: Imprime en caso de que el usuario elija la opción 4
    Entradas:
    - edificio(list): matriz que contiene los alquileres del edificio
    Salidas:
    - N/A
    '''
    estado=True
    while estado:
        opcion=imprimirMenuOpcion4()
        if int(opcion)==1:
            piso=input("Ingrese el numero de piso en el que se encuentra el local: " )
            local=input("Ingrese el número del local del cual desea saber los ingresos: ") 
            if not(esDigito(piso)and esDigito(local)):
                print("El piso y el local deben indicarse por medio de un numero entero")
                return imprimirOpcion4Aux(edificio)
            if not validacionRangoMat(piso,local,edificio):
                print("El número de piso este entre 1-"+str(len(edificio))+"\nEl número de local este entre 1-"+str(len(edificio[0]))+"\n")
                return imprimirOpcion4Aux(edificio)
            total=indicarIngresoXLocal(piso,local,edificio)
            if total!=False:
                print("El ingreso del local es: "+str(total))
        elif int(opcion)==2:
            piso=input("Ingrese el número del piso de la cual desea saber los ingresos: ")
            if not(esDigito(piso)):
                print("El piso deben indicarse por medio de un numero entero")
                return imprimirOpcion4Aux(edificio)
            if not validacionRangoMat(piso,1,edificio):
                print("El número de piso este entre 1-"+str(len(edificio))+"\nEl número de local este entre 1-"+str(len(edificio[0]))+"\n")
                return imprimirOpcion4Aux(edificio)
            total=indicarIngresoXPiso(piso,edificio)
            if total!=False:
                print("Para un total de ingresos del piso de $:"+str(total))
        elif int(opcion)==3:
            columna=input("Ingrese el número de la columna de la cual desea saber los ingresos: ")
            if not(esDigito(columna)):
                print("La columna debe indicarse por medio de un numero entero")
                return imprimirOpcion4Aux(edificio)
            if not validacionRangoMat(1,columna,edificio):
                print("El número de piso este entre 1-"+str(len(edificio))+"\nEl número de local este entre 1-"+str(len(edificio[0]))+"\n")
                return imprimirOpcion4Aux(edificio)
            total=indicarIngresoXColumna(columna,edificio)
            if total!=False:
                print("Para un total de ingresos por columna de $:"+str(total))
        elif int(opcion)==4:
            total=indicarIngresoTotal(edificio)
            if total!=False:
                print("\nPara un total de ganancias de $: "+str(total))
        else:
            return""

def imprimirOpcion5Aux(edificio):
    '''
    Funcionalidad: imprime lo necesario en caso de que el usuario ingrese la opción 5
    Entradas:
    - edificio(list): matriz que contiene los alquileres 
    Salidas:
    - N/A
    '''
    print("Reporte total del Edificio".center(90,"="))
    disponibles=calDisponiblesyOcupados(edificio)[0]
    ocupados=calDisponiblesyOcupados(edificio)[1]
    print("\nTotal de locales alquilados: "+str(ocupados)+", para un porcentaje de: "+str(round(calcularPorcentajeMat(ocupados,edificio),2))+"%")
    print("Total de locales desocupados: "+str(disponibles)+", para un porcentaje de: "+str(round(calcularPorcentajeMat(disponibles,edificio),2))+"%")
    return ""

def imprimirMenu():
    '''
    Funcionalidad: imprime el menú de opciones al usuario
    Entradas:
    - N/A
    Salidas:
    - opción(int): opción escogida por el usuario
    '''
    while True:
        print("\n"+"Menú".center(90,"="))
        print("\n   1. Alquilar local\n   2. Modificar renta de un local\n   3. Desalojar local")
        print("   4. Indicar ingreso por alquiler\n   5. Reporte total del edificio\n   6. Salir\n")
        opcion=input("Ingrese la opción deseada: ")
        if not validarDigitos(opcion,6):
            print("Opción no válida")
            print("Debe ingresar un valor entero entre 1-6")
        else:
            break
    return opcion

def menuArchivos():
    '''
    Funcionalidad: Verifica si el usuario ya posee datos anteriores, en caso de que si, los carga;
    de otra forma crea un archivo nuevo 
    Entradas:
    - N/A
    Salidas:
    - archivo: el archivo antiguo, o el nombre del archivo a crear
    '''
    print('Por favor indique 1 o 2, correspondiente a la opción que desea'
          '\n1: Ya tengo registrado mi edificio, deseo acceder a él'
          '\n2: Quiero crear un archivo nuevo con mi edificio'
    )
    valor=input('Ingrese aquí "1" o "2": ')
    if not validarDigitos(valor,2):
        print('Debe ingresar únicamente "1" o "2"')
        return menuArchivos()
    intentar=True
    while intentar:
        if int(valor)==1:
            nombreArchivo=input('Ingrese el nombre que le colocó a su edificio: ')
            try: 
                archivo=leerArchivoB(nombreArchivo)
                intentar=False
            except:
                print('Carga de archivo fallida... ')
                print('El nombre que ingresó no existe. ')
                respuesta=contestacion('¿Desea volver a intentarlo? En caso de indicar "N" se procederá a crear un nuevo archivo')
                if not respuesta:
                    valor=2
                intentar=True
        else: 
            nombreArchivo=input('Ingrese el nombre que desea colocarle a su edificio: ')
            intentar=False
            archivo=''
    return archivo,nombreArchivo

def EyS():
    '''
    Funcionalidad: Entradas y salidas 
    Entradas:
    - N/A
    Salidas:
    - N/A
    '''
    print("Bienvenido al Sistema de Administración de Locales".center(90,"="))
    archivo=menuArchivos()[0]
    nombreArchivo=menuArchivos()[1]
    constante=True
    while constante:
        if archivo=='':
            cantPisos=input("Por favor ingrese la cantidad de pisos de su edificio: ")
            cantLocales=input("Por favor ingrese la cantidad de locales por piso: ")
            if not (esDigito(cantPisos) and esDigito(cantLocales)):
                print("\nDebe ingresar número enteros positivos mayores que 0\nPor favor inténtelo nuevamente\n")
            else: 
                edificio=generarMatriz(cantPisos,cantLocales)
                guardarArchivoB(nombreArchivo,edificio)
                constante=False
        else:
            edificio=archivo
            constante=False
    respuesta=False
    while not respuesta:
        opcion=imprimirMenu()
        if int(opcion)==1:
            edificio=imprimirOpcion1Aux(edificio)
        elif int(opcion)==2:
            edificio=imprimirOpcion2Aux(edificio)
        elif int(opcion)==3:
            edificio=imprimirOpcion3Aux(edificio)
        elif int(opcion)==4:
            imprimirOpcion4Aux(edificio)
        elif int(opcion)==5:
            imprimirOpcion5Aux(edificio)
        else:
            respuesta=contestacion('¿Está seguro que desea salir?')
    print(guardarArchivoB(nombreArchivo,edificio))
    print('\n'+'¡Gracias por utilizar el sistema!'.center(90,' '))
    print('\n'+'FIN'.center(90,'='))
    return ''

#Progrma principal
EyS()