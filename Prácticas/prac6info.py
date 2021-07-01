'''
#PRAC6 EJER 1
#1.1
def estaEnLista(n,lst):
    if n in lst:
        return True
    else:
        return False
'''
'''
#1.2
def estaEnLista(n,lst):
    numero = str(n)
    retornar = False
    for i in range(0,len(lst)):
        if lst[i]==n:
            retornar=True
        else:
            i+=1
            
    return retornar
'''
'''
#1.3
def estaEnLista(n,lst):
    i=0
    retornar = False
    while i<len(lst):
        if lst[i]==n:
            retornar=True
        i+=1
    return retornar
'''
'''
#PRAC6 EJER2
def cargarLista(n):
    lista = []
    while n!=0:
        while n<0:
            n = int(input('Error. Numero NO positivo. \n'))
        while n in lista:
            n = int(input('Error. Numero repetido. \n'))
        lista.append(n)
        n = int(input())
                
    print('La lista contiene: \n',lista)
                
        
def main():
    lista = int(input('Ingrese lista: '))
    cargarLista(lista)
main()
'''
'''
#PRAC6 EJER3
def presentarMenu():
    opcion=0
    conjuntoA=[]
    conjuntoB=[]
    while opcion!=6:
        opcion=0
        print('1. CARGAR CONJUNTOS')
        print('2. UNION')
        print('3. INTERSECCION')
        print('4. DIFERENCIA (A-B)')
        print('5. DIFERENCIA SIMÉTRICA')
        print('6. SALIR')
        opcion=int(input('Ingrese el valor de la opcion: '))
        while opcion<1 or opcion>6:
            opcion=int(input('Valor incorrecto. Ingrese otro numero: '))
    
        callFunction(opcion,conjuntoA,conjuntoB)
    if opcion==6:
        print('GRACIAS POR PARTICIPAR')
    
def cargarConjuntos(lA,lB):
    xclear(lA)
    xclear(lB)
    print("\nPara cargar lista 'A': ")
    cargarLista(lA)
    print("\nPara cargar lista 'B': ")
    cargarLista(lB)
    print('Conjunto A = {}'.format(lA))
    print('Conjunto B = {}'.format(lB))
    print()
    
def union(lA,lB):
    resunion = []
    igualarLista(resunion,lA)
    print(lA)
    for b in lB:
        if not (b in resunion):
            resunion.append(b)
    print(lA)
    print('\nUnion entre {} y {}: \n{}\n'.format(lA,lB,resunion))
    
def interseccion(lA,lB):
    resintersec = []
    for b in lB:
        for a in lA:
            if b==a:
                resintersec.append(b)
    print('\nInterseccion entre {} y {}: \n{}\n'.format(lA,lB,resintersec))
    
def diferencia(lA,lB):
    resdif=[]
    igualarLista(resdif,lA)
    for b in lB:
        for a in lA:
            if b==a:
                resdif.remove(b)
    print('\nDiferencia entre {} y {}: \n{}\n'.format(lA,lB,resdif))
    
def diferenciaSimetrica(lA,lB):
    resdifsim=[]
    igualarLista(resdifsim,lA)
    for b in lB:
        if not (b in resdifsim):
            resdifsim.append(b)
    for b in lB:
        for a in lA:
            if b==a:
                resdifsim.remove(b)
    print('\nDiferencia simetrica entre {} y {}: \n{}\n'.format(lA,lB,resdifsim))
    
def xclear(lst):
    i=0
    while i<len(lst):
        lst.pop(i)
        
def cargarLista(lista):
    numero = int(input('Ingresar numeros o 0 (cero) para salir\n'))
    while numero!=0:
        validar(numero,lista)
        numero = int(input())
        
def validar(numero,lista):
    res = False
    while res==False:
        if estaEnLista(numero,lista):
            res = False
            numero = int(input('Error, numero repetido.\n'))
        elif numero<0:
            numero = int(input('Error, numero NO positivo:.\n'))
            res = False
        else:
            res = True
            lista.append(numero)
        
def igualarLista(listaCero,listaValor):
    for a in listaValor:
        listaCero.append(a)
        
def estaEnLista(num,lst):
    res=False
    if num in lst:
        res = True
    return res

def callFunction(n,a,b):
    if n==1:
        cargarConjuntos(a,b)
    elif n==2:
        union(a,b)
    elif n==3:
        interseccion(a,b)
    elif n==4:
        diferencia(a,b)
    elif n==5:
        diferenciaSimetrica(a,b)
        
def main():
    presentarMenu()
main()
'''
'''
#PRAC6 EJER4
import random

def cargarListaAleat(inicio,fin,cantidad):
    lst = []
    if inicio>fin:
        for cantVeces in range(1,cantidad+1):
            lst.append(random.randint(fin,inicio))
    else:
        for cantVeces in range(1,cantidad+1):
            lst.append(random.randint(inicio,fin))
            
    if inicio==fin:
        for cantVeces in range(1,cantidad+1):
            lst.append(random.randint(fin,inicio))
    print(lst)
    
    maxValor = lst[0]
    for numero in lst:
        if maxValor>numero:
            maxValor=maxValor
            
        else:
            maxValor = numero
    minValor =lst[0]
    
    for numero in lst:
        if minValor<numero:
            minValor=minValor
        else:
            minValor=numero
    print('El maximo valor es: {} y el minimo valor es {}'.format(maxValor,minValor))
def main():
    a = int(input('Ingrese inicio: '))
    b = int(input('Ingrese final: '))
    c = int(input('Ingrese cantidad: '))
    cargarListaAleat(a,b,c)
main()
'''
'''
#PRAC6 EJER5
import random
def estaEnLista(n,lst):
    i=0
    retornar = False
    while i<len(lst):
        if lst[i]==n:
            retornar=True
        i+=1
    return retornar

def cambiaLista(lst,a,b):
    cont=0
    for n in lst:
        if n<a or n>b:
            lst.remove(n)
            aleatorio = random.randint(a,b)
            lst.insert(cont,aleatorio)
        cont+=1
    return lst

def main():
    print('Cargue una lista: ')
    print('ingrese numeros (terminar con 0): ')
    lst=[]
    num = 1
    while num!=0:
        num = int(input())
        if num>0 and not estaEnLista(num,lst):
            lst.append(num)
        while num<0:
            num = int(input('ERROR, numero negativo: '))
            if num>0:
                lst.append(num)
    print('Lista Generada: ',lst)
    a = int(input('Ingrese limite a del rango: '))
    b = int(input('Ingrese limite b del rango: '))
    print('La lista modificada es: ')
    print(cambiaLista(lst,a,b))    
main()
'''
'''
#PRAC6 EJER6
def ordenarLst(lst):
    for i in range(0,len(lst)-1):
        for j in range(i+1,len(lst)):
            if lst[i]>lst[j]:
                aux = lst[i]
                lst[i]=lst[j]
                lst[j]=aux
    return lst
                
    
def main():
    print('Cargue una lista: ')
    lst=[]
    n = int(input('Ingrese numeros (terminar con 0): '))
    while n!=0:
        while n<0:
            n = int(input('ERROR. Ingrese numero positivo: '))
        while n>0:
            lst.append(n)
            n = int(input())
    print('\nLa lista cargada es: ')
    print(lst)
    
    print('\nLa lista ordenada es: ')
    print(ordenarLst(lst))
main()
'''
'''
#PRAC6 EJER7
def insertOrd(lst,num):
    bandera = True
    if num<lst[0]:
        lst.insert(0,num)
    for i in range(0,len(lst)-1):
        for j in range(i+1,len(lst)):
            if num>lst[i] and num<lst[j] and bandera==True:
                lst.insert(j,num)
                bandera=False
    if num>lst[len(lst)-1]:
        lst.append(num)
    
    return lst
    
def main():
    print('Cargue una lista: ')
    lst=[]
    n = int(input('Ingrese numeros (terminar con 0): '))
    while n!=0:
        while n<0:
            n = int(input('ERROR. Ingrese numero positivo: '))
        while n>0:
            lst.append(n)
            n = int(input())
    print('\nLa lista cargada es: ')
    print(lst)
    num = int(input('Ingrese valor a insertar: '))
    print('\nLa lista con la insercion ordenada es: ')
    print(insertOrd(lst,num))
main()
'''
'''
#PRAC6 EJER8
def inserOrd(num,lst):
    i = 0
    largo = len(lst)
    bandera=True
    while i<largo and bandera==True:
        if largo==1:
            if num<=lst[i]:
                lst.insert(0,num)
            if num>lst[i]:
                lst.append(num)
                
        else:
            if i<(largo-1):
                if num>=lst[i] and num<=lst[i+1]:
                    lst.insert(i+1,num)
                    bandera=False
                elif num<=lst[i]:
                    lst.insert(i,num)
                    bandera=False
            elif i==(largo-1):
                if num>=lst[i]:
                    lst.append(num)
                    bandera=False
        i+=1
    return lst
    
def main():
    print('CARGUEMOS UNA LISTA:')
    n = int(input('Ingrese numeros (terminar con 0): '))
    lista=[]
    bandera = True
    if n==0:
        print('LISTA VACIA')
    while n!=0:
        while n<0:
            n = int(input('ERROR, Numero Negativo: '))
        if bandera==True:
            lista.append(n)
            bandera=False
        else:
            lst=inserOrd(n,lista)
        n = int(input())
    print(lista)
main()
'''
'''
#PRAC6 EJER9 MENOR A 3
def ordernarAluXDNI(lista):
    for recorrido in range(len(lista)):
        for posicion in range(len(lista)-1):
            if lista[posicion][0]<lista[posicion+1][0]:
                temporal=lista[posicion]
                lista[posicion]=lista[posicion+1]
                lista[posicion+1]=temporal
    return lista

def cargarLstAlu():
    alumnos=0
    cont=1
    lista=[]
    while alumnos<3:
        dni=int(input("Ingrese el DNI del {}° alumno: " .format(cont)))
        nombre=input("Ingrese nombre del {}° alumno: " .format(cont))
        edad=int(input("Ingrese la edad del {}° alumno: " .format(cont)))
        datos=[dni,nombre,edad]
        lista.insert(alumnos,datos)
        alumnos+=1
        cont+=1
    return lista

def main():
    lista=cargarLstAlu()
    print(lista)
    r=ordernarAluXDNI(lista)
    print(r)
main()

'''
'''
#PRAC6 EJER9
#LISTA DE LISTAS

def ordenarAluXDNI(lista):
    for recorrido in range(len(lista)):
        for posicion in range(len(lista)-1):
            if lista[posicion][0]<lista[posicion+1][0]:
                temporal=lista[posicion]
                lista[posicion]=lista[posicion+1]
                lista[posicion+1]=temporal
    return lista

   


def cargarLstAlu():
    lista=[]
    lstgrande = []
    opcion = int(input('PULSE 1 PARA CARGAR, 0 PARA SALIR: '))
    if opcion==0:
        print('No se ingresaron datos')
    while opcion!=0 and opcion!=1:
        opcion= int(input('ERROR. Opcion no valida: '))
        lstgrande.append(lista)
    while opcion!=0 and opcion==1:
        dni = int(input('Ingrese DNI: '))
        nombre = str(input('Ingrese nombre: '))
        edad = int(input('Ingrese edad: '))
        lista.append(dni)
        lista.append(nombre)
        lista.append(edad)
        opcion = int(input('Seguir? : '))
        lstgrande.append(lista)
        lista=[]    
     
    return lstgrande

def main():
    l =(cargarLstAlu())
    print(l)
    print(ordenarAluXDNI(l))
main()
'''
'''
#PRAC6 EJER10
import random

def atributoTriple(lista):
    cont=0
    conttriples=0
#    for recorrido in range(len(lista)):
    for posicion in range(len(lista)-2):
        cont=0
        if lista[posicion]==lista[posicion+1]:
            cont+=1
            if lista[posicion+1]==lista[posicion+2]:
                cont+=1
                if cont==2:
                    conttriples+=1
                   
                        
    if conttriples==0:
        msj = 'NADA'
    elif conttriples==1:
        msj='Un Triple'
    elif conttriples==2:
        msj = 'Dos Triples'
    elif conttriples>=3:
        msj = '+Triples'
        
    return msj

def cargarListaAleat(inicio,fin,cantidad):
    lst = []
    if inicio>fin:
        for cantVeces in range(1,cantidad+1):
            lst.append(random.randint(fin,inicio))
    else:
        for cantVeces in range(1,cantidad+1):
            lst.append(random.randint(inicio,fin))
            
    if inicio==fin:
        for cantVeces in range(1,cantidad+1):
            lst.append(random.randint(fin,inicio))
    return lst

def main():
    inicio = int(input('Ingrese inicio: '))
    fin = int(input('Ingrese fin: '))
    cantidad = int(input('Ingrese la cantidad de numeros a generar: '))
    lst = cargarListaAleat(inicio,fin,cantidad)
    print(lst)
    print(atributoTriple(lst))
main()
'''
'''
#PRAC6 EJER11
import random

def ruleta():
    lst = []
    n = int(input('Ingrese un numero entero positivo: '))
    for i in range(n):
        aleatorio = random.randint(0,6)
        lst.append(aleatorio)
    return lst
    
def porcentual(lst):
    lst_sin_repetir = []
    contlista=1
    for i in lst:
        if i not in lst_sin_repetir:
            lst_sin_repetir.append(i)
            
    for caracter1 in lst_sin_repetir:
        cont=0
        for caracter2 in lst:
            if caracter1==caracter2:
                cont+=1
        if cont==1:
            print('El numero {} salió {} vez {}%'.format(caracter1,cont,(cont*100)/len(lst)))
        else:
            print('El numero {} salió {} veces {}%'.format(caracter1,cont,(cont*100)/len(lst)))

def main():
    r=ruleta()
    print(r)
    porcentual(r)
main()
'''
'''
#PRAC6 EJER12
def operaciones(a,b):
    tup=()
    suma= a+b
    resta= a-b
    multiplicacion = a*b
    if b == 0:
        division = None
    else:
        division = a/b
    tup= (suma,resta,multiplicacion,division)
    return tup
'''
'''
#PRAC6 EJER 13
def agregarDicEle(dic):
    print('Carguemos un Diccionario:')
    num = int(input('Ingrese numero a traducir o cero para salir: '))
    while num!=0:
        dic[num]=str(input('Ingrese el numero en letras: '))
        num = int(input('Ingrese numero a traducir o cero para salir: '))
    return dic

def main():
    dic = {}
    dic = agregarDicEle(dic)
    if len(dic)!=0:
        num = int(input('Ingrese numero para consultar ese numero en letras: '))
        while num not in dic:
            num = int(input('ERROR: Ingresar numero a traducir o cero para salir: '))
        print('{} --> {}'.format(num,dic[(num)]))
main()
'''
'''
#PRAC6 EJER14 
def agregarDicEle2(dic):
    print('Carguemos un diccionario: ')
    num = int(input('Ingrese 1 para añadir elementos al diccionario: '))
    while num !=1:
        print('DICCIONARIO VACIO BOBO')
        num = int(input('Ingrese UNO por favor: '))
    while num==1:
        numero = int(input('Ingrese numero a traducir: '))
        en = str(input('Ingrese traduccion al ingles: '))
        sp = str(input('Ingrese traduccion al español: '))
        de = str(input('Ingrese traduccion al aleman: '))
        dic[numero]=(en,sp,de)
        num = int(input('Seguir? Ingrese 1. En caso contrario pulse otro numero: '))
    return dic

def main():
    dic=dict()
    dic=agregarDicEle2(dic)
    num = int(input('Ingresar numero a traducir o cero para salir: '))
    while num!=0:
        while num not in dic:
            num = int(input('ERROR. El numero no esta en el diccionario: '))
        idioma = str(input("Ingresar idioma ['en'|'sp'|'de']: "))
        while idioma not in ('en','sp','de'):
            idioma = str(input('ERROR. Ingresar Idioma: '))
        if idioma == 'en':
            print('{} en Ingles: {}'.format(num,dic[num][0]))
        elif idioma=='sp':
            print('{} en Español: {}'.format(num,dic[num][1]))
        elif idioma =='de':
            print('{} en Alemán: {}'.format(num,dic[num][2]))
        num = int(input('Ingrese otro numero a traducir o cero para salir: '))
main()
'''
'''
#PRAC6 EJER15
def ordenarLst(lst):
    for pasada in range(len(lst)-1):
        for i in range(len(lst)-1):
            if lst[i]>lst[i+1]:
                lst[i],lst[i+1]=lst[i+1],lst[i]
    return lst


def agregarDicEle3():
    print('Carguemos un diccionario: ')
    dic= dict()
    n = int(input('Sistema de adicion de alumnos (pulse 0 para salir): '))
    while n!=0:
        dni = int(input('Ingrese DNI: '))
        apellido = str(input('Ingrese apellido: '))
        nombre = str(input('Ingrese nombre: '))
        nota1 = int(input('Ingresar la primer nota: '))
        nota2 = int(input('Ingrese la segunda nota: '))
        nota3 = int(input('Ingrese la tercer nota: '))
        lista1=[nombre,apellido]
        lista2=[nota1,nota2,nota3]
        listas_comb = [lista1,lista2]
        dic[dni]=listas_comb
        n = int(input('Seguir? (Ingrese 0 para cortar): '))
    return dic

def imprimirDic(dic):
    print('\nLa base de datos sin ordenar es: \n{}'.format(dic))
    
def imprimirDicOrd(dic):
    claves = list(dic.keys())
    ordenarLst(claves)
    print('\nLa base de datos ordenada es: ')
    baseOrd=dict()
    for c in claves:
        baseOrd[c]=dic[c]
    print(baseOrd)
    
    
def main():
    dic = agregarDicEle3()
    imprimirDic(dic)
    imprimirDicOrd(dic)
main()
'''