#retorna una lst con los habitantes que hay en dicha localidad que tengan exactamente
#la cantidad de hijos pasada por parametro, cargar en la lst el id habitante y el nombre
def cantHabitantes(nombreLocalidad,hijos):
    lst_lineas = []
    lst_a_retornar = []
    lst_hijos_cumple = []
    f = open("habitantes.csv","r")
    for linea in f.readlines():
        linea = linea[:-1]
        lst_lineas.append(linea.split(','))
    f.close()
    
    for linea in lst_lineas:
        if int(linea[2]) == hijos:
            lst_hijos_cumple.append(linea)
            
    for linea in lst_hijos_cumple:
        lst_intermedia = []
        lst_intermedia.append(linea[0])
        lst_intermedia.append(linea[1])
        lst_a_retornar.append(lst_intermedia)
            
    return lst_a_retornar


def ordenarLst(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-i-1):
            if lst[j][0] > lst[j+1][0]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
    return lst


def edadXlocalidad():
    lst_habitantes = []
    lst_localidades = []
    lst_habxloc = []
    lst_ID_loc = []
    f = open("habitantes.csv","r")
    for linea in f.readlines():
        linea = linea[:-1]
        lst_habitantes.append(linea.split(','))
    f.close()
   
    
    f = open("localidades.csv","r")
    for linea in f.readlines():
        linea = linea[:-1]
        lst_localidades.append(linea.split(','))
    f.close()
    
    
    f = open("habitantesXlocalidad.csv","r")
    for linea in f.readlines():
        linea = linea[:-1]
        lst_habxloc.append(linea.split(','))
    f.close()
    
    
    lst = []
    for i in range(len(lst_localidades)):
        cont_habitantes = 0
        edad = 0
        for j in range(len(lst_habxloc)):
            if int(lst_habxloc[j][0]) == int(lst_localidades[i][0]):
                ID_habitante = int(lst_habxloc[j][1])
            
                for x in range(len(lst_habitantes)):
                    if int(lst_habitantes[x][0]) == ID_habitante:
                        edad += int(lst_habitantes[x][3])
                        cont_habitantes += 1
                
        if edad!=0 and cont_habitantes!=0:
            lst.append([int(lst_localidades[i][0]),edad/cont_habitantes])
    
    lst = ordenarLst(lst)
    print("ID localidad   Promedio Edad")
    for i in range(len(lst)):
        print("{} ------------>  {}".format(lst[i][0],lst[i][1]))
            
    


def main():
    print(cantHabitantes("Adolfo Alsina",1))
    edadXlocalidad()
    dic = {"1":"uno","2":"dos"}
    print(dic)
    keys = list(dic)
    valores = list(dic.values())
    print(keys)
    print(valores)
    
    lst = [1,2]
    dic = {}
    dic[lst[0]] ="hola"
    dic[lst[1]] = "chau"
    print(dic)
main()