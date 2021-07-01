'''
#PRAC5 EJER1
def trespals(s):
    if len(s)<2:
        return ''
    else:
        return (s[len(s)-2] + s[len(s)-1])*3
    
def main():
    pal = str(input('Ingrese una palabra: '))
    if trespals(pal)=='':
        print('La funcion ha retornado una palabra vacia')
    else:
        print('La funcion ha retornado: {}'.format(trespals(pal)))
    
main()
'''
'''
#PRAC5 EJER2
def extremos(s,palabra):
    primer = s[len(s)-2]
    segundo = s[len(s)-1]
    unidos = primer+palabra+segundo
    return unidos

def main():
    ext = str(input('Ingrese los extremos: '))
    pal = str(input('Ingrese palabra: '))
    if len(ext)!=2 or pal=='':
        print('La funcion ha retornado una palabra vacía')
    else:
        print('La función retornó: {}'.format(extremos(ext,pal)))
main()
'''
'''
#PRAC5 EJER3
def primeraMitad(pal):
    if (len(pal)%2)!=0:
        return False
    else:
        return pal[0:len(pal)//2]
    
def main():
    pal = str(input('Ingrese una palabra de longitud par: '))
    while primeraMitad(pal)==False:
        pal = str(input('Error. Ingrese una palabra de longitud par: '))
    print('La funcion ha retornado: {}'.format(primeraMitad(pal)))
main()
'''
'''
#PRAC5 EJER4
def es_letra(c):
    if (c>='a' and c<='z') or (c>='A' and c<='Z'):
        return True
    else:
        return False
    
def a_minuscula(c):
    if c>='a' and c<='z':
        letra = c
    elif c>='A' and c<='Z':
        letra = chr(ord(c)+32)
    elif c=='á' or c=='Á':
        letra = 'á'
    elif c=='é' or c=='É':
        letra = 'é'
    elif c=='í' or c=='Í':
        letra = 'í'
    elif c=='ó' or c=='Ó':
        letra = 'ó'
    elif c=='ú' or c=='Ú':
        letra = 'ú'
    elif c=='ñ' or c=='Ñ':
        letra = 'ñ'
    return letra
    
def principioFin(txt):
    i=0
    primerPalabra=True
    while i<len(txt):
        while i<len(txt) and es_letra(txt[i])==False:
            i+=1
        pal=""
        while i<len(txt) and es_letra(txt[i]):
            pal+=txt[i]
            i+=1
        if primerPalabra==True:
            primera=pal
            primerPalabra=False
    primera_min=""
    for l in range(len(primera)):
        primera_min+=a_minuscula(primera[l])
    x=0
    invertido=txt[::-1]                          #Texto invertido
    primera2=True
    while x<len(invertido):
        while (x<len(invertido) and es_letra(invertido[x])==False):
            x+=1
        ultima=""
        while (x<len(invertido) and es_letra(invertido[x])==True):
            ultima+=invertido[x]
            x+=1
        if primera2==True:
            ultima_final=ultima
            primera2=False
    ultima_final=ultima_final[::-1]
    ultima_minuscula=""
    for l in range(len(ultima_final)):
        ultima_minuscula+=a_minuscula(ultima_final[l])
    return primera_min==ultima_minuscula

def main():
    texto=input('Ingrese un texto: ')
    if principioFin(texto)==True:
        print('El texto cumple la condicion')
    else:
        print('El texto no cumple la condicion')
main()        
'''
'''
#PRAC5 EJER5
def rotacion(s):
    PrimeraMitad = s[0:len(s)//2]
    SegundaMitad = s[len(s)//2:len(s)]
    retornar = SegundaMitad+PrimeraMitad
    return retornar

def main():
    s = str(input('Ingrese un texto: '))
    while len(s)<2 or (len(s))%2!=0:
        s = str(input('Error. Ingrese un texto: '))
    print('La funcion ha retornado: ',rotacion(s))
main()
'''
'''
#PRAC5 EJER6
def a_minuscula(l):
    letra = l
    if l>='A' and l<='Z':
        letra = chr(ord(l)+32)
    elif l=='Á' or l=='á':
        letra = 'a'
    elif l=='É' or l=='é':
        letra = 'e'
    elif l=='Í' or l=='í':
        letra = 'i'
    elif l=='Ó' or l=='ó':
        letra = 'o'
    elif l=='Ú' or l=='ú':
        letra = 'u'
    return letra


def es_letra(c):
    if (c>='a' and c<='z') or (c>='A' and c<='Z') or c=='á' or c=='Á' or c=='í' or c=='Í' or c=='é' or c=='É' or c=='ó' or c=='Ó' or c=='ú' or c=='Ú' or c=='ñ' or c=='Ñ':
        return True
    else:
        return False
    
def palindroma(frase):
    basura = ''
    fraselimpia = ''
    for i in range(len(frase)):
        if es_letra(frase[i]):
            fraselimpia+=a_minuscula(frase[i])
        else:
            basura+=frase[i]
    if fraselimpia[0:len(fraselimpia)]==fraselimpia[::-1]:
        return True
    else:
        return False
        
    
def main():
    frase = str(input('Ingrese una frase: '))
    if palindroma(frase)==True:
        print('La frase es palindroma!')
    else:
        print('La frase no es palindroma!')
    
main()
'''
'''
#PRAC5 EJER7
def buscador(largo,corto):
    contcorto=0
    for i in range(len(largo)):
        if corto in (largo[i:len(corto)+i]):
            contcorto+=1
    return contcorto

def main():
    largo = str(input('Ingrese el texto largo: '))
    corto = str(input('Ingrese el texto corto: '))
    print('El texto corto se encontró {} veces en el texto largo'.format(buscador(largo,corto)))
main()
'''
'''
#PRAC5 EJER8
def pasaje(c):
    if (c>='A' and c<='Z'):
        letra = c
    elif (c>='a' and c<='z'):
        letra = chr(ord(c)-32)
    elif c=='á' or c=='Á':
        letra = 'Á'
    elif c=='é' or c=='É':
        letra = 'É'
    elif c=='í' or c=='Í':
        letra = 'Í'
    elif c=='ó' or c== 'Ó':
        letra = 'Ó'
    elif c=='ú' or c=='Ú':
        letra = 'Ú'
    elif c=='ñ' or c=='Ñ':
        letra = 'Ñ'
        
    return letra
    
def es_letra(c):
    if (c>='a' and c<='z') or (c>='A' and c<='Z') or c=='á' or c=='Á' or c=='é' or c=='É' or c=='í' or c=='Í' or c=='ó' or c=='Ó' or c=='ú' or c=='Ú' or c=='ñ' or c=='Ñ':
        return True
    else:
        return False
    

def mayuscula(t):
    i = 0
    retornar = ''
    pal=''
    primera = True
    while i<len(t):
        while i<len(t) and not es_letra(t[i]):
            pal+=t[i]
            i+=1
            
        primera = True
        while i<len(t) and es_letra(t[i]):
            if primera==True:
                pal += pasaje(t[i])
                primera = False
            else:
                pal+=t[i]
            i+=1
        
    return pal

def main():
    t = str(input('Ingrese un texto: '))
    print(mayuscula(t))
main()
'''
'''
#PRAC5 EJER9

def es_letra(l):
    if (l>="a" and l<="z") or (l>="A" and l<="Z"):
        return True
    else:
        return False

def pal_larga(txt):
    i=0
    pal=""
    pal_max=""
    while i<len(txt):
        while i<(len(txt)) and es_letra(txt[i])==True:
            pal+=txt[i]
            i+=1
        if len(pal)>len(pal_max):
            pal_max=pal
        if i<len(txt) and es_letra(txt[i])==False:
            pal=""
        i+=1
    return pal_max

def pal_corta(txt):
    i=0
    pal=""
    primera=1
    while i<len(txt):
        while i<len(txt) and es_letra(txt[i])==True:
            pal+=txt[i]
            i+=1
        if primera==1:
            pal_min=pal
        if len(pal)<len(pal_min) and len(pal)!=0:
            pal_min=pal
        if i<len(txt) and es_letra(txt[i])==False:
            pal=""
        i+=1
        primera+=1
    return pal_min

def contar_palabras(txt):
    cont_pal=0
    nueva_pal=0
    i=0
    while i<len(txt):
        if es_letra(txt[i])==True and nueva_pal==0:
            nueva_pal+=1
            cont_pal+=1
        elif es_letra(txt[i])==False:
            nueva_pal=0
        i+=1
    return cont_pal
  
def main():
    texto=input("Ingrese un texto: ")
    print("El texto tiene {} palabras, la de mayor longitud es '{}' y la de menor longitud es'{}'" .format(contar_palabras(texto),pal_larga(texto),pal_corta(texto)))
main()
'''
'''
#PRAC5 EJER10

def es_letra(l):
    if (l>="a" and l<="z") or (l>="A" and l<="Z"):
        return True
    else:
        return False
def comparar(pal1,pal2):
    cumple=True
    cont1=0
    cont2=0
    for letra in pal1:
        for letra1 in pal1:
            if letra==letra1:
                cont1+=1
        for letra2 in pal2:
            if letra==letra2:
                cont2+=1
        if cont1!=cont2 or len(pal1)!=len(pal2) :
            cumple=False
    return cumple
def analizar(txt,pal):
    i=0
    p=""
    while i<len(txt):
        while i<len(txt) and es_letra(txt[i])==False:
            i+=1
        p=""
        while i<len(txt) and es_letra(txt[i])==True:
            p+=txt[i]
            i+=1
        if comparar(p,pal)==True:
            return True
    return False
            

def main():
    texto=input("Ingrese el texto: ")
    palabra=input("Ingrese la palabra: ")
    if analizar(texto,palabra)==True:
        print("Se cumple con la condición")
    else:
        print("No se cumple con la condición")
main()
'''
