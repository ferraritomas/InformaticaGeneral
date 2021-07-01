'''
#PRAC2 EJER1
import math

def triangulo(a,b,c):
    p = (a+b+c)/2
    area = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return area

def main():
    l1 = int(input('ingrese el lado 1: '))
    l2 = int(input('ingrese el lado 2: '))
    l3 = int(input('ingrese el lado 3: '))
    print('el area del triangulo es: {:.2f} '.format(triangulo(l1,l2,l3)))
main()
'''
'''
#PRAC2 EJER 2
import math
def raiz(x,n):
    res = math.pow(x,(1/n))
    return res
    
def main():
    r = int(input('ingrese el radicando (numero real): '))
    i = int(input('ingrese el indice (numero natural): '))
    print('la raiz {} de {} es = {:.2f}'.format(r,i,(raiz(r,i))))
main()
'''
'''
#PRAC2 EJER3
def paridad(nb):
    n0 = nb%10
    n1 = (nb//10)%10
    n2 = (nb//100)%10
    n3 = (nb//1000)%10
    n4 = (nb//10000)%10
    n5 = (nb//100000)%10
    n6 = (nb//1000000)%10
    n7 = (nb//10000000)%10
    bpg = (n0+n1+n2+n3+n4+n5+n6+n7)%2
    return bpg
    
    
def main():
    n = int(input('ingrese un numero binario de hasta 8 bits: '))
    print('bit de paridad generado: {}'.format(paridad(n)))
main()
'''
'''
#PRAC2 EJER4
import math
def areaCirc(d):
    return math.pi*((d/2)**2)
def areaCuad(l):
    return l**2
def areaNegra(l):
    return areaCuad(l) - areaCirc(l*(2/3)) - areaCirc(l*(1/3))*2
def main():
    a = int(input('ingrese el lado del cuadrado: '))
    porcentaje = (areaNegra(a)*100)/(areaCuad(a))
    print('el area negra es {:.2f} y es un {:.2f}% del area total del cuadrado'.format(areaNegra(a),porcentaje))
main()
'''
'''
#PRAC 2 EJER 5
import random
def funcion(n1,n2):
    return random.randint(n1,n2)
def main():
    li = int(input('ingrese el limite inferior (numero natural): '))
    ls = int(input('ingrese el limite superior (numero natural): '))
    print('Límite inferior {}, Límite superior {}, Número generado: {}'.format(li,ls,funcion(li,ls)))
main()
'''
'''
#PRAC2 EJER6 MAL
import random
def booleana(a1,a2):
    return random.randint(a1,a2)
def main():
    v1 = str(input('ingrese alternativa 1 para vestimenta: '))
    v2 = str(input('ingrese alternativa 2 para vestimenta: '))
    p1 = str(input('ingrese alternativa 1 para plato: '))
    p2 = str(input('ingrese alternativa 2 para plato: '))
    b1 = str(input('ingrese alternativa 1 para bebida: '))
    b2 = str(input('ingrese alternativa 2 para bebida: '))
    booleana1 = booleana(v1,v2)
    booleana2 = booleana(p1,p2)
    booleana3 = booleana(b1,b2)
    print('Cena al Azar: {}, {}, {}'.format(booleana1,booleana2,booleana3))
main()
'''
'''
#PRAC2 EJER7
def justificado(fra,ancho):
    a = (' '*(ancho-2)+fra)
    return a
    
def main():
    f = str(input('ingrese la frase: '))
    ancho = int(input('ingrese al ancho total a ser usado: '))
    print("'",justificado(f,ancho),"'")
main()
'''
'''
#PRAC2 EJER8
def crearFila(ancho):
    return str('*'*ancho)
        
def crearRectangulo(ancho,alto):
    b = (crearFila(ancho)+'\n')*alto
    return b
    
def main():
    ancho = int(input('ingrese ancho: '))
    alto = int(input('ingrese alto: '))
    print(crearRectangulo(ancho,alto))
main()
'''