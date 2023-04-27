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

