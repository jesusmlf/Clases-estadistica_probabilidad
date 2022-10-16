def almacenarDatos(ruta):

    archivo = open(ruta,'r')
    data = []
    for i in archivo:
        data.append(float(i))
    archivo.close()

    return data

def contardatos(data):
    

def run():
    ruta = '/home/jesus/clases/Estadistica1/medidas.csv'
    data = almacenarDatos(ruta)
    print(data)

if __name__ == '__main__':
    run()