from datetime import date
def cargarArchivo():
    """
    Funcion que carga el archivo .csv y devuelve una lista con diccionario de datos
    """
    archivo = open('../Recursos/LaLigaBot-LFP.csv',encoding='utf-8')
    data = []
    #Leer el encabezado del archivo
    archivo.readline()
    for i in archivo.readlines():
        #Separar los datos de la linea por ,
        temp = i.strip().split(',')
        fecha = temp[0].split('/')
        temporada = temp[1].split('-')
        data.append({
            'fecha':date(year=int(fecha[2]),month=int(fecha[1]),day=int(fecha[0])),
            'temporada':(int(temporada[0]),int(temporada[1])),
            'jornada':int(temp[2]),
            'equipo1':temp[3],
            'equipo2':temp[4],
            'goles1': int(temp[5]),
            'goles2': int(temp[6]),
        })

    return data