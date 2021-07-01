def comision(ventas,objetivo,sueldo):
    if ventas < (objetivo*0.8):
        comision = 0
    elif (ventas <= objetivo) and (ventas >= (objetivo*0.8)):
        comision = sueldo * 0.03
    else:
        comision = sueldo*0.1
        
    return comision
    


def liquidar():
    lst_tarjetas = []
    lst_vendedores = []
    lst_liquidacion = []
    
    f = open("ventasTarjetas.csv","r")
    for linea in f.readlines():
        linea = linea[:-1]
        lst_tarjetas.append(linea.split(','))
    f.close()
    print(lst_tarjetas)
    
    f = open("vendedores.csv","r")
    for linea in f.readlines():
        linea = linea[:-1]
        lst_vendedores.append(linea.split(','))
    f.close()
    print(lst_vendedores)
    
  
    f = open("liquidacionComisiones.csv","w")
    for i in range(len(lst_vendedores)):
        totalTarjetas=0
        lst_intermedia = []
        for j in range(len(lst_tarjetas)):          
            if (int(lst_vendedores[i][0]) == int(lst_tarjetas[j][0])):       
                totalTarjetas += int(lst_tarjetas[j][2])
                objetivo = int(lst_vendedores[j][2])
                sueldo = float(lst_vendedores[j][3])
        com=comision(totalTarjetas,objetivo,sueldo) 
        com=round(com, 2)
        print(str(lst_vendedores[i][0])+","+str(com)+"\n")
        f.write(str(lst_vendedores[i][0])+","+str(com)+"\n")
        lst_intermedia.append(int(lst_vendedores[i][0]))
        lst_intermedia.append(com)
        lst_liquidacion.append(lst_intermedia)
                
    f.close()
    
    
    return lst_liquidacion
    
    
def topcinco(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-i-1):
            if lst[j][1] < lst[j+1][1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
                
    print(lst)
    lst_vendedores = []
    f = open("vendedores.csv","r")
    for linea in f.readlines():
        linea = linea[:-1]
        linea = linea.split(',')
        linea[0] = int(linea[0])
        linea[2] = int(linea[2])
        linea[3] = float(linea[3])
        lst_vendedores.append(linea)
    print(lst_vendedores)
    
    lst_final = []
    for i in range(len(lst)):
        lst_intermedia = []
        for j in range(len(lst_vendedores)):
            if lst[i][0] == lst_vendedores[j][0]:
                lst_intermedia.append(lst[i][0])
                lst_intermedia.append(lst[i][1])
                lst_intermedia.append(lst_vendedores[j][1])
                lst_final.append(lst_intermedia)
    print(lst_final)
    
    for i in range(len(lst_final)):
        print("{} {} {}".format(lst_final[i][0],lst_final[i][2],lst_final[i][1]))
    
def main():
    lst = liquidar()
    print(lst)
    topcinco(lst)
main()