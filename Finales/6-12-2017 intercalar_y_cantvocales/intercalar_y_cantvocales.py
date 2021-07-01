'''
#3.1)Desarrollar la función INTERCALAR que recibe por parámetro 2 listas de numeros
#enteros. La función retorna una tercer lista cuyos valores son partes intercalados
#de cada lista pasada por parámetro. Como la cantidad de datos de cada lista no es
#fija, considerar si se debe terminar de cargar la nueva lista sólo con valores
#de la lista mas larga.

#L1 = [1,2,5,6,9,10,13,14,15,16]
#L2 = [3,4,7,8,11,12]

#intercalar(L1,L2) --> L3 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

#ACLARACION: NO se deben modificar las listas que son pasadas por parámetro;
#y no es necesario crear listas auxiliares (sólo la de retorno).

def ordenarLst(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
    return lst


def intercalar(lst1,lst2):
    lst3 = lst1+lst2
    lst3 = ordenarLst(lst3)
    return lst3

    
    
def main():
    lst1 = [1,2,5,6,9,10,13,14,15,16]
    lst2 = [3,4,7,8,11,12]
    print(intercalar(lst1,lst2))
main()
'''
#3.2)Desarrollar la funcion CANTVOCALES que recibe por parámetro un string
#del nombre de un archivo CSV en el cual, por cada línea, se encuentran palabras
#sueltas separadas por comas. La función deberá imprimir por pantalla un listado
#con cada palabra del archivo junto con la cantidad de vocales que contiene esa
#palabra. No se deben repetir las palabras si aparecen más de una vez en el archivo.

#hola,chau,esperar --> hola: 2 vocales
#nota,lapicera,hola    esperar: 3 vocales
#                      nota: 2 vocales

def esPalabra(palabra):
    string = ""
    for i in palabra:
        if i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
            i = chr(ord(i)+32)
            string+=i
        elif i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            string+=i
        elif i=='á' or i=='Á':
            string+='a'
        elif i=='é' or i=='É':
            string+='e'
        elif i=='í' or i=='Í':
            string+='i'
        elif i=='ó' or i=='Ó':
            string+='o'
        elif i=='ú' or i=='Ú':
            string+='u'
        else:
            string+=i
    return string

def contarVocales(palabra):
    string = ""
    for i in palabra:
        if i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
            i = chr(ord(i)+32)
            string+=i
        elif i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            string+=i
        elif i=='á' or i=='Á':
            string+='a'
        elif i=='é' or i=='É':
            string+='e'
        elif i=='í' or i=='Í':
            string+='i'
        elif i=='ó' or i=='Ó':
            string+='o'
        elif i=='ú' or i=='Ú':
            string+='u'
    return len(string)
         



def cantVocales(nomArch):
    lst_lineas = []
    lst_palabras = []
    lst_palabras_sin_repetir = []
    f = open(nomArch,"r")
    for linea in f.readlines():
        linea = linea[:-1]
        lst_lineas.append(linea.split(','))
    print(lst_lineas)
    
    for lst in lst_lineas:
        lst_palabras += lst
    print(lst_palabras)
    
    for palabra in lst_palabras:
        palabra = esPalabra(palabra)
        if palabra not in lst_palabras_sin_repetir:
            lst_palabras_sin_repetir.append(palabra)
    
    for palabra in lst_palabras_sin_repetir:
        print("{} --> {}".format(palabra,contarVocales(palabra)))
        
    
    
def main():
    cantVocales("palabras.csv")
    print(contarVocales("hola"))
    print(esPalabra("lapícérá"))
main()

            
    
    
    
    
    
    
    
    
    
    
    
    
    
    