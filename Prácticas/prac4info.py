'''
#PRAC4 EJER1
def par(n):
    if (n%2)==0:
        return True
    else:
        return False
    
def multiplo_de_4(n):
    if n%4==0:
        return True
    else:
        return False

        
def main():
    contnum = 0
    contpar = 0
    contcuatro = 0
    while contpar < 5:
        a = int(input('ingrese numero entero: '))
        if par(a)==True:
            contpar += 1
            print('Numero par. Total de numeros pares ingresados:',contpar)
            if multiplo_de_4(a)==True:
                contcuatro += 1
                print('Numero par. Tambien es multiplo de 4. Total de numeros pares ingresados: ',contpar)
        contnum+=1
    print('FIN')
                
main()
'''
'''
#PRAC4 EJER2

def main():
    n = int(input('ingrese numeros enteros positivos (finalice con 0): '))
    mayor = n
    menor = n
    while n!=0:
        if n < menor:
            menor = n
        elif n > mayor:
            mayor = n
        n = int(input())
    print('el mayor es {} y el menor es {}'.format(mayor,menor))
main()
'''
'''
#PRAC4 EJER3
def primo(n):
    cont = 0
    if n==1:
        return False
    elif n==2:
        return True
    else:
        for i in range(2,n):
            if n%i==0:
                cont += 1
        if cont == 0:
            return True
        else:
            return False
        
        
def main():
    cant = int(input('Ingrese cantidad (numero natural): '))
    print('\n Primos entre 1 y ',cant)
    for i in range(cant+1):
        if primo(i)==True:
            print('{:5}'.format(i),end=' ')
            
    print('\n Primeros {} primos\n'.format(cant))
    
    for i in range (2,cant+1):
        cont = 0
        contnum = 0
        if primo(i)==True:
            print('{:5}'.format(i),end=' ')
            if (cont+1)%10==0:
                print('')
            cont+=1
            i+=1
        else:
            i+=1
main()
'''
'''
#PRAC4 EJER4
def perfecto(n):
    cont = 0
    for i in range(1,n):
        if n%i==0:
            cont+=i
    if cont==n:
        return True
    else:
        return False
    
def main():
    cantperfectos = 0
    num = 1
    while cantperfectos<4:
        if perfecto(num)==True:
            cantperfectos+=1
            print(num,end=' ')
        num+=1
main()
'''
'''
#PRAC4 EJER5
def condicion(n):
#    CIFRA DE CUATRO SI O SI
    UltimaCifra = n%10
    AnteUltima = (n//10)%10
    SegundaCifra = (n//100)%10
    PrimeraCifra = (n//1000)%10
    if (PrimeraCifra+AnteUltima) == (SegundaCifra+UltimaCifra):
        return True
    else:
        return False

def main():
    for i in range(1000,9999):
        if condicion(i)==True:
            print(i,end=' ')
main()
'''
'''
#PRAC4 EJER6
def aBinario(num):
    p = 1
    convertido = 0
    while num!=0:
        resto = num%2
        num = num//2
        convertido = convertido + resto*p
        p = p*10
    return convertido
    
def main():
    n = int(input('Ingrese un numero en decimal: '))
    print('Numero en  binario: ',aBinario(n))
main()
'''
'''
#PRAC4 EJER7 MAL
def aplazados(n):
    if n<4:
        return True
    else:
        return False
def aprobados(n):
    if n>=4 and n<=7:
        return True
    else:
        return False
def promocionados(n):
    if n>7 and n<=10:
        return True
    else:
        return False

def main():
    contnotas=0
    contaplazos=0
    contaprobados=0
    contpromocionados=0
    promedios = 0
    n = int(input('Ingrese nota: '))
    promedios += n
    contnotas+=1
    if n==0:
        print('No se ingresaron notas')
    while n!=0:
        if aplazados(n)==True:
            if n==0:
                contaplazos+=0
                contnotas+=0
            else:
                contaplazos+=1
                contnotas+=1
        elif aprobados(n)==True:
            contaprobados+=1
            contnotas+=1
        elif promocionados(n)==True:
            contpromocionados+=1
            contnotas+=1
        else:
            contnotas+=0
        n = int(input('Ingrese nota: '))
        promedios+=n
    print('Cantidad de aplazos: {}({}%)'.format(contaplazos,(((contaplazos*100)/contnotas))))
    print('Cantidad de aprobados: {}({}%)'.format(contaprobados,((contaprobados*100)/contnotas)))
    print('Cantidad de promocionados: {}({}%)'.format(contpromocionados,((contpromocionados*100)/contnotas)))
    print('Promedio General: {}%'.format((promedios*contnotas)/100))
main()
'''
'''
#PRAC4 EJER8
def factorial(n):
    cont = 1
    for i in range(1,n+1):
        cont*=i
    return cont
    
    
def main():
    n = int(input('Ingrese un numero entero: '))
    if n<=0:
        print('No se puede calcular el factorial')
    else:
        print('el factorial de {} es: {}'.format(n,factorial(n)))
main()
'''
'''
#PRAC4 EJER9
def capicua(num):
    n = num
    cont = 0
    while n>0:
        descomposicion = n%10
        cont = cont*10+descomposicion
        n = n//10
        
    if cont == num:
        return True
    else:
        return False
    
def main():
    n = int(input('Ingrese un numero: '))
    if capicua(n)==True:
        print('Es capicua')
    else:
        print('No es capicua')
main()
'''    
'''
#PRAC4 EJ10
def figura(b,h):
    for fila in range(b):
        for col in range(h):
             print('*',end='')
        else:
           print(' ',end='')
    
        print('')
        
def main():
    b = int(input('Ingrese base: '))
    while b < 2:
        b = int(input('Error, debe ser mayor o igual a 2. Ingrese base: '))
    h = int(input('Ingrese altura: '))
    while h < 2:
        h = int(input('Error, debe ser mayor o igual a 2. Ingrese altura: '))
    figura(h,b)    
main()
'''
'''
#PRAC4 EJ11
def figura(b,h):
    for fila in range(b):
        for col in range(h):
            if fila==0 or col==0 or fila==(b-1) or col==(h-1):
                print('*',end='')
            else:
                print(' ',end='')
        print()
        
def main():
    b = int(input('Ingrese base: '))
    while b < 2:
        b = int(input('Error, debe ser mayor o igual a 2. Ingrese base: '))
    h = int(input('Ingrese base: '))
    while h < 2:
        h = int(input('Error, debe ser mayor o igual a 2. Ingrese altura: '))
    figura(h,b)
main()
'''
'''
#PRAC4 EJER12
def figura(base):
    for fila in range(base):
        for col in range(base):
            if fila>=col:
                print('*',end='')
            else:
                print('-',end='')
        print()
        
def main():
    b = int(input('Ingrese base: '))
    while b<3:
        b = int(input('ERROR. Ingrese base: '))
    figura(b)
main()
'''

#PRAC4 EJER13
def figura(b):
    for fila in range((b//2)+1):
        for col in range(b):
            if fila==((b//2)) or col==(b//2) or (fila+col==((b-1)//2)  or fila>=-col+(b//2) and col-fila<=(b//2)):
                print('*',end='')
            else:
                print('-',end='')
        print()
        
def main():
    b = int(input('Ingrese base: '))
    while b%2==0 or b<3:
        b = int(input('Error. Ingrese base: '))
    figura(b)
main()

'''
#PRAC4 EJER14

def figura(b):
    for fila in range(b):
        for col in range(b):
            if fila<=(b//2) or   :
                print('*',end='')
            else:
                print('-',end='')
        print()

def main():
    b = int(input('Ingrese base: '))
    while b%2==0 or b<5:
        b = int(input('Error. Ingrese base: '))
    figura(b)
main()
'''