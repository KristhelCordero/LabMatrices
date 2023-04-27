#Elaborado por: Kristel Cordero y Kendall Piedra
#Fecha de creación: 22/4/2023 11:00am
#Ultima versión: 27/4/2023 1:00am
#Versión: 3.10.6 
import pickle

def guardarArchivoB(nomArchGrabar,lista):
    '''
    Funcionalidad: Toma una lista y la graba en un archivo binario
    Entradas: 
    -nomArchGrabar: nombre del archivo a generar
    -lista: lista a ser grabada en el archivo
    Salidas:
    -Mensajes notificando el estado de la grabacion 
    -Archivo grabado  
    '''
    try:
        f=open(nomArchGrabar,"wb")
        print("Guardando el edificio: ", nomArchGrabar)
        pickle.dump(lista,f)
        f.close()
        return str(nomArchGrabar)+" guardado con exito"
    except:
        return "Error al guardar: "+ str(nomArchGrabar) 
    
def leerArchivoB (nomArchLeer):
    '''
    Funcionalidad: Toma una archivo binario y lo lee
    Entradas: 
    - nomArchGLeer: nombre del archivo leer
    Salidas:
    - lista: contenido del archivo, generalmente una lista 
    '''
    f=open(nomArchLeer,"rb")
    print("Buscando el edificio: ", nomArchLeer)
    lista = pickle.load(f)
    print("Se encontró: ", nomArchLeer)
    f.close()
    return lista

def guardarEnBD(nomArchGrabar,edificio):
    '''
    Funcionalidad: Toma una lista y la graba dentro de una base de datos binaria
    Entradas: 
    -nomArchGrabar: nombre del archivo a generar
    -lista: lista a ser grabada en el archivo
    Salidas:
    -Mensajes notificando el estado de la grabacion 
    -Archivo grabado  
    '''
    f=open("BD","rb")
    lista = pickle.load(f)
    f.close()
    lista.append((nomArchGrabar,edificio))
    try:
        f=open("BD","wb")
        print("Guardando el edificio: ", nomArchGrabar)
        pickle.dump(lista,f)
        f.close()
        return str(nomArchGrabar)+" guardado con exito"
    except:
        return "Error al guardar: "+ str(nomArchGrabar) 
    
def leerDeBD(nomArchLeer):
    '''
    Funcionalidad: lee un edificio en especifico de la base de datos
    Entradas: 
    -nomArchGrabar: nombre del edificio a encontrar
    Salidas:
    -Mensajes notificando la busqueda del edificio 
    -Archivo grabado  
    '''
    f=open("BD","rb")
    lista = pickle.load(f)
    f.close()
    for i in range(len(lista)):
        print("Buscando el edificio...")
        if lista[i][0]==nomArchLeer:
            print("Edificio encontrado")
            return lista[i]
        return #######NOSE
    

