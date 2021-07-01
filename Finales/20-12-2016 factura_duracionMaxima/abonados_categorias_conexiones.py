def factura(ID_abonado):
    lst_abonados = []
    lst_categorias = []
    lst_conexiones = []
    
    f = open("abonados.csv","r")
    for linea in f.readlines():
        linea = linea[:-1]
        linea = linea.split(',')
        linea[0] = int(linea[0])
        linea[3] = int(linea[3])
        lst_abonados.append(linea)
    f.close()
    
    f = open("categorias.csv","r")
    for linea in f.readlines():
        linea = linea[:-1]
        linea = linea.split(',')
        linea[0] = int(linea[0])
        linea[1] = float(linea[1])
        linea[2] = float(linea[2])
        lst_categorias.append(linea)
    f.close()
    
    f = open("conexiones.csv","r")
    for linea in f.readlines():
        linea = linea[:-1]
        linea = linea.split(',')
        linea[0] = int(linea[0])
        linea[1] = int(linea[1])
        lst_conexiones.append(linea)
    f.close()
    
    
    cont_minutos = 0
    for i in range(len(lst_abonados)):
        if lst_abonados[i][0] == ID_abonado:
            nombre = lst_abonados[i][1]
            domicilio = lst_abonados[i][2]
            
            for j in range(len(lst_categorias)):
                if lst_categorias[j][0] == lst_abonados[i][3]:
                    abono = lst_categorias[j][1]
                    importe_por_minuto = lst_categorias[j][2]
            
                    for x in range(len(lst_conexiones)):
                        if lst_conexiones[x][0] == lst_abonados[i][0]:
                            cont_minutos += lst_conexiones[x][1]
    
    importe = importe_por_minuto * cont_minutos
    print("Nombre: ",nombre)    
    print("Domicilio: ",domicilio)
    print("Abono: ",abono)
    print("Importe: ",importe)
    print("Total: ",abono+importe)
    
    
    
def duracionMaxima():
    lst_abonados = []
    lst_categorias = []
    lst_conexiones = []
    
    f = open("abonados.csv","r")
    for linea in f.readlines():
        linea = linea[:-1]
        linea = linea.split(',')
        linea[0] = int(linea[0])
        linea[3] = int(linea[3])
        lst_abonados.append(linea)
    f.close()
    
    f = open("categorias.csv","r")
    for linea in f.readlines():
        linea = linea[:-1]
        linea = linea.split(',')
        linea[0] = int(linea[0])
        linea[1] = float(linea[1])
        linea[2] = float(linea[2])
        lst_categorias.append(linea)
    f.close()
    
    f = open("conexiones.csv","r")
    for linea in f.readlines():
        linea = linea[:-1]
        linea = linea.split(',')
        linea[0] = int(linea[0])
        linea[1] = int(linea[1])
        lst_conexiones.append(linea)
    f.close()
    
    
    lst_ID_abonado = []
    for i in range(len(lst_abonados)):
        if lst_abonados[i][0] not in lst_ID_abonado:
            lst_ID_abonado.append(lst_abonados[i][0])
    
    
    primero = True
    for i in range(len(lst_ID_abonado)):
        cont = 0
        for j in range(len(lst_conexiones)):
            if lst_conexiones[j][0] == lst_ID_abonado[i]:
                cont += lst_conexiones[j][1]
        if primero == True:
            duracion_maxima = cont
            ID_max = lst_ID_abonado[i]
            nombre = lst_abonados[i][1]
            ID_categoria_maxima = lst_abonados[i][3]
            primero = False
        
        else:
            if cont > duracion_maxima:
                duracion_maxima = cont
                ID_max = lst_ID_abonado[i]
                nombre = lst_abonados[i][1]
                ID_categoria_maxima = lst_abonados[i][3]
    
    print("ID_abonado: ",ID_max)
    print("Nombre: ",nombre)
    print("Categoria: ",ID_categoria_maxima)
    print("Duracion Maxima: ",duracion_maxima)
    
    
def main():
    ID_abonado = 3
    factura(ID_abonado)
    print("\n")
    duracionMaxima()
main()