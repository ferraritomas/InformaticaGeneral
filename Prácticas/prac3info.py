'''
#PRAC3 EJER1
def cuenta(n1,n2,s):
    if s=='+':
        res = n1+n2
    elif s=='-':
        res = n1-n2
    elif s=='*':
        res = n1*n2
    elif s=='/':
        res = n1/n2
    else:
        print('ERROR')
    return res
        
def main():
    p = int(input('ingrese el primer numero: '))
    s = int(input('ingrese el segundo numero: '))
    op = str(input('ingrese la operacion (+,-,*,/): '))
    print(p,op,s,'=',cuenta(p,s,op))
main()
'''
'''
#PRAC3 EJER2
def funcion(n1,n2,n3):
    if n1<n2 and n2<n3:
        orden = '\n'+str(n1)+'\n'+str(n2)+'\n'+str(n3)
    elif n2<n3 and n3<n1:
        orden = '\n'+str(n2)+'\n'+str(n3)+'\n'+str(n1)
    elif n2<n1 and n1<n3:
        orden = '\n'+str(n2)+'\n'+str(n1)+'\n'+str(n3)
    elif n3<n2 and n2<n1:
        orden = '\n'+str(n3)+'\n'+str(n2)+'\n'+str(n1)
    elif n1<n3 and n3<n2:
        orden = '\n'+str(n1)+'\n'+str(n3)+'\n'+str(n2)
    elif n2<n1 and n1<n3:
        orden = '\n'+str(n2)+'\n'+str(n1)+'\n'+str(n3)
    return orden
            
def main():
    a = int(input('ingrese el primer numero: '))
    b = int(input('ingrese el segundo numero: '))
    c = int(input('ingrese el tercer numero: '))
    print('los numeros ordenados de forma ascendente son: ',funcion(a,b,c))
main()
'''
'''
#PRAC3 EJER3
def funcion(nr):
    if nr==0:
        res = 'Cero'
    elif nr<0:
        res = 'Negativo'
    else:
        res = 'Positivo'
    return res

def definicion(n):
    if (n%1)==0 and n>0:
        res = 'Natural'
    elif (n%1)==0:
        res = 'Entero'
    else:
        res = 'Real'
    return res    
    
def main():
    a = float(input('ingrese un numero: '))
    print('el numero es {} y {}'.format(funcion(a),definicion(a)))
main()
'''
'''
#PRAC3 EJER4
def booleana(n1,n2):
    if n1>n2:
        mayor = n1
        menor = n2
    else:
        mayor = n2
        menor = n1
        
    if (mayor-menor)>=menor and (mayor-menor)<=mayor:
        return 'SI'
    else:
        return 'NO'
    
def main():
    a = int(input('ingrese un numero A: '))
    b = int(input('ingrese un numero B: '))
    print('{} cumple condicion'.format(booleana(a,b)))
main()
'''
'''
#PRAC3 EJER5 MALLLL
def booleana(d,m,a):
    bisiesto = (año%4 == 0 and año%100 != 0) or (año%400 ==0)
    if (d>=1 and d<=31) and (m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12) and (a<=2019):
        return True
    elif (d>=1 and d<=30) and (m==4 or m==6 or m==9 or m==11):
        return True
    else:
        return False
    
def main():
    d = int(input('ingrese el dia: '))
    m = int(input('ingrese el mes: '))
    a = int(input('ingrese el año: '))
    if booleana==True:
        c = 'correcta'
    else:
        c = 'incorrecta'
    
    print('La fecha es ',c)
main()
'''
'''
#PRAC3 EJER6
def booleana(n):
    if n%2==0:
        num = int(input('ingrese un numero menor que {}: '.format(n)))
        if num<n:
            return 'Correcto!'
        else:
            return 'Incorrecto!'
    else:
        num = int(input('ingrese un numero mayor que {}: '.format(n)))
        if num>n:
            return 'Correcto!'
        else:
            return 'Incorrecto!'
        
        
def main():
    a = int(input('ingrese un numero entero positivo: '))
    c = booleana(a)
    print(c)

main()
'''
'''
#PRAC3 EJER7
def booleana(n1,n2,n3):
    if n1<=n2 and n2<=n3:
        mayor = n3
        medio = n2
        menor = n1
    elif n2<=n3 and n3<=n1:
        mayor = n1
        medio = n3
        menor = n2
    elif n2<=n1 and n1<=n3:
        mayor = n3
        medio = n1
        menor = n2
    elif n3<=n2 and n2<=n1:
        mayor = n1
        medio = n2
        menor = n3
    elif n1<=n3 and n3<=n2:
        mayor = n2
        medio = n3
        menor = n1
    elif n2<=n1 and n1<=n3:
        mayor = n3
        medio = n1
        menor = n2
    
    if (mayor-medio)==(medio-menor):
        return True
    else:
        return False
    
    
def main():
    a = int(input('ingrese el primer numero: '))
    b = int(input('ingrese el segundo numero: '))
    c = int(input('ingrese el tercer numero: '))
    res = booleana(a,b,c)
    if res == True:
        print('Están igualmente distanciados')
    else:
        print('NO Están igualmente distanciados')
    
main()
'''

#PRAC3 EJER8
def promedio(n1,n2,n3):
    if n1>4 and n2>4 and n3>4 and ((n1+n2+n3)/3)>=7:
        
    elif n1>4 and n2>4 and n3>4 and ((n1+n2+n3)/3)<7:
        
    elif n1<4 or n2<4 or n3<4:
        a = int(input('ingrese la nota del recuperatorio: '))
        
        
    
def notatotal(n1,n2,n3,pg):
    
    
def main():
    
main()
    
    
    