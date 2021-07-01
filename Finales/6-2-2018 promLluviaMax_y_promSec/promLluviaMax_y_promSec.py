def promLluviaMax(año):
    lst_lluvias = []
    lst_localidades = []
    lst_lluvias_con_año = []
    lst_ID_año = []
    f = open("lluvias.csv","r")
    for linea in f.readlines():
        linea = linea[:-1]
        lst_lluvias.append(linea.split(','))
    print(lst_lluvias)
    f.close()
    
    f = open("localidades.csv","r")
    for linea in f.readlines():
        linea = linea[:-1]
        lst_localidades.append(linea.split(','))
    print(lst_localidades)
    f.close()
    
    for i in range(len(lst_lluvias)):
        if (int(lst_lluvias[i][2])//10000) == año:
            lst_lluvias_con_año.append(lst_lluvias[i])
    print(lst_lluvias_con_año)
        
        
    for i in range(len(lst_lluvias_con_año)):
        if int(lst_lluvias_con_año[i][0]) not in lst_ID_año:
            lst_ID_año.append(int(lst_lluvias_con_año[i][0]))
    print(lst_ID_año)
    
    primero = True
    cantidad_lluvia = 0
    contador_lluvia = 0
    for i in range(len(lst_ID_año)):
        cont = 0
        for j in range(len(lst_lluvias_con_año)):
            if int(lst_lluvias_con_año[j][0]) == int(lst_ID_año[i]):
                cont += float(lst_lluvias_con_año[j][1])
                
        contador_lluvia += cont
        cantidad_lluvia += 1
        if primero==True:
            max_lluvia = cont
            min_lluvia = cont
            ID_max = lst_ID_año[i]
            ID_min = lst_ID_año[i]
            primero = False
        
        else:
            if cont > max_lluvia:
                max_lluvia = cont
                ID_max = lst_ID_año[i]
            
            if cont < min_lluvia:
                min_lluvia = cont
                ID_min = lst_ID_año[i]
    
    for i in range(len(lst_localidades)):
        if int(lst_localidades[i][0]) == ID_max:
            localidadMaxima = lst_localidades[i][1]
        
        if int(lst_localidades[i][0]) == ID_min:
            localidadMinima = lst_localidades[i][1]
            
    print("ID Localidad Maxima: {}, Localidad: {}".format(ID_max,localidadMaxima))
    print("ID Localidad Minima: {}, Localidad: {}".format(ID_min,localidadMinima))
    print("Promedio de Lluvia: ",(contador_lluvia/cantidad_lluvia))
    print("Minima cantidad de Lluvia: ",min_lluvia)
    print("Maxima cantidad de Lluvia: ",max_lluvia)
            
            
            
def promSec(lst):
    i = 0
    secuencia = 0
    largo = 0
    total = 0
    while i<len(lst):
        while i<len(lst) and lst[i]%2==1:
            largo = 0
            i+=1
        while i<len(lst) and lst[i]%2==0:
            largo+=1
            i+=1
        if largo!=0:
            secuencia+=1
            total += largo
    print(total/secuencia)        
            
            
    
            
        
    

def main():
    promLluviaMax(10)
    promSec([1,3,2,4,16,5,2,9,-4,10,22,8,14,11,39,4,63,12,60])
main()