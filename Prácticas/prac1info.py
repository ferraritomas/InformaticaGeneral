
#PRAC1 EJER2

def main():
    a = str(input('ingrese su nombre: '))
    b = str(input('ingrese su apellido: '))
    print('Hola, {} {}'.format(b,a))
    
main()

'''
#PRAC1 EJER 3

def main():
    a = int(input('ingrese lado 1: '))
    b = int(input('ingrese lado 2: '))
    p = (a*2)+(b*2)
    area = a*b
    print('perimetro: ',p)
    print('area: ',area)
    
main()
'''
'''
#prac1 ejer4
def main():
    n = float(input('ingrese numero: '))
    pe = n//1
    pf = (n-pe)
    print('parte entera: ',pe)
    print('parte fraccionaria: {:.3f}'.format(pf))
main()
'''
'''
#prac1 ejer5
def main():
    n = int(input('ingrese numero: '))
    d0 = n%10
    d1 = (n//10)%10
    d2 = (n//100)%10
    d3 = (n//1000)%10
    d4 = (n//10000)%10
    print('separacion en digitos: {}-{}-{}-{}-{}'.format((d4**2),(d3**2),(d2**2),(d1**2),(d0**2)))
main()
'''
'''
#prac1 ejer6
def main():
    b = int(input('ingrese base: '))
    h = int(input('ingrese altura: '))
    a = (b*h)/2
    hip = ((b**2)+(h**2))**0.5
    p = b + h + hip
    print('calculos para un triangulo de base {} y altura {}'.format(b,h))
    print('<<<Area={:.2f}>>> <<<Perimetro={:.2f}>>>'.format(a,p))
main()
'''
'''
#prac1 ejer7
def main():
    p = int(input('ingrese el primer numero: '))
    s = int(input('ingrese el segundo numero: '))
    u_p = p%10
    d_s = (s//10)%10
    n = str(d_s) + str(u_p)
    print('el numero resultante es: ',n)
main()
'''
'''
#PRAC1 EJER13 FALTA TERMINAR

def main():
    mm = int(input('ingrese el multiplicando: '))
    mp = int(input('ingrese el multiplicador: '))
    print('{:=10d}'.format(mm))
    print('x{:=9d}'.format(mp))
    print('-'*12)
    resultado = mm*mp
    print('{:=10d}'.format(resultado))
     
main()
'''

        
    


