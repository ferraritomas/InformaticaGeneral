def topCinco():
    d_vt={1:["Enero",210],8:["Febrero",32],3:["Enero",140],8:["Junio",180]}
    d_v={1:["Juan",91,12500.00],6:["Carlos",60,10000.00],8:["Marcos",78,7600.00],3:["Alberto",60,11000.00],7:["Luis",81,6000.00]}
    d_c={1:1250.0,6:0,8:760.0,3:1100.0,7:0}
    l=[]
    for clave in d_v:
        l.append([clave,d_v[clave][0],d_c[clave]])
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            if l[i][2]<l[j][2]:
                l[i],l[j]=l[j],l[i]
    for k in range(len(l)):
        print(l[k])

def liquidar():
    d_vt={1:["Enero",210],8:["Febrero",32],3:["Enero",140],8:["Junio",180]}
    #d_l={1:1250.0,6:0,8:760.0,3:1100.0,7:0} asi tiene q quedar
    d_v={1:["Juan",91,12500.00],6:["Carlos",60,10000.00],8:["Marcos",78,7600.00],3:["Alberto",60,11000.00],7:["Luis",81,6000.00]}
    d_l={}
    for clave in d_v:
        if clave not in d_vt:
            comision=0
        elif d_vt[clave][1]<d_v[clave][1]*0.8:
            comision=0
        elif d_vt[clave][1]>d_v[clave][1]*0.8 and d_vt[clave][1]<d_v[clave][1]:
            comision=d_v[clave][2]*0.03
        elif d_vt[clave][1]>d_v[clave][1]:
            comision=d_v[clave][2]*0.1
        d_l[clave]=comision
    print(d_l)

def main():
    liquidar()
    topCinco()
    
main()