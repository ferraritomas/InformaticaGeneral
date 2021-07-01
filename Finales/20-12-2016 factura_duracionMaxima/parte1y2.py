'''
#1.1) BIEN
def promLst(lst):
    i = 0
    prom = []
    for sl in lst:
        sum = 0
        for i in sl:
            sum += i
        prom.append(sum/len(sl))
    return prom

print(promLst([[1,3],[4,16],[5,5,10,20]]))
'''
'''
#1.2 BIEN
def ingresar():
    num = int(input("Num: "))
    while (num%7)==0 or (num%3)!=0 or (num%2)==0:
        print("Error")
        num = int(input("Num: "))
    return num

numero = ingresar()
print(numero)
'''
'''
#2.1) BIEN
x = input()
if x>='0' or x<='9':
    print("Correcto")
else:
    print("Incorrecto")
'''
'''
#2.2) BIEN
def f2(x):
    x-=5
    print(x,"",end="")
    
def f1():
    x = 5
    f2(x)
    print(x,"",end="")
    
x = 1
f1()
print(x,"",end="")
'''
'''
#2.3) BIEN
def cambiar(miStr,num):
    miStr[num] = 'x'
    y = num
    num+=1
    return miStr[num-y]

cad = "abcd"
n=3
letra = cambiar(cad,3)
print("{:s}-{:s}-{:d}".format(cad,letra,n))
'''
'''
#2.4)
xn = ['1','2','3','4']
n = "1234".split()
a = ('1' in xn)
b = ('2' in n)
print(a,b)
'''












