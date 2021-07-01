'''
#1.1)
def primero_igual_ultimo(n):
    ultimo = n%10
    while len(str(n))>1:
        digito = n%10
        n = n//10
    return ultimo==n

print(primero_igual_ultimo(52125))
'''
'''
#FALTA ENUNCIADO (?
#1.2)
def es_azar(digitos):
    mini =
    maxi =
    return
'''

#2.1)
def main():
    x = 12345
    if (5 in x):
        print('El número 5 está en el numero')
    else:
        print('El numero 5 no esta en el numero')
main()
#RTA: ERROR DE SINTAXIS BIEN

'''
#2.2)
def f1(num):
    num = num/25
    return num

def main():
    num = 10
    print(f1(num))
main()

#RTA: 0.4 BIEN
'''
'''
#2.3)
def main():
    l = [10,20,30,40,50]
    tam = len(l)
    i=1
    suma=0
    while i<=tam:
        suma+=l[i]
        i+=1
    return suma
main()

#RTA: NINGUNA DE LAS ANTERIORES BIEN
'''
'''
#2.4)
x = input()
if x>='a' or x<='z':
    print('Verdadero')
else:
    print('Falso')
#RTA: SIEMPRE RETORNA VERDADERO BIEN
'''