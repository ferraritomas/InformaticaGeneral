'''
Recibe la lista por parámetro y retorna una tupla con dos elementos:
<el mes> donde se produce la máxima cantidad de hallazgos positivos al virus (en cualquier ciudad) y
<la edad promedio> de las personas para dicho mes analizado
>>>(5,37.0)

'''

def maxMesypromEdad(lst_contagios):
    lst_mes = []
    lst_mes_sin_repetir = []
    for i in range(len(lst_contagios)):
        lst_contagios[i][3] = (int(lst_contagios[i][3])//100)%100
        lst_mes.append(int(lst_contagios[i][3]))
    print(lst_contagios)
    print(lst_mes)
    
    for mes in lst_mes:
        if mes not in lst_mes_sin_repetir:
            lst_mes_sin_repetir.append(mes)
    print(lst_mes_sin_repetir)
    
    primero = True
    for i in range(len(lst_mes_sin_repetir)):
        cont_edad = 0
        cont_personas = 0
        for j in range(len(lst_contagios)):
            if int(lst_contagios[j][3]) == int(lst_mes_sin_repetir[i]):
                cont_edad += int(lst_contagios[j][1])
                cont_personas+=1
            
            if primero == True:
                mes_max_contagiados = lst_mes_sin_repetir[i]
                max_cant_personas = cont_personas
                promedio_edad = cont_edad/max_cant_personas
                primero = False
            
            else:
                if cont_personas > max_cant_personas:
                    max_cant_personas = cont_personas
                    mes_max_contagiados = lst_mes_sin_repetir[i]
                    promedio_edad = cont_edad/max_cant_personas
                    
    tupla = (mes_max_contagiados,promedio_edad)
    print(tupla)
                


def main():
    #[ID_persona , Edad , ID_ciudad , fecha_positivo(año-mes-dia)]
    lst = [["10","33","114","200518"],['11','31','223','200519'],['21','34','278','200819'],['11','81','223','100429']]
    maxMesypromEdad(lst)
main()