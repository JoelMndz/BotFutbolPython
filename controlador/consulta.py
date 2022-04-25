from controlador.archivo import cargarArchivo

class Consulta:
    def __init__(self):
        self.data = cargarArchivo()

    def resultadoPartido(self, filtro:dict):
        """
        Funcion para obtener el resultado de un partido
        :param filtro: Diccionario con los datos que se quieren filtrar
        :return: Un diccionario con los goles
        """
        for i in self.data:
            if (i['equipo1'].upper() == filtro['equipo1'].upper() and
                i['equipo2'].upper() == filtro['equipo2'].upper() and
                i['temporada'] == filtro['temporada']):
                return {'gole1':i['goles1'], 'goles2':i['goles2']}
        return {}

    def resultadoJornada(self, filtro:dict):
        """
        Funcion para obtener los partidos de una jornada
        :param filtro: Diccionario con los datos que se quieren filtrar
        :return: Lista con los partidos
        """
        partidos = []
        for i in self.data:
            if (i['jornada'] == filtro['numero'] and
                i['temporada'] == filtro['temporada']):
                #Agregar el resultaod final
                if i['goles1'] == i['goles2']:
                    i['resultado'] = 'Empate'
                elif i['goles1'] > i['goles2']:
                    i['resultado'] = f'Gano {i["equipo1"]}'
                else:
                    i['resultado'] = f'Gano {i["equipo2"]}'
                partidos.append(i)
        return partidos

    def resultadoTotal(self, filtro:dict):
        """
        Funcion para obtener los goles de una temporada
        :param filtro: Diccionario con los datos que se quiere filtrar
        :return: Lista con los partidos
        """
        goles = 0
        for i in self.data:
            if (filtro['condicion'] == 'LOCAL' and
                i['equipo1'] == filtro['equipo'] and
                i['temporada'] == filtro['temporada']):
                goles += i['goles1']
            elif (filtro['condicion'] == 'VISITANTE' and
                i['equipo2'] == filtro['equipo'] and
                i['temporada'] == filtro['temporada']):
                goles += i['goles2']
            elif (filtro['condicion'] == 'TOTAL' and
                  i['temporada'] == filtro['temporada'] and
                  (i['equipo2'] == filtro['equipo'] or
                   i['equipo1'] == filtro['equipo'])):
                if i['equipo1'] == filtro['equipo']:
                    goles += i['goles1']
                else:
                    goles += i['goles2']
        return goles

    def resultadoTablaGeneral(self,temporada:tuple):

        # Lista para almacenar los partidos de la temporada
        partidos = []
        # Primero obtenemos los equipos de la serie
        equipos = []
        # Lista para guardar los puntos del cada equipo
        puntos = []
        # Lista para ubicar los quipos y sus puntis
        tabla = []
        #Obtener los partidos de la temporada
        for i in self.data:
            if i['temporada'] == temporada:
                partidos.append(i)

        #Obtener los equipos de la temporada
        for i in partidos:
            if i['equipo1'] not in equipos:
                equipos.append(i['equipo1'])
                puntos.append(0)
            if i['equipo2'] not in equipos:
                equipos.append(i['equipo2'])
                puntos.append(0)

        #Calcular los puntos de cada equipo
        for i in partidos:
            #Si el equipo1 gano
            if i['goles1'] > i['goles2']:
                indice = equipos.index(i['equipo1'])
                puntos[indice] += 3
            if i['goles2'] > i['goles1']:
                indice = equipos.index(i['equipo2'])
                puntos[indice] += 3
            #Si huvo empate
            else:
                indice = equipos.index(i['equipo1'])
                puntos[indice] += 3
                indice = equipos.index(i['equipo2'])
                puntos[indice] += 3

        #Pasar los datos a la tabla
        for i in range(len(equipos)):
            tabla.append((equipos[i],puntos[i]))

        #Ordenar tabla por los puntos
        for i in range(len(tabla)-1):
            indice = i
            maximo = tabla[i][1]
            for j in range(i+1,len(tabla)):
                if maximo < tabla[j][1]:
                    indice = j
                    maximo = tabla[j][1]
            if i != indice:
                aux = tabla[i]
                tabla[i] = tabla[indice]
                tabla[indice] = aux

        return tabla

    def resultadoTopTemporada(self,filtro:dict):
        # obtener n ó dejar su valor por defecto
        n = 5
        if '-n' in filtro:
            if filtro['-n'] > 0:
                n = filtro['-n']
        #Obtener la tabla de la temporada
        tabla = self.resultadoTablaGeneral(filtro['temporada'])
        if n >= len(tabla):
            return tabla
        top = []
        if filtro['condicion'] == 'SUPERIOR':
            for i in range(n):
                top.append(tabla[i])
        if filtro['condicion'] == 'INFERIOR':
            for i in range(len(tabla)-1,len(tabla)-n-1,-1):
                top.append(tabla[i])
        return top


    def resultadoTemporadaEquipo(self, filtro:dict):
        partidos = []
        #Obtener la jornada inicial y final
        jornadaI = -1
        jornadaF = -1
        if '-ji' in filtro:
            jornadaI = filtro['-ji']
        if '-jf' in filtro:
            jornadaF = filtro['-jf']

        #Resultados de un equipo
        for i in self.data:
            if jornadaI != -1 and jornadaF != -1:
                if (i['temporada'] == filtro['temporada'] and
                    i['jornada'] >= jornadaI and
                    i['jornada'] <= jornadaF and
                    (i['equipo2'] == filtro['equipo'] or
                        i['equipo1'] == filtro['equipo'])):
                    partidos.append(i)
            elif jornadaI != -1:
                if (i['temporada'] == filtro['temporada'] and
                    i['jornada'] >= jornadaI and
                    (i['equipo2'] == filtro['equipo'] or
                        i['equipo1'] == filtro['equipo'])):
                    partidos.append(i)
            elif jornadaF != -1:
                if (i['temporada'] == filtro['temporada'] and
                    i['jornada'] <= jornadaF and
                    (i['equipo2'] == filtro['equipo'] or
                        i['equipo1'] == filtro['equipo'])):
                    partidos.append(i)
            else:
                if (i['temporada'] == filtro['temporada'] and
                    (i['equipo2'] == filtro['equipo'] or
                        i['equipo1'] == filtro['equipo'])):
                    partidos.append(i)
        return partidos

