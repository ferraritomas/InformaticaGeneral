'''
#1.1)Completar una funcion que recibe por parametro un numero y retorne True or False si el ultimo digito es igual al primer digito:  1234 -> False,  5005 -> True
def primero_igual_ultimo(n):
    ultimo = n%10
    while n!=0:
        dig = n%10
        n = n//10
    return dig==ultimo    
    
def main():
    print(primero_igual_ultimo(1234))
    print(primero_igual_ultimo(5005))
main()
'''
'''
#1.2) Completar una funcion que recibe dos listas pasadas por parametro y retorne una nueva lista que contenga todos los numeros de la primera lista que no se encuentren en la segunda lista: foo([1,2,3,4,5],[1,2]) -> [3,4,5]
def foo(A,B):
    lst = []
    for i in range(len(A)):
        if A[i] not in B:
            lst.append(A[i])
    return lst
def main():
    print(foo([1,2,3,4,5],[1,2]))
main()
'''

#MAL - RTA: "4334" - EL FOR I IN RANGE(4) TOMA HASTA i=3 (SI TOMA i=4 DABA ERROR OUT OF RANGE)
#2.1)
y = (1,2,0,1)
x = ["2","4","3"]
z = ""
for i in range(0,len(y)):
    z = z + (x[y[i]] * y[i])
print(z)

"""
1era vuelta: i=0
for i in range(4):
    z = "" + ("4"*1)
z = "4"
2da vuelta:
for i in range(4): i=1
    z = "4" + ("3" * 2)
z = "433"
3ra vuelta: i=2
for i in range(4):
    z = "433" + ("2" * 0)
z = "433"
4ta vuelta: i=3
for i in range(4):
    z = "433" + ("4" * 1)
    z = "4334"
"""
'''
BIEN - RTA: 10 (NO ENTRA NUNCA A F1)
#2.2)
def f1(num):
    num = num/25
    return num

def main():
    num =10
    f1(num)
    print(num)
main()
'''
'''
#BIEN - LST OUT OF RANGE (TRUCO EN EL <=)
#2.3)
lst = [10,20,30,40,50]
tam = len(lst) #tam=5
i = 1
suma = 0
while i<=tam:
    suma += lst[i]
    i+=1
print(suma)
'''
"""
1ra vuelta:
suma = 20
i=2
2da vuelta:
suma = 50
i=3
3ra vuelta:
suma = 90
i=4
4ta vuelta:
suma = 140
i=5
LST OUT OF RANGE
"""
'''
#2.4)
def foo():
    sum = "0"
    for x in "0123":
        if not(x=="0" and x=="1") == (not x=="0" or not x=="1"):
            sum = sum+x
    return sum
def main():
    print(foo())
main()
'''
"""
1ra vuelta x=0
sum = "00"
2da vuelta x=1
sum = "001"
3ra vuelta x=2
sum = "0012"
4ta vuelta x=3
sum = "00123"

"""




