
#MAL
#1.1)
def binADec(num):
    bit = 0
    pot = 1
    dec = 0
    while num!=0:
        bit = num%10
        num = num//10
        dec = dec + bit*pot
        pot = pot*2
    return dec

print(binADec(100010))

'''
#BIEN
#1.2)
def dibujar(base):
    for i in range(base):
        print("*"+"*"*i)

dibujar(4)
'''
'''
#BIEN
#2.1)
def f2():
    lst=[]
    lst.append(1)
    lst.append(2)
    return lst
def f1(lst):
    lst = f2()
    lst.append(3)
    return lst

def main():
    lst= []
    f1(lst)  #NO SE GUARDA EN NINGUNA VARIABLE 
    print(lst)  #IMPRIME []
main()
'''
'''
#MAL BOOL(0)=FALSE, BOOL(OTRO NUM)=TRUE
#2.2)
def f(a,b):
    if not(a and b)!=(not a or not b):   #NOT(2 != False) -> NOT(TRUE) --> FALSE(RETURN 0)    // A AND B RETORNA EL VALOR DEL SEGUNDO (B) (ENTERO)
        return 1
    else:
        return 0
print(f(1,2))
'''
'''
#BIEN  -->  Error,num not defined
#2.3)
def foo():
    while num>0:
        num=1
        print("num")
def main():
    num=0
    foo()
main()
'''
'''
#BIEN  --> Error, las tuplas son inmutables
lst = [("Maria",32),("Tomas",40),("Lucas",16)]
lst[1][1] = 22
print(lst)
'''

