"""
'''
def esPalabra(pal):
    palabra=''
    for l in pal:
        if (l>='a' and l<='z') or (l>='A' and l<='Z') or l in 'áéíóúñÁÉÍÓÚÑ' or l==' ':
            palabra+=l
    return palabra

def es_num(l):
    if l>=0 and l<=9:
        return True
    else:
        return False


def factura(ID_abonado):
    f = open('abonados.csv','r')
    todos = f.readlines()
    todos_nombres = []
    todos_domicilios = []
    todos_abonos = []
    for linea in todos:
        nombre = esPalabra(linea[1])
        todos_nombres.append(nombre)
    
    for linea in todos:
        domicilio = esPalabra(linea[2])
        todos_domicilios.append(domicilio)
'''
'''
#abrir cada archivo y guardar cada uno en un diccionario o en una lista (según conveniencia)
def cargarDicHabitantes():
    archHab = open('habitantes.txt','r')      '''ABRO EL ARCHIVO'''
    dicHab = {}                               '''CREO DICCIONARIO VACIO'''
    for linea in archHab.readlines():         '''RECORRO TODAS LAS LINEAS DEL ARCHIVO'''
        linea=linea[:-1]                      '''ELIMINO EL \n DEL FINAL DE CADA LINEA'''
                                               
        linea = linea.split(',')              '''DE STRING LO PASO A UNA LISTA '''
        if linea[0]!='':                      '''VERIFICO QUE HAYA ALGUN NUMERO'''
            
            linea[0] = int(linea[0])          '''CONVIERTO A CADA ELEMENTO EN SU TIPO DE DATO ORIGINAL (INT), (ANTES ESTABAN EN STR)'''
            
            linea[2] = int(linea[2])
            linea[3] = int(linea[3])
            dicHab[linea[0]]=[linea[1],linea[2],linea[3]]      '''GUARDO LOS ELEMENTOS EN UN DICCIONARIO'''
    archHab.close()
    return dicHab
'''
#CARGO COMO EL DICCIONARIO PERO A UNA LISTA
def cargarListaHabitantes():
    archHab = open('habitantes.txt','r')       '''ABRO EL ARCHIVO, LO LIMPIO DE AS \n'''
    listaHab=[]                                '''Y HAGO UNA LISTA DE TODAS LAS LINEAS (LISTA DE LISTAS)'''
    for linea in archHab.readlines():
        linea = linea[:-1]
        
        linea = linea.split(',')
        if linea[0]!='':
            linea[0] = int(linea[0])
            
            linea[2] = int(linea[2])
            linea[3] = int(linea[3])
            listaHab.append(linea)
    archHab.close()
    return listaHab

def cargarDicLocalidades():
    archLoc = open('localidades.txt','r')
    dic = {}
    for linea in archLoc.readlines():
        linea = linea[:-1]
        
        linea = linea.split(',')
        if linea[0]!='':
            linea[0] = int(linea[0])
            
            linea[2] = int(linea[2])
        dic[linea[0]] = [linea[1],linea[2]]
    archLoc.close()
    return dic

def cargarDicHabXLoc():
    archHabXLoc = open('habitantesXlocalidad.txt','r')
    dic = {}
    for linea in archHabXLoc.readlines():
        linea = linea[:-1]
        
        linea = linea.split(',')
        if linea[0]!='':
            linea[0] = int(linea[0])
            linea[1] = int(linea[1])
            
        dic[linea[1]]= linea[0]
    archHabXLoc.close()
    return dic
    
def imprimirDic(dic):
    for clave in dic:
        print(clave,':',dic[clave])

    
def cantHabitantes(loc,hijos):
    dicLoc = cargarDicLocalidades()             '''Carga el archivo 'localidades.txt' en un diccionario'''
    dicHabXLoc = cargarDicHabXLoc()             '''Carga el archivo 'habitantesXlocalidad.txt' en un diccionario '''
    listaHab = cargarListaHabitantes()          '''Cargo el archivo 'habitantes.txt' en una lista'''
    idLoc = -1                                  '''Inicializo la variable idLoc, para luego detectar si fue asignado '''
    
'''
BUSCO EL ID DE LA LOCALIDAD QUE PERTENECE AL NOMBRE DE LOCALIDAD PASADO POR PARAMETRO
HAY QIE ITERAR PORQUE EL DICCIONARIO TIENE COMO CLAVE EL ID Y NO EL NOMBRE
'''
    for clave in dicLoc:                 '''itero el diccionario localidad '''
        if dicLoc[clave][0]==loc:    
            idLoc = clave                '''asignar clave a una variable '''
            break
    
    if (idLoc!=-1):
        contHab = 0
        for hab in listaHab:
            estaenDic = dicHabXLoc.get(hab[0])
            
            if hab[2]==hijos and estaenDic and dicHabXLoc[hab[0]]==idLoc:
                contHab=contHab+1
    
    return contHab
'''
'''
def LstVentasTarjetas():
    f = open('ventastarjetas.csv','r')
    lst = []
    for linea in f.readlines():
        linea = linea[:-1]
        linea.split(',')
        if linea[0]!='':
            linea[0] = int(linea[0])
            linea[2] = int(linea[2])
        lst.append(linea[0],linea[1],linea[2])
    f.close()
    return lst

def LstVendedores():
    f = open('vendedores.csv','r')
    lst = []
    for linea in f.readlines():
        linea = linea[:-1]
        linea.split(',')
        if linea[0]!='':
            linea[0] = int(linea[0])
            linea[2] = int(linea[2])
            linea[3] = int(linea[3])
        lst.append(linea[0],linea[1],linea[2],linea[3])
    f.close()
    return lst

def cargarListaComisiones():
    archComi = open('liquidaciones.txt','r')
    lisComi = []
    for linea in archComi.readlines():
        linea = linea[:-1]
        linea = linea.split(',')
        
        linea[0] = int(linea[0])
        linea[1] = float(linea[1])
        lisComi.append(linea[0],linea[1])
    archComi.close()
    return lisComi

def imprimirLista(lista):
    for linea in lista:
        print(linea)
    
def comision(cantidad_tarjetas,objetivo_tarjetas):
    porcentaje_objetivo_minimo = 0.8
    porcentaje_mayor_al_100 = 0.1
    porcentaje_mayor_al_80 = 0.03
    comisionMin = 0
    
    if cantidad_tarjetas<(objetivo_tarjetas*porcentaje_objetivo_minimo):
        valorComision = comisionMin

    elif (objetivo_tarjetas*porcentaje_objetivo_minimo <= cantidad_tarjetas*objetivo_tarjetas):
        valorComision = sueldo*porcentaje_mayor_al_80
    else:
        valorComision = sueldo*porcentaje_mayor_al_100
        
    return valorComision


def liquidar():
    vendedores = LstVendedores()
    venta_tarjetas = LstVentasTarjetas
    f = open('liquidacioncomisiones.txt','w')
    cantidad_vendedores = len(vendedores)
    cantidad_venta_tarjetas = len(venta_tarjetas)
    
    for vendedor in cantidad_vendedores:
        total_tarjetas=0
        for ventaTar in venta_tarjetas:
            if (vendedor[0]==ventaTar[0]):
                total_tarjetas+=ventaTar[2]
            com = comision(total_tarjetas,ven[2],ven[3])
            com = round(com,2)
            f.write(str(ven[0])+','+str(com)+'\n')
            
def ordenarLst(lst,c):
    for i in range(0,len(lst)):
        for j in range(i+1,len(lst)):
            if lst[j][c]>lst[i][c]:
                lst[i],lst[j] = lst[j],lst[i]
    return lst

def topcinco():
    vendedores = LstVendedores()
    comision = comision()
    cantidad = 5
    comision = ordenarLst(comision,1)
    print ("{0:10}{1:10}\n".format("codVen","Comision"))               # Imprimir la cabecera de la tabla de salida
    for i in range(0,cantidad):
        print ("{0:<10}{1:<10}\n".format(lisComi[i][0],lisComi[i][1]))
    
    
    
    

def liquidar():
    # calcula la comisión por cada vendedor y escribe en el archivo liquidacionComisiones.txt
    # el id del vendedor y su correspondiente comisión
    lisVen = cargarListavendedores()       # Cargar el archivo "vendedores.txt" en una lista lisVen
    lisVenTar = cargarListaVentasTarjetas()# Cargar el archivo "ventasTarjetas.txt" en una lista lisVenTar

    archLiqComi = open("liquidacionComisiones.txt","w")  # abrir archivo
    tamVen=len(lisVen)                     # Cantidad de elementos de la lista de vendedores
    tamVenTar=len(lisVenTar)               # Cantidad de elementos de la lista de VentasTarjetas
    for ven in lisVen:                     # iterar la lista de vendedores y guardar cada registro de vendedor en la variable ven
        totTar=0                           # inicializar el total por tarjeta
        for venTar in lisVenTar:           # iterar la lista de VentasTarjetas y guardar cada registro de venta por tarjeta en la variable venTar
            if (ven[0]==venTar[0]):        # comparar si son los mismos codigos de vendedores
                totTar=totTar+venTar[2]    # acumular los totales de tarjetas
        com=comision(totTar,ven[2],ven[3]) # calcular la comisión
        com=round(com, 2)                  # redondeo a dos decimales para no escribir "muchos" decimales en el archivo
        archLiqComi.write(str(ven[0])+","+str(com)+"\n") # escribir en el archivo "liquidacionComisiones.txt" el código del vendedor y el valor de la comisión

def topcinco():
    # obtiene los cinco vendedores que tengan la mayor comision
    # Para ello se ordena la lista y se imprimen los cinco primeros
    lisVen = cargarListavendedores() # Cargar el archivo "vendedores.txt" en una lista lisVen
    lisComi= cargarListaComisiones() # Cargar el archivo "liquidacionComisiones.txt" en una lista lisComi
    cantidad=5                       # cantidad de registros que se necesitan leer e imprimir "de la lista ordenada"

    lisComi=ordenarLista(lisComi,1)  # ordenar la lista lsiComi por el campo 1

    print ("{0:10}{1:10}\n".format("codVen","Comision"))               # Imprimir la cabecera de la tabla de salida
    for i in range(0,cantidad):
        print ("{0:<10}{1:<10}\n".format(lisComi[i][0],lisComi[i][1])) # Imprimir los daots de la lista

def ordenarLista(lista, c):
    # lista: es la lista que se va a ordenar
    # c: es el número de "campo" por el cual se va a ordenar
    for i in range(0, len(lista)):
        for j in range(i+1, len(lista)):
            if lista[j][c] > lista[i][c]: # >: ordena descendente  , <: ordena ascendente
                lista[i] , lista[j] = lista[j] , lista[i]
    return lista

def main():
    #--------- INICIO PROGRAMA PRINCIPAL ----------#

    liquidar()     # Se crea el archivo "liquidacionComisiones.txt" con las comisiones por codigo de vendedor

    topcinco()     # Imprime los primero cinco (codVen y comisión) cuya comisiones sean las mayores

"""    
'''
def dicHabitantes():
    f = open('habitantes.csv','r')
    dic = {}
    for linea in f.readlines():
        linea = linea[:-1]
        linea = linea.split(',')
        
        if linea[0]!='':
            linea[0]=int(linea[0])
            linea[2]=int(linea[2])
            linea[3]=int(linea[3])
        dic[linea[0]] = [linea[1],linea[2],linea[3]]
    f.close()
    return dic
def lstHabitantes():
    lista_habitantes = []
    archivoHabitantes = open("habitantes.csv","r")
    for linea in archivoHabitantes.readlines():
        linea = linea[:-1]
        linea = linea.split(",")
        linea[0] = int(linea[0])
        linea[2] = int(linea[2])
        linea[3] = int(linea[3])
        lista_habitantes.append(linea)
    archivoHabitantes.close()
    return lista_habitantes

def dicLocalidades():
    f = open('localidades.csv','r')
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

def dichabitantesXlocalidad():
    f = open('habitantesXlocalidad.csv','r')
    dic = {}
    for linea in f.readlines():
        linea = linea[:-1]
        linea = linea.split(',')
        if linea[0]!='':
            linea[0] = int(linea[0])
            linea[1] = int(linea[1])
        dic[linea[0]] = [linea[1]]
    f.close()
    return dic

def imprimirDic(dic):
    for clave in dic:
        print(clave,':', dic[clave])
        
        
def cantHabitantes(nombreLocalidad,hijos):
    dicLoc = dicLocalidades()
    dicHabxLoc = dichabitantesXlocalidad()
    lst_hab = lstHabitantes()
    
    idLoc = -1
    listafinal = []
    claves = list(dicLoc.keys())
    i = 0
    while i<=len(claves) and idLoc==-1:
        if dicLoc[claves[i]][0]==nombreLocalidad:
            idLoc = claves[i]
        i+=1
    if idLoc!=-1:
        for habitante in lst_hab:
            valorLoc = dicHabxLoc.get(habitante[0])
            
            if habitante[2]==hijos and valorLoc ==idLoc:
                listafinal.append((habitante[0],habitante[1]))
    return listafinal
        



def edadXlocalidad():
    dicHabXLoc = dichabitantesXlocalidad()
    dicLoc = dicLocalidades()
    dicHab = dicHabitantes()
    dic_edad_x_loc = {}
    for claveLoc in dicLoc:
        edad = 0
        cant = 0
        for claveHab in dicHabXLoc:
            if dicHabXLoc[claveHab] == claveLoc:
                edad = edad+dicHab[claveHab][2]
                cant+=1
            if cant>0:
                dic_edad_x_loc[claveHab]= edad/cant
                    
    imprimirDicOrdenado(dic_edad_x_loc)
                
        
        
    
    
def imprimirDicOrdenado(dic):
    claves = list(dic.keys())
    ordenarLista(claves)
    print('{0:15}{1:15}\n',format('ID Localidad','Promedio Edad'))
    for clave in claves:
        print('{0:<15}{1:<15}\n'.format(clave,dic[clave]))
            
def ordenarLista(lst):
    for i in range(0,len(lst)-1):
        for j in range(i,len(lst)):
            if lst[i]>lst[j]:
                lst[i],lst[j] = lst[j],lst[i]
    

    
    
def main():
    localidad = 'Lujan'
    hijos = 3
    lstHabHijos = cantHabitantes(localidad,hijos)
    print('Lista de habitantes que tienen {0} hijos en {1}:\n{2}\n'.format(hijos,localidad,lstHabHijos))
    edadXlocalidad()
    
main()
''' 

'''

'''
'''
def abonados():
    f = open('abonados.csv','r')
    dic = {}
    for linea in f:
        linea = linea.split(',')
        dic[int(linea[0])] = [linea[1],linea[2],int(linea[3])]
    f.close()
    return dic


def categorias():
    f = open('categorias.csv','r')
    dic = {}
    for linea in f:
        linea = linea.split(',')
        dic[int(linea[0])] = [float(linea[1]),float(linea[2])]
    f.close()
    return dic


def conexiones():
    f = open('conexiones.csv','r')
    lst = []
    for linea in f.readlines():
        linea = linea[:-1]
        linea = linea.split(',')
        linea[0] = int(linea[0])
        linea[1] = int(linea[1])
        lst.append(linea)
    f.close()
    return lst



def factura(ID_abonados):
    abonado = abonados()
    categoria = categorias()
    conexion = conexiones()
    lista_categoria = list(categoria.keys())
    abono_telefonico_movil = 0
    cont=0
    for clave in abonado:
        if ID_abonados == int(clave):
            nombre = abonado[clave][0]
            domicilio = abonado[clave][1]
        ID_categoria = abonado[clave][2]
        if ID_categoria == int(lista_categoria[0]):
            abono_telefonico_movil = categoria[clave][0]
            
    for sublista in conexion:
        ID_categoria = abonado[ID_abonados][2]
        if ID_abonados == sublista[0]:
            cont+=sublista[1]
  
    importe = cont*categoria[ID_categoria][1]
    print('Nombre: ',nombre)
    print('Domicilio: ',domicilio)
    print('Abono: ',abono_telefonico_movil)
    print('Importe: ',importe)
''' 
'''
def duracionMaxima():
    abonado = abonados()
    categoria = categorias()
    conexion = conexiones()
    mayor = 0
    nombre=''
    ID_categoria=''
    repetido = []
    llaves = list(abonado.keys())
#    nombres = list(abonado.get())
    for n in range(0,len(conexion)):
        if conexion[n][0] not in repetido:
            minutos = 0
            repetido.append(conexion[n][0])
        for p in range(0,len(conexion)):
            if conexion[p][0]==conexion[n][0]:
                minutos += int(conexion[n][1])
    
        if minutos>mayor:
            mayor = minutos
            ID_abonado = conexion[n][0]
    
    for p in range(0,len(abonado)):
        if llaves[p]==ID_abonado:
            nombre = abonado[llaves[p]][0]
            ID_categoria = abonado[llaves[p]][2]
    print('ID_abonado: {}\nNombre: {}\nID_categoria: {}\nDuracion Total de minutos: {}\n'.format(ID_abonado,nombre,ID_categoria,mayor))
'''
'''
def duracionMaxima():
    dicCat = categorias()
    dicAbonados = abonados()
    listaConex = conexiones()
    maxi = 0 ; primera = True ; suma_min = 0

    repetido = []
    mayor = 0
    for k in range(0,len(listaConex)):
        if listaConex[k][0] not in repetido:
            minutos = 0
            repetido.append(listaConex[k][0])
            for h in range(0,len(listaConex)):
                if listaConex[h][0]==listaConex[k][0]:
                    minutos+=int(listaConex[h][1])
            if minutos>mayor:
                mayor = minutos
                ID_abonado = listaConex[k][0]


    print("ID_abonado: {}\n Nombre: {}\n Categoria: {}\n Duracion total en minutos: {}".format(ID_abonado,dicAbonados[ID_abonado][0],dicAbonados[ID_abonado][2],mayor))

    


def main():
    dicAbonados = abonados()
    IDS = list(dicAbonados.keys())

    ID_abonado = int(input("Ingrese ID de abonado: <<({})>>: ".format(IDS)))
    factura(ID_abonado)
    duracionMaxima()
main()
'''

def buscarS(xs,s):
    ini = -1
    fin = -1
    i = 0
    bandera = False
    while i<len(xs):
        if bandera==False and xs[i:i+len(s)]==s:
            ini = len(xs[0:i])
            fin = len(xs[0:i+len(s)-1])
            bandera = True
        i+=1
    return (ini,fin)

def listaIndice(xs,s):
    lst = []
    ini = -1
    fin = -1
    i = 0
    bandera = False
    while i<len(xs)-len(s):
        h = buscarS(xs,s)
        if (h!=(0,0) and h!=(-1,-1)) and bandera==False:
            n1 = h[0]
            n2 = h[1]
            n = n1,n2
            lst.append(n)
            bandera=True
            resto=h[0]
        elif (h!=(0,0) and h!=(-1,-1)) and bandera==True:
            n1 = h[0]+resto
            n2 = h[1]+resto
            n = n1,n2
            lst.append(n)
            resto+=h[0]
        xs = xs[h[0]+1:]
        i+=1
    return lst

def main():
    ind = input('Ingrese string a buscar: ')
    arch_texto = open('archivo_de_strings.txt','r')
    linea_texto = arch_texto.readline()
    h = buscarS(linea_texto,ind)
    print('Se encuentra en: ',h)
    m = listaIndice(linea_texto,ind)
    print(m)
    arch_texto.close()
main()

'''
#xs = La verdad absoluta no existe, y esto es absolutamente cierto
#s = d ab
def buscarS(xs,s):
    ini = -1
    fin = -1
    i=0
    bandera = False
    while i<len(xs) and bandera==False:
        if xs[i:i+len(s)]==s:
            ini = len(xs[0:i])
            fin = len(xs[0:i+len(s)-1])
            bandera=True
        i+=1
    return (ini,fin)

def listaIndice(xs,s):
    lst = []
    for i in range(len(xs)):
        if s==xs[i:i+len(s)]:
            tupla = (i,i+len(s)-1)
            lst.append(tupla)
    return lst
    
    
def main():
    s = input('Ingrese string a buscar: ')
    f = open('archivo_de_strings.txt','r')
    xs = ''
    for line in f:
        xs+=line
    f.close()
    print(buscarS(xs,s))
    print(listaIndice(xs,s))
main()
''' 
'''        
def fa(a):
    return fb(a)+1
def fb(b):
    for i in range(0, len(b)):
        return int("".join(b))+i
a=['1','2']
print ("{0:d}{1:d}".format(fb(a),fa(a)))
'''     
            