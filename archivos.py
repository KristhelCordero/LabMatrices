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
        print("Grabando el archivo: ", nomArchGrabar)
        pickle.dump(lista,f)
        f.close()
        return str(nomArchGrabar)+" grabado con exito"
    except:
        return "Error al grabar el archivo: "+ str(nomArchGrabar) 
    
def leerArchivoB (nomArchLeer):
    '''
    Funcionalidad: Toma una archivo binario y lo lee
    Entradas: 
    - nomArchGLeer: nombre del archivo leer
    Salidas:
    - lista: contenido del archivo, generalmente una lista 
    '''
    f=open(nomArchLeer,"rb")
    print("Leyendo el archivo: ", nomArchLeer)
    lista = pickle.load(f)
    print("Se leyó con exito el archivo: ", nomArchLeer)
    f.close()
    return lista

def sobrescribirArchivo(nomArchivo,lista):
    archivoBinario=open(nomArchivo,"wb")
    listaBytes=bytearray(lista)
    archivoBinario.write(listaBytes)
    archivoBinario.close()
    print('"'+str(nomArchivo)+'" guardado correctamente')
    return lista