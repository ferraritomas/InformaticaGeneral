
#3.1)
#Desarrollar f1(nomArch) que recibe por parámetro el nombre de un archivo de texto
#(nomArch) y retorna una lista de las palabras sin repetir (en minúscula)
#El archivo de texto contiene lineas indeterminadas con frases, y las palabras pueden
#estar separadas por cualquier caracter que no es texto.

def reemplazarEspacios(lst):
    string = ""
    for i in range(len(lst)):
        if (lst[i]>="A" and lst[i]<="Z") or (lst[i]>='a' and lst[i]<='z') or (lst[i]=='á' or lst[i]=='é' or lst[i]=='í' or lst[i]=='ó' or lst[i]=='ú' or lst[i]=='Á' or lst[i]=='É' or lst[i]=='Í' or lst[i]=='Ó' or lst[i]=='Ú' or lst[i]=='ñ' or lst[i]=='Ñ'):
            string+=lst[i]
        else:
            string+=' '
    return string

def esPalabra(palabra):
    string = ""
    for letra in palabra:
        if (letra>='A' and letra<='Z'):
            string += chr(ord(letra)+32)
        elif (letra>='a' and letra<='z'):
            string += letra
        elif letra=='á' or letra=='Á':
            string += 'a'
        elif letra=='é' or letra=='É':
            string += 'e'
        elif letra=='í' or letra=='Í':
            string += 'i'
        elif letra=='ó' or letra=='Ó':
            string += 'o'
        elif letra=='ú' or letra=='Ú':
            string += 'u'
        elif letra=='ñ' or letra=='Ñ':
            string += 'ñ'
    return string
            
 

def f1(nomArch):
    lst_lineas = []
    lst_con_espacios = []
    lst_palabras_con_espacios = []
    lst_palabras = []
    lst_palabras_corregidas = []
    lst_palabras_sin_repetir = []
    f = open(nomArch,"r")
    for linea in f.readlines():
        linea = linea[:-1]
        lst_lineas.append(linea)
    f.close()

    for linea in lst_lineas:
        lst_con_espacios.append(reemplazarEspacios(linea))
    
    
    for lst in lst_con_espacios:
        lst_palabras_con_espacios.append(lst.split(' '))
   
    
    for i in range(len(lst_palabras_con_espacios)):
        lst_palabras += lst_palabras_con_espacios[i]    
    
    
    for palabra in lst_palabras:
        if len(palabra)!=0:
            lst_palabras_corregidas.append(esPalabra(palabra))

    
    for palabra in lst_palabras_corregidas:
        if palabra not in lst_palabras_sin_repetir:
            lst_palabras_sin_repetir.append(palabra)
            
    return lst_palabras_sin_repetir
            
#3.2)
#Desarrollar f2(nombreArch,lst), que recibe por parámetro el nombre de un archivo CSV y una lista de palabras (la que retorna f1).
#La funcion debe crear y retornar un diccionario que tenga como clave las palabras del archivo y como valor de cada clave,
#las palabras de lst que tengan las mismas 4 ultimas letras que la clave.
#El archivo contiene lineas indefinidas, con palabras separadas por coma.    
    

def f2(nomArch,lst):
    dic = {}
    lst_lineas = []
    lst_palabras = []
    lst_cuatro_letras = []
    f = open(nomArch,"r")
    for linea in f.readlines():
        linea = linea[:-1]
        lst_lineas.append(linea.split(','))
    
    for i in range(len(lst_lineas)):
        lst_palabras += lst_lineas[i]
    
    for i in range(len(lst_palabras)):
        lst_cuatro_letras = []
        for j in range(len(lst)):
            if (lst_palabras[i][-4:]) == lst[j][-4:]:
                lst_cuatro_letras.append(lst[j])
        
        dic[lst_palabras[i]] = lst_cuatro_letras
    return dic
    
    
    
def main():
    lst = f1('texto.txt')
    dic = f2('texto2.csv',lst)
    print(dic)
    keys = list(dic)
    valores = list(dic.values())
    print(keys)
    print(valores)
main()