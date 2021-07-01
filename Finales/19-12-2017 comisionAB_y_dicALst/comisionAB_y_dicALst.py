#3.1)Tengo los archivos "Comision A" y "Comision B" donde esta el numero de registro, el nombre y el apellido separados por coma,
#puede una misma persona estar en ambos archivos. Tengo que crear el archivo "Comision AB" donde aparecieran todas las personas 
#sin repetirse y ordenarlo por numero de registro ascendente.
'''
def ordenarLst(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-i-1):
            if lst[j][0] > lst[j+1][0]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
    return lst

def mezclarListas():
    lstA = []
    lstB = []
    lstAB = []
    f = open("comisionA.csv","r")
    for linea in f.readlines():
        linea = linea[:-1]
        linea = linea.split(',')
        linea[0] = int(linea[0])
        lstA.append(linea)
    f.close()
    print(lstA)
    
    f = open("comisionB.csv","r")
    for linea in f.readlines():
        linea = linea[:-1]
        linea = linea.split(',')
        linea[0] = int(linea[0])
        lstB.append(linea)
    f.close()
    print(lstB)
    
    for lst in lstA:
        if lst not in lstAB:
            lstAB.append(lst)
    for lst in lstB:
        if lst not in lstAB:
            lstAB.append(lst)
    print(lstAB)
    
    lstAB = ordenarLst(lstAB)
    
    f = open("comisionAB.csv","w")
    for i in range(len(lstAB)):
        linea = (str(lstAB[i][0])+','+lstAB[i][1]+','+lstAB[i][2]+'\n')
        print(linea)
        f.write(linea)
    f.close()
    
'''       
#3.2)Me dan un diccionario como parametro, como clave tiene el apellido de un alumno y como valor una lista con sus notas.
#Tengo que imprimir por pantalla el apellido del alumno con su promedio de notas en orden descendente.
  
def transformarDicALista(dic):
    nombres = list(dic)
    notas = list(dic.values())
    lst = []
    for i in range(len(dic)):
        lst_intermedia = []
        lst_intermedia.append(nombres[i])
        lst_intermedia.append(notas[i])
        lst.append(lst_intermedia)
    return lst


def ordenarLst(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-i-1):
            if lst[j][1] < lst[j+1][1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
    return lst

def ordenarDic(dic):
    lst = transformarDicALista(dic)
    lst_promedios = []
    for i in range(len(lst)):
        cont = 0
        cant_notas = 0
        lst_intermedia = []
        for x in range(len(lst[i][1])):
            cont += lst[i][1][x]
            cant_notas+=1
    
        lst_intermedia.append(lst[i][0])
        lst_intermedia.append(cont/(cant_notas))
        lst_promedios.append(lst_intermedia)
    print(lst_promedios)
        
    lst_promedios = ordenarLst(lst_promedios)
    print(lst_promedios)
        
    
def main():
    #mezclarListas()
    dic = {"Lautaro":[9,7,5,8],"Tomás":[9,8,5,10],"Agustin":[2,3,5,10]}
    #print(dic)
    ordenarDic(dic)
    #print(dic)
main()







