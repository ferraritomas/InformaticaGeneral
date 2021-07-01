
def buscarS(xs,s):
    if s not in xs:
        tupla = (-1,-1)
    else:
        primero = True
        for i in range(len(xs)-1):
            if (xs[i:i+len(s)] == s) and primero == True:
                tupla = (i,i+len(s)-1)
                primero = False
    return tupla
        
def listaIndice(xs,s):
    lst = []
    bandera = True
    string = buscarS(xs,s)
    
    if string!=(-1,-1):
        inicio = string[0]  #posiciones de la tupla que retornó buscarS
        fin = string[1]
        lst.append(string)
    
        while bandera == True:
            xs = xs[string[1]+1:]
            string = buscarS(xs,s)
            if string!=(-1,-1):
                inicio = fin+string[0]+1
                fin = inicio+len(s)-1
                string = (inicio,fin)
                lst.append(string)
            else:
                bandera = False
    return lst
        
    
                

    
def main():
    s = "zz"
    f = open("info.txt","r")
    for linea in f.readlines():
        linea = linea[:-1]
    print(linea)
        
    print(buscarS(linea,s))
    print(listaIndice(linea,s))
main()