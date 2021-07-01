'''
#1.1) BIEN
#Retorna True si la cantidad de cifras impares que hay en el numero es par.
#False en caso contrario.

def cont_dig_impar(n):
    cont = 0
    while n!=0:
        dig = n%10
        if dig%2 == 1:
            cont+=1
        n = n//10
    return cont%2 == 0

print(cont_dig_impar(246578)) #True
print(cont_dig_impar(34)) #False
print(cont_dig_impar(236417)) #False
'''
'''
#1.2) ESTUDIAR
#Recibe por parametro los numeros a y b, y se sabe que a es menor a b.
#La funcion genera un numero aleatorio en el intervalo [a,b] y retorna un numero
#que puede ser 1 3 5 7 o 9 (cualquiera de estos)

import random
def aleatorio(a,b):
    num = (random.randint(a,b)%5)*2+1
    return num

print(aleatorio(100,300)) #Retorna 1,3,5,7 o 9
'''
'''
#BIEN   Error retorno sin funcion
#2.1)
dic = {10:12,12:10}
if dic.get(21)!=None:
    x=dic[21]+1
else:
    x = dic[12]+1
return x+1
'''
'''
#BIEN error de index ([,6])
#2.3)
lst = [[1,2],'Hola Mundo',[,6]]
print(lst[0][0][0:lst[2][0]])
'''
'''
#BIEN 00123
#2.4)
sum = '0'
n = '0123'
for x in n:
    sum=sum+x
print(sum)
'''
