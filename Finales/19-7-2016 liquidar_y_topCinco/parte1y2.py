'''
#1.1)
def esPrimo(n):
    primo = True
    i = 2
    while i<n:
        if n%i==0:
            primo = False
        i+=1  
    return primo

print(esPrimo(17))
print(esPrimo(18))
'''
'''
#BIEN
#1.2)
def espalindromo(texto):
    palindromo = True
    for i in range(len(texto)):
        if(texto[-i-1] != texto[i]):
            palindromo = False
    return palindromo

print(espalindromo('neuquen'))
print(espalindromo('palabra'))
'''
'''
#BIEN    Error de ejecucion --> string no soporta item assignment
#2.1)
xs = ['Hola','Mundo',]
xs = "Hola"
xs = "Mundo"
xs[0] = 'x'
print(xs)
'''
'''
#BIEN --> False
#2.2)
def comparar(a,b,c):
    if((a and (b or c)) != ((a and b) or (a and c))):
        return True
    else:
        return False
print(comparar(1,2,3))
'''
'''
#BIEN 20-15
#2.3)
def f2(x):
    x=x+10
    return x
def f1():
    x=10
    print(str(f2(x))+"-",end="")
x=5
f1()
print ("{0:d}".format(f2(x)))
'''
'''
#BIEN  Error de ejecucion
#2.4)
xn = [1,2,3,4]
n = 1234
print((2 in xn) and (2 in n))
'''


