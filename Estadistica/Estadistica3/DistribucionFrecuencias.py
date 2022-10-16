def NumeroDatos(data:list):
    #Esta función devuelve el numero de datos contenidos en "data".
    return len(data)

def Rango(ValorMaximo,ValorMinimo,Decimales = 3):
    #Esta funcion devuelve el rango, recibe como parametros el valor maximo y minimo del
    #conjunto de datos.

    #La funcion redondea los limites de clase a 3 decimales, para cambiar el numero de decimales
    #a los que se redondea hay que cambiar el valor de Decimales a la cantidad de decimales que
    #deseamos redondear.
    return (round(ValorMaximo-ValorMinimo,Decimales))

def NumeroClases(NumeroDatos,RedondearArriba = True):
    from math import log,ceil,floor
    #Esta funcion devuelve el numero de clases en el que se agruparan los datos, recibe
    #como parametros el numero de datos.

    #La funcion por defecto redondea el numero de clases hacia arriba.
    #Para que la función redondee hacia el entero inferior, hay que cambiar el valor de
    #RedondearArriba = False

    k = 1 + 3.3 * log(NumeroDatos,10)

    if RedondearArriba == True:
        k = ceil(k)
    else:
        k = floor(k)
    return k

def IntervaloClases(Rango, NumeroClases):
    #Esta funcion devuelve el intervalo de clases, recibe por parámetros el Rango y el
    #numero de clases.
    return Rango/NumeroClases

def Limites(IntervaloClase,ValorMinimo,NumeroClases,Decimales = 3):
    #Esta funcion devuelve una lista que contiene los Limites de clase.

    #La funcion redondea los limites de clase a 3 decimales, para cambiar el numero de decimales
    #a los que se redondea hay que cambiar el valor de Decimales a la cantidad de decimales que
    #deseamos redondear.

    limites = []
    for i in range(0,NumeroClases+1):
        if i == 0:
            limites.append(ValorMinimo)
        else:
            limites.append(round(limites[i-1]+IntervaloClase,Decimales))
    return limites

def Contar(Data:list,Limites,IntervaloClase, ValorMaximo):
    #Esta funcion devuelve una lista con las frecuencias de cada clase.
    contador = 0
    frecuencia = []

    for i in Limites:
        if i == ValorMaximo:
            break
    
        for j in Data:
            if j >= i and j < i + IntervaloClase:
                contador = contador + 1

        frecuencia.append(contador)
        contador = 0
    return frecuencia

def MarcaClase(Limites:list):
    marca_clase = []
    for i in range(0,len(Limites)):
        if i == len(Limites)-1:
            break
        marca_clase.append((Limites[i]+Limites[i+1])/2)
    return marca_clase

def Intervalos(Limites:list):
    #Esta funcion devuelve una lista de strings. 
    #Cada indice de la lista contiene el intervalo inferior y superior de cada clase.

    intervalos = []
    for i in range(0,len(Limites)):
        if i == len(Limites) - 1:
            break
        else:
            intervalos.append(str(Limites[i]) + '-' + str(Limites[i+1]))
    return intervalos

def FrecuenciaRelativa(Frecuencia:list,NumeroDatos:int,Porcentaje=True):
    #Esta funcion devuelve una lista con la frecuencia relativa de cada clases.
    #Por defecto devuelte los valores en forma de porcentaje, para que los devuelva en forma decimal, hay que cambiar
    #el valor de Porcentaje = False
    frecuencia_relativa = []
    for i in Frecuencia:
        if Porcentaje == True:
            frecuencia_relativa.append(round((i/NumeroDatos)*100,2))
        else:
            frecuencia_relativa.append((i/NumeroDatos ))

    return frecuencia_relativa

def FrecuenciaAcumulada(Frecuencia:list):
    frecuencia_acumulada = []
    suma = 0
    for i in Frecuencia:
        suma = suma + i
        frecuencia_acumulada.append(suma)
    return frecuencia_acumulada

def FrecuenciaRelativaAcumulada(FrecuenciaAcumulada:list,NumeroDatos:int):
    F_relativa_acumulada = []
    for i in FrecuenciaAcumulada:
        F_relativa_acumulada.append((i/NumeroDatos)*100)
    return F_relativa_acumulada
