'''
#PRAC7 EJER1
def informe(archivo):
    f = open(archivo,'r')
    lst=[]
    val_max=0
    val_min=0
    suma=0
    contlineas=0
    lineas=f.readlines()
    primera=True
    for i in range(len(lineas)):
        lineas[i]=int(lineas[i])
        contlineas+=1
        
    for i in range(len(lineas)):
        if primera==True:
            val_min=lineas[i]
            val_max=lineas[i]
            primera=False
        if lineas[i]<val_min:
                val_min=lineas[i]
        if lineas[i]>val_max:
                val_max=lineas[i]
        suma+=lineas[i]
    promedio = suma/contlineas
    lst.append(val_max)
    lst.append(val_min)
    lst.append(promedio)
    lst.append(contlineas)
    return lst
            

def main():
    print(informe('notaejer1.txt'))
main()
'''
'''
#PRAC7 EJER2
def agregarMedia(archivo):
    f = open(archivo,"r")
    lst=f.readlines()
    lista_prom=[]
    f.seek(0)
    for linea in f:
        lista_lineas=linea.split(',')
        cont=0
        suma=0
        for num in lista_lineas:
            suma+=int(num)
            cont+=1
        promedio = str(suma/cont) + '\n'
        lista_prom = lista_prom+[promedio]
    f.close()
    
    f = open(archivo,'w')
    for i in range(len(lst)):
        f.write(str(lst[i]))
        f.write(str(lista_prom[i]))
    f.close()
     
    
def main():
    agregarMedia("ejer2.csv")
main()
'''
'''
#PRAC7 EJER4
def esPalabra(pal):
    palabra=''
    for l in pal:
        if (l>='a' and l<='z') or (l>='A' and l<='Z') or (l in 'áéíóúÁÉÍÓÚñÑ'):
            palabra+=l
    return palabra

def cabecera(arch,cant,pmin,pmax):
    lst=[]
    f = open(arch,'r')
    for linea in f:
        lst = linea.split()
    lista_limpia = []
    for caracter in lst:
        caracter = esPalabra(caracter)
        lista_limpia.append(caracter)
    i=0
    impresos=0
    while i<len(lista_limpia) and impresos<cant:
        if len(lista_limpia[i])>=pmin and len(lista_limpia[i])<=pmax:
            print(lista_limpia[i])
            impresos+=1
        i+=1
    f.close()
    
def main():
    archivo = 'ejer4.txt'
    cantidad = int(input('Ingrese cantidad: '))
    pmin = int(input('Ingrese valor minimo: '))
    pmax = int(input('Ingrese valor maximo: '))
    cabecera(archivo,cantidad,pmin,pmax)
main()
'''
'''
#PRAC7 EJER5
def esPalabra(pal):
    palabra=''
    for l in pal:
        if (l>='a' and l<='z') or (l>='A' and l<='Z') or l in 'áéíóúÁÉÍÓÚñÑ':
            palabra+=l
    return palabra


def cabecera2(arch,cant,pmin,pmax):
    lst=[]
    f = open(arch,'r')
#   Separo cada linea
    for linea in f:
        lst = linea.split()
    lista_limpia = []
#   Verifico que sean palabras y las guardo en la lista limpia
    for caracter in lst:
        caracter = esPalabra(caracter)
        lista_limpia.append(caracter)
    i=0
    impresos=0
    lst_final=[]
#   Verifico e imprimo las palabras que cumplan con las dos condiciones
    while i<len(lista_limpia) and impresos<cant:
        if len(lista_limpia[i])>=pmin and len(lista_limpia[i])<=pmax:
            print(lista_limpia[i])
            lst_final.append(lista_limpia[i])
            impresos+=1
        i+=1
    f.close()
    
    f = open('resultado.csv','w')
    sin_repetir = []
    for pal in lst_final:
        if pal not in sin_repetir:
            sin_repetir+=pal
            string = str(pal)+'\n'
            f.write(string)
            
    f.close()
    
    
def main():
    archivo = 'ejer4.txt'
    cantidad = int(input('Ingrese cantidad de palabras: '))
    pmin = int(input('Ingrese cantidad minima de letras a buscar: '))
    pmax = int(input('Ingrese cantidad maxima de letras a buscar: '))
    cabecera2(archivo,cantidad,pmin,pmax)
main()
'''
'''
#PRAC7 EJER6
import random

def esPalabra(pal):
    palabra=''
    for l in pal:
        if (l>='a' and l<='z') or (l>='A' and l<='Z') or l in 'áéíóúÁÉÍÓÚñÑ':
            palabra+=l
    return palabra

def generadora(ori,dest,cant):
    f = open(ori,'r')
    listado_de_palabras = f.readlines()
    lista_limpia=[]
#   listado_de_palabras = ['pija\n','verga\n',etc]
#   LIMPIO LA LISTA DE LOS \n
    for palabra in listado_de_palabras:
        palabra=esPalabra(palabra)
        lista_limpia.append(palabra)
#   lista_limpia = ['pija','verga',etc]
    lista_aleatoria=[]
    for i in range(len(lista_limpia)):
        aleatorio = random.randint(0,len(lista_limpia)-1)
        lista_aleatoria.append(lista_limpia[aleatorio])
        lista_limpia.remove(lista_aleatoria[i])
        
    print(lista_aleatoria)
    f.close()
    
    f = open(dest,'w')
    for i in range(cant):
        limpio = esPalabra(lista_aleatoria[i])+'\n'
        f.write(limpio)
    
    f.close()
        
    
def main():
    origen = 'origenejer6.txt'
    destino = 'destinoejer6.txt'
    cantidad = int(input('Ingrese una cantidad: '))
    generadora(origen,destino,cantidad)
main()
'''
'''
#PRAC7 EJER7
def diccionario():
    dic = {}
    f = open('persona.csv','r')
    for line in f:
        lst = line.split(',')
        dic[int(lst[2])] = [lst[0],lst[1]]
    f.close()
    return dic


def menu():
    print('1.AGREGAR REGISTRO \n2.ELIMINAR REGISTRO \n3.BUSCAR REGISTRO \n4.ORDENAR ARCHIVO POR \n5.MOSTRAR ARCHIVO \n6.SALIR')
    opcion = int(input('Ingrese el valor de la opcion: '))
    return opcion

def agregarRegistro(archivo):
    dic = {}
    seguir = 'si'
    while seguir == 'si':
        nombre = str(input('Ingrese nombre: '))
        apellido = str(input('Ingrese apellido: '))
        dni = int(input('Ingrese DNI: '))
        while dni in dic:
            dni = int(input('ERROR. DNI repetido. Ingrese otro: '))
        dic[dni] = [nombre,apellido]
        f = open(archivo,'a')
        string = nombre+','+apellido+','+dni+'\n'
        f.write(string)
        f.close()
        seguir = str(input('Seguir agregando al registro? (si/no)'))

def eliminarRegistro(archivo):
    f = open(archivo,'r')
    dni = int(input('Ingrese DNI a eliminar: '))
    string=''
    for line in f:
        lst = line.split(',')
        if dni == int(lst[2]):
            string+=''
        else:
            string+=line
    f.close()
    f = open(archivo,'w')
    f.write(string)
    f.close()
    
        
def buscarRegistro(archivo):
    f = open(archivo,'r')
    dic = diccionario()
    op = int(input('Ingrese 1 para buscar por DNI o 2 para buscar por apellido: '))
    claves = dic.keys()
    if op==1:
        dni = int(input('Ingrese DNI: '))
        if dni in claves:
            string = str(dic[dni][0])+','+str(dic[dni][1])
            print(string)
        else:
            dni = int(input('El DNI ingresado no está ingresado, ingrese otro: '))
    elif op==2:
        apellido = str(input('Ingrese el apellido: '))
        for i in claves:
            if apellido in dic[i]:
                string = str(i)+','+dic[i][0]
                print(string)
    f.close()
    
def ArchivoPor(archivo):
    opcion = int(input('Ingrese opcion (1 a 3): '))
    f = open(archivo,'r')
    dic = diccionario()
    
    
    

def main():
    op = menu()
    archivo = 'personas.csv'
    while op!=6:
        if op ==1:
            agregarRegistro(archivo)
        elif op == 2:
            eliminarRegistro(archivo)
        elif op == 3:
            buscarRegistro(archivo)
        elif op == 4:
            ordenarArchivoPor(archivo)
        elif op == 5:
            mostrarArchivo(archivo)
        op = menu()
main()
'''
'''
def cargarDicProvincias():
    f = open('provincias.csv','r')
    dic = {}
    for linea in f.readlines():
        linea = linea[:-1]
        linea = linea.split(',')
        
        if linea[0]!='':
            linea[0]=int(linea[0])
            linea[2]=int(linea[2])
        dic[linea[0]]=[linea[1],linea[2]]
    f.close()
    return dic
        
def cargarLocalidades():
    f = open('localidades8.csv','r')
    dic = {}
    for linea in f.readlines():
        linea = linea[:-1]
        linea = linea.split(',')
        if linea[0]!='':
            linea[0] = int(linea[0])
            linea[2] = int(linea[2])
            linea[3] = int(linea[3])
            linea[4] = int(linea[4])
        dic[linea[0]] = [linea[1],linea[2],linea[3],linea[4]]
    f.close()
    return dic
    
def cargarPaises():
    f = open('paises.txt.csv','r')
    dic = {}
    for linea in f.readlines():
        linea = linea[:-1]
        linea = linea.split(',')
        if linea[0]!='':
            
            linea[0] = int(linea[0])
            linea[2] = int(linea[2])
        dic[linea[0]] = [linea[1],linea[2]]
    f.close()
    return dic
   
def poblacion(ID_provincia):
    dic_provincias = cargarDicProvincias()
    provincia = ''
    for i in dic_provincias:
        if i == ID_provincia:
            provincia = dic_provincias[i][0]
    
    dicloc = cargarLocalidades()
    habitantes = 0
    for i in dicloc:
        if dicloc[i][1]==ID_provincia:
            habitantes+=dicloc[i][3]
    if len(provincia)==0:
        print('NADA DE DATOS GATO')
    else:
        print('{}: {} Habitantes'.format(provincia,habitantes))


def localidadMaxima():
    dic_localidades = cargarLocalidades()
    primero = True
    for i in dic_localidades:
        if primero==True:
            max_poblacion = dic_localidades[i][3]
            max_localidad = dic_localidades[i][0]
            ID_provincia = dic_localidades[i][1]
            primero = False
        else:
            if dic_localidades[i][3]>max_poblacion:
                max_poblacion = dic_localidades[i][3]
                max_localidad = dic_localidades[i][0]
                ID_provincia = dic_localidades[i][1]    
                
    dic_provincias=cargarDicProvincias()            
    for i in dic_provincias:
        if i==ID_provincia:
            provincia = dic_provincias[i][0]
            ID_pais = dic_provincias[i][1]

    dic_paises = cargarPaises()
    for i in dic_paises:
        if i==ID_pais:
            pais = dic_paises[i][0]
        
    print('Población: {}\nLocalidad: {}\nProvincia: {}\nPaís: {}\n'.format(max_poblacion,max_localidad,provincia,pais))



def main():
    ID_provincia = int(input('Ingrese el ID de la provincia: '))
    poblacion(ID_provincia)
    localidadMaxima()
main()
'''

