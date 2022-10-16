def Pearson(lista_x:list,lista_y:list):
    from math import sqrt
    if len(lista_x) == len(lista_y):

        suma_x = 0
        for i in lista_x:
            suma_x = suma_x + i
        
        suma_y = 0
        for i in lista_y:
            suma_y = suma_y + i
        
        x_cuadrado = []
        for i in lista_x:
            x_cuadrado.append(i**2)

        suma_x_cuadrado = 0
        for i in x_cuadrado:
            suma_x_cuadrado = suma_x_cuadrado + i
        
        y_cuadrado = []
        for i in lista_y:
            y_cuadrado.append(i**2)

        suma_y_cuadrado = 0
        for i in y_cuadrado:
            suma_y_cuadrado = suma_y_cuadrado + i
        
        XY = []
        for i in range(0,len(lista_x)):
            XY.append( lista_x[i] * lista_y[i])
        
        suma_XY = 0
        for i in XY:
            suma_XY = suma_XY + i

        n = len(lista_x)

        numerador = (n * suma_XY) - (suma_x * suma_y)

        denom = sqrt(((n*suma_x_cuadrado)-(suma_x)**2)*((n*suma_y_cuadrado)-(suma_y)**2) )
        pearson = numerador / denom
        return pearson

    else:
        print("Las listas deben de ser del mismo tamaño")
    