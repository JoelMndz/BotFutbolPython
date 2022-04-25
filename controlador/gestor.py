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
        webbrowser.open('manualUsuario.pdf')

    def abrirManualTecnico(self):
        """
        Funcion que abre el manual tecnico en el navegador
        """
        webbrowser.open('manualTecnico.pdf')


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
        if len(self.tokens) > 0:
            for i in self.tokens:
                html += i.html()
        else:
            html += """
                <h4>No hay datos</h4>
            """
        html += """
            </tbody>
            </table>
            </body>
            </html>
        """

        #Guardar los cambios
        archivo = open('tokens.html','w',encoding='utf-8')
        archivo.write(html)
        archivo.close()

        webbrowser.open('tokens.html')


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
        if len(self.errores) > 0:
            for i in self.errores:
                html += i.html()
        else:
            html += """
                        <h4>No hay datos</h4>
                    """
        html += """
                    </tbody>
                    </table>
                    </body>
                    </html>
                """

        # Guardar los cambios
        archivo = open('tokens.html', 'w', encoding='utf-8')
        archivo.write(html)
        archivo.close()

        webbrowser.open('tokens.html')

    def recibirIntruccion(self, mensaje):
        self.analizador.analizar(mensaje)
        # Pasar los tokens
        for i in self.analizador.tokens:
            self.tokens.append(i)
        # Pasar los errores
        for i in self.analizador.errores:
            self.errores.append(i)

        #Obtener la informacion
        info = self.analizador.obtenerInformacion()
        # Si es un partido
        print(info)
        if info['accion'] == 'RESULTADO':
            resultado = self.consulta.resultadoPartido(info)
            print(resultado)
        # Si es una jornada
        elif info['accion'] == 'JORNADA':
            resultado = self.consulta.resultadoJornada(info)
            for i in resultado:
                print(i)
        #Total de goles de una temporada
        elif info['accion'] == 'GOLES':
            resultado = self.consulta.resultadoTotal(info)
            print(resultado)
        #Tabla de posiciones
        elif info['accion'] == 'TABLA':
            resultado = self.consulta.resultadoTablaGeneral(info['temporada'])
            print(resultado)
        #Temporada de un equipo
        elif info['accion'] == 'PARTIDOS':
            resultado = self.consulta.resultadoTemporadaEquipo(info)
            print(resultado)
        #Top de equipos
        elif info['accion'] == 'TOP':
            resultado = self.consulta.resultadoTopTemporada(info)
            print(resultado)
        elif info['accion'] == 'ADIOS':
            print('ADIOS')




g = Gestor()
g.recibirIntruccion("ADIOS")