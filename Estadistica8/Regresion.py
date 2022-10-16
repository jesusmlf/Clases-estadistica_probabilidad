def pendiente(lista_x:list, lista_y:list):
    n = len(lista_x)

    suma_x = 0
    for i in lista_x:
        suma_x = suma_x + i
    
    suma_y = 0
    for i in lista_y:
        suma_y = suma_y + i
    
    lista_xy = []
    suma_xy = 0
    for i in range(0,n):
        lista_xy.append(lista_x[i]*lista_y[i])
        suma_xy = suma_xy + lista_xy[i]
    
    lista_xc = []
    suma_xc = 0
    for i in lista_x:
        lista_xc.append(i**2)
    
    for i in lista_xc:
        suma_xc = suma_xc + i
    
    sum_cuadrada_x = suma_x**2

    pendiente = ((n*suma_xy) - (suma_x*suma_y)) / ((n*suma_xc) - (sum_cuadrada_x))
    return pendiente
    
def ordenada_origen(lista_x:list,lista_y:list,pendiente:float):
    n = len(lista_x)
    suma_x = 0
    for i in lista_x:
        suma_x = suma_x + i
    
    suma_y = 0
    for i in lista_y:
        suma_y = suma_y + i
    
    ordenada = (suma_y - (pendiente*suma_x)) / n
    return ordenada