import webbrowser
from controlador.consulta import Consulta
from modelo.analizadorLexico import AnalizadorLexico


class Gestor:
    def __init__(self):
        self.analizador = AnalizadorLexico()
        self.consulta = Consulta()
        self.tokens = []
        self.errores = []

    def limpiarTokens(self):
        """
        Funcion para limpiar la lista de tokens
        """
        self.tokens = []

    def limpiarErrores(self):
        """
        Funcion para limpiar la lista de errores
        """
        self.errores = []

    def abrirManualUsuario(self):
        """
        Funcion que abre el manual de usuario en el navegador
        """
        webbrowser.open('manual_usuario.pdf')

    def abrirManualTecnico(self):
        """
        Funcion que abre el manual tecnico en el navegador
        """
        webbrowser.open('manual_tecnico.pdf')


    def reporteTokens(self):
        """
        Funcion para hacer un reporte de los tokens
        """
        html = """
              <!DOCTYPE html>
              <html lang="es">
              <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
                <title>Reporte</title>
              </head>
              <body>
                <nav class="navbar navbar-light bg-light">
                  <div class="conatiner-fluid">
                    <h1 class="mx-2 display-6">Reporte de Tokens</h1>
                  </div>
                </nav>
                <div class="container">
                  
            """

        if len(self.tokens) > 0:
            html += """
                <table class="table mt-3">
                <thead>
                    <tr>
                      <th scope="col">Lexema</th>
                      <th scope="col">Tipo</th>
                      <th scope="col">Linea</th>
                      <th scope="col">Columna</th>
                    </tr>
                  </thead>
                  <tbody>
            """
            for i in self.tokens:
                html += i.html()
            html += """
                </tbody>
                </table>
            """
        else:
            html += """
                <h4>No hay datos</h4>
            """
        html += """
            </body>
            </html>
        """

        #Guardar los cambios
        archivo = open('temp.html','w',encoding='utf-8')
        archivo.write(html)
        archivo.close()

        webbrowser.open('temp.html')

    def reporteErrores(self):
        """
        Funcion para hacer un reporte de los errores
        """
        html = """
          <!DOCTYPE html>
          <html lang="es">
          <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
            <title>Reporte</title>
          </head>
          <body>
            <nav class="navbar navbar-light bg-light">
              <div class="conatiner-fluid">
                <h1 class="mx-2 display-6">Reporte de Errores</h1>
              </div>
            </nav>
            <div class="container">

        """

        if len(self.errores) > 0:
            html += """
                <table class="table mt-3">
                <thead>
                    <tr>
                      <th scope="col">Descripcion</th>
                      <th scope="col">Tipo</th>
                      <th scope="col">Linea</th>
                      <th scope="col">Columna</th>
                    </tr>
                  </thead>
                  <tbody>
            """
            for i in self.errores:
                html += i.html()
            html += """
                </tbody>
                </table>
            """
        else:
            html += """
                        <h4>No hay datos</h4>
                    """
        html += """
            </body>
            </html>
        """

        # Guardar los cambios
        archivo = open('temp.html', 'w', encoding='utf-8')
        archivo.write(html)
        archivo.close()

        webbrowser.open('temp.html')

    def reporteJornada(self,titulo,resultado:list,nombre='jornada'):
        """
        Funcion para hacer un reporte
        """
        html = f"""
          <!DOCTYPE html>
          <html lang="es">
          <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
            <title>Reporte</title>
          </head>
          <body>
            <nav class="navbar navbar-light bg-light">
              <div class="conatiner-fluid">
                <h1 class="mx-2 display-6">{titulo}</h1>
              </div>
            </nav>
            <div class="container">

        """
        html += """
                    <table class="table mt-3">
                    <thead>
                        <tr>
                          <th scope="col">Fecha</th>
                          <th scope="col">Equipo 1</th>
                          <th scope="col">Equipo 2</th>
                          <th scope="col">Goles 1</th>
                          <th scope="col">Goles 2</th>      
                          <th scope="col">Resultado</th>                    
                        </tr>
                      </thead>
                      <tbody>
                """
        if len(resultado) > 0:
            for i in resultado:
                html += f"""
                    <tr>
                        <td>{i['fecha']}</td>
                        <td>{i['equipo1']}</td>
                        <td>{i['equipo2']}</td>
                        <td>{i['goles1']}</td>
                        <td>{i['goles2']}</td>
                        <td>{i['resultado']}</td>
                    </tr>
                """
            html += """
                </tbody>
                </table>
            """
        else:
            html += """
                        <h4>No hay datos</h4>
                    """
        html += """
                    </body>
                    </html>
                """

        # Guardar los cambios
        archivo = open(f'{nombre}.html', 'w', encoding='utf-8')
        archivo.write(html)
        archivo.close()

        webbrowser.open(f'{nombre}.html')

    def reporteTabla(self,titulo,resultado:list,nombre='temporada'):
        """
        Funcion para hacer un reporte
        """
        html = f"""
          <!DOCTYPE html>
          <html lang="es">
          <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
            <title>Reporte</title>
          </head>
          <body>
            <nav class="navbar navbar-light bg-light">
              <div class="conatiner-fluid">
                <h1 class="mx-2 display-6">{titulo}</h1>
              </div>
            </nav>
            <div class="container">

        """

        if len(resultado) > 0:
            html += """
                <table class="table mt-3">
                <thead>
                    <tr>
                      <th scope="col">Equipo</th>
                      <th scope="col">Puntos</th>                      
                    </tr>
                  </thead>
                  <tbody>
            """
            for i in resultado:
                html += f"""
                    <tr>
                        <td>{i[0]}</td>
                        <td>{i[1]}</td>
                    </tr>
                """
            html += """
                </tbody>
                </table>
            """
        else:
            html += """
                <h4>No hay datos</h4>
            """
        html += """
            </body>
            </html>
        """

        # Guardar los cambios
        archivo = open(f'{nombre}.html', 'w', encoding='utf-8')
        archivo.write(html)
        archivo.close()

        webbrowser.open(f'{nombre}.html')

    def reporteEquipo(self,titulo,resultado:list,nombre='partidos'):
        """
        Funcion para hacer un reporte
        """
        html = f"""
          <!DOCTYPE html>
          <html lang="es">
          <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
            <title>Reporte</title>
          </head>
          <body>
            <nav class="navbar navbar-light bg-light">
              <div class="conatiner-fluid">
                <h1 class="mx-2 display-6">{titulo}</h1>
              </div>
            </nav>
            <div class="container">

        """

        if len(resultado) > 0:
            html += """
                <table class="table mt-3">
                <thead>
                    <tr>
                      <th scope="col">Fecha</th>
                      <th scope="col">Equipo 1</th>
                      <th scope="col">Equipo 2</th>
                      <th scope="col">Goles 1</th>
                      <th scope="col">Goles 2</th>     
                      <th scope="col">Jornada</th> 
                      <th scope="col">Resultado</th>                    
                    </tr>
                  </thead>
                  <tbody>
            """
            for i in resultado:
                html += f"""
                    <tr>
                        <td>{i['fecha']}</td>
                        <td>{i['equipo1']}</td>
                        <td>{i['equipo2']}</td>
                        <td>{i['goles1']}</td>
                        <td>{i['goles2']}</td>
                        <td>{i['jornada']}</td>
                        <td>{i['resultado']}</td>
                    </tr>
                """
            html += """
                </tbody>
                </table>
            """
        else:
            html += """
                <h4>No hay datos</h4>
            """
        html += """
            </body>
            </html>
        """

        # Guardar los cambios
        archivo = open(f'{nombre}.html', 'w', encoding='utf-8')
        archivo.write(html)
        archivo.close()

        webbrowser.open(f'{nombre}.html')

    def recibirInstruccion(self, mensaje):
        data = {}
        self.analizador.analizar(mensaje)
        # Pasar los tokens
        for i in self.analizador.tokens:
            self.tokens.append(i)
        # Pasar los errores
        for i in self.analizador.errores:
            self.errores.append(i)

        #Obtener la informacion
        info = self.analizador.obtenerInformacion()
        if 'accion' not in info:
            return {}
        # Si es un partido
        if info['accion'] == 'RESULTADO':
            resultado = self.consulta.resultadoPartido(info)
            #Si no hay resultados
            if len(resultado) == 0:
                return {}
            data['respuesta'] = f'El resultado de este partido fue: {info["equipo1"]} {resultado["goles1"]} - {info["equipo2"]} {resultado["goles2"]}'

        # Si es una jornada
        elif info['accion'] == 'JORNADA':
            resultado = self.consulta.resultadoJornada(info)
            titulo = f'Jornada {info["numero"]} temporada <{info["temporada"][0]}-{info["temporada"][1]}>'
            if '-f' not in info:
                self.reporteJornada(titulo, resultado)
            else:
                self.reporteJornada(titulo, resultado, info['-f'])
            data['respuesta'] = f'Generando archivo de resultados jornada {info["numero"]} temporada {info["temporada"][0]}-{info["temporada"][1]}'

        #Total de goles de una temporada
        elif info['accion'] == 'GOLES':
            resultado = self.consulta.resultadoTotal(info)
            data['respuesta'] = f'Los goles anotados por el {info["equipo"]} en {info["condicion"].lower()} en la temporada {info["temporada"][0]}-{info["temporada"][1]} fueron {resultado}'

        #Tabla de posiciones
        elif info['accion'] == 'TABLA':
            resultado = self.consulta.resultadoTablaGeneral(info['temporada'])
            titulo = f'Temporada <{info["temporada"][0]}-{info["temporada"][1]}>'
            if '-f' not in info:
                self.reporteTabla(titulo, resultado)
            else:
                self.reporteTabla(titulo, resultado, info['-f'])
            data['respuesta'] = f'Generando archivo de clasificación de temporada {info["temporada"][0]}-{info["temporada"][1]}'

        #Temporada de un equipo
        elif info['accion'] == 'PARTIDOS':
            resultado = self.consulta.resultadoTemporadaEquipo(info)
            # Si no hay resultados
            if len(resultado) == 0:
                return {}
            titulo = f'Temporada <{info["temporada"][0]}-{info["temporada"][1]}> de {info["equipo"]}'
            if '-f' not in info:
                self.reporteEquipo(titulo,resultado)
            else:
                self.reporteEquipo(titulo, resultado,info['-f'])
            data['respuesta'] = f'Generando archivo de resultados de {info["temporada"][0]}-{info["temporada"][1]} del {info["equipo"]}'

        #Top de equipos
        elif info['accion'] == 'TOP':
            resultado = self.consulta.resultadoTopTemporada(info)
            if len(resultado) == 0:
                return {}
            texto = f'El top {info["condicion"].lower()} de la temporada {info["temporada"][0]}-{info["temporada"][1]} fue:'
            for i in range(len(resultado)):
                texto += f'\n{i+1}. {resultado[i][0]} ({resultado[i][1]} pts)'
            data['respuesta'] = texto

        elif info['accion'] == 'ADIOS':
            data['respuesta'] = 'ADIOS'

        return data