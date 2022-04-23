from modelo.error import Error
from modelo.token import Token


class AnalizadorLexico:
    def __init__(self):
        self.tokens = []
        self.errores = []

    def analizar(self, cadena: str):
        #Boorrar informacion
        self.tokens = []
        self.errores = []

        # variables
        linea = 1
        columna = 0
        indice = 0
        buffer = ''
        estado = 'PALABRA RESERVADA'
        reservadas = ['RESULTADO','TEMPORADA','VS','JORNADA','-f','GOLES','TABLA','PARTIDOS','-ji','-jf','TOP','-n','ADIOS','SUPERIOR','INFERIOR']
        cadena += '$'
        #Iterar sobre cada caracter
        for caracter in cadena.strip():
            if estado == 'SIGNO':
                if caracter == '<':
                    buffer = caracter
                    self.tokens.append(Token(buffer, 'MENOR QUE', linea, columna))
                    buffer = ''
                    estado = 'ANIO'
                    columna += 1
                elif caracter == ' ':
                    columna += 1
                elif caracter == '"' or caracter == '“':
                    buffer = ''
                    estado = 'CADENA'
                    columna += 1
                elif caracter.isdigit():
                    buffer += caracter
                    estado = 'ENTERO'
                    columna += 1
                elif caracter.isalpha() or caracter == '-':
                    buffer += caracter
                    estado = 'PALABRA RESERVADA'
                    columna += 1
                elif caracter != '$':
                    self.errores.append(Error(caracter + " no reconocido como token.", 'LEXICO', linea, columna))
                    buffer = ''
                    columna += 1
            elif estado == 'PALABRA RESERVADA':
                if caracter == ' ' or caracter == '$':
                    if buffer in reservadas:
                        self.tokens.append(Token(buffer, 'RESERVADA', linea, columna))
                        buffer = ''
                        estado = 'SIGNO'
                        columna += 1
                    else:
                        self.tokens.append(Token(buffer, 'CADENA', linea, columna))
                        buffer = ''
                        estado = 'SIGNO'
                        columna += 1
                else:
                    buffer += caracter
                    columna += 1
            elif estado == 'CADENA':
                if caracter == '"' or caracter == '”':
                    self.tokens.append(Token(buffer, 'CADENA', linea, columna))
                    buffer = ''
                    estado = 'SIGNO'
                    columna += 1
                else:
                    buffer += caracter
                    columna += 1
            elif estado == 'ENTERO':
                if caracter.isdigit():
                    buffer += caracter
                    self.tokens.append(Token(buffer, 'ENTERO', linea, columna))
                    buffer = ''
                    estado = 'SIGNO'
                    columna += 1
                elif caracter == ' ' or caracter == '$':
                    self.tokens.append(Token(buffer, 'ENTERO', linea, columna))
                    buffer = ''
                    estado = 'SIGNO'
                    columna += 1
                else:
                    self.errores.append(Error(caracter + " no reconocido como token.", 'LEXICO', linea, columna))
                    buffer = ''
                    columna += 1
                    estado = 'SIGNO'
            elif estado == 'ANIO':
                if caracter == '-' and len(buffer)==4 and buffer.isnumeric():
                    self.tokens.append(Token(buffer, 'ANIO', linea, columna))
                    buffer = ''
                    columna += 1
                    self.tokens.append(Token(caracter, 'GUION', linea, columna))
                    columna += 1
                elif caracter == '>' and len(buffer)==4 and buffer.isnumeric():
                    self.tokens.append(Token(buffer, 'ANIO', linea, columna))
                    buffer = ''
                    columna += 1
                    self.tokens.append(Token(caracter, 'MAYOR QUE', linea, columna))
                    columna += 1
                    estado = 'SIGNO'
                elif caracter.isdigit():
                    buffer += caracter
                    columna += 1
                else:
                    buffer += caracter
                    self.errores.append(Error(caracter + " no reconocido como token.", 'LEXICO', linea, columna))
                    buffer = ''
                    columna += 1
                    estado = 'SIGNO'

    def obtenerInformacion(self):
        data = {}
        if len(self.tokens) > 0:
            if self.tokens[0].lexema == 'RESULTADO':
                data['accion'] = 'RESULTADO'
                data['equipo1'] = self.tokens[1].lexema
                data['equipo2'] = self.tokens[3].lexema
                data['temporada'] = (int(self.tokens[6].lexema),int(self.tokens[8].lexema))
            elif self.tokens[0].lexema == 'JORNADA':
                data['accion'] = 'JORNADA'
                data['numero'] = int(self.tokens[1].lexema)
                data['temporada'] = self.tokens[2].lexema
                data['temporada'] = (int(self.tokens[4].lexema), int(self.tokens[6].lexema))
                if len(self.tokens) == 10:
                    if self.tokens[8].lexema == '-f':
                        data['-f'] = self.tokens[-1].lexema
            elif self.tokens[0].lexema == 'GOLES':
                data['accion'] = 'GOLES'
                if self.tokens[1].lexema in ['LOCAL','VISITANTE','TOTAL']:
                    data['condicion'] = self.tokens[1].lexema
                    data['equipo'] = self.tokens[2].lexema
                    data['temporada'] = (int(self.tokens[5].lexema),int(self.tokens[7].lexema))
                #else:
                   # raise Exception('Formato incorrecto!')
            elif self.tokens[0].lexema == 'TABLA':
                data['accion'] = self.tokens[0].lexema
                data['temporada'] = (int(self.tokens[3].lexema), int(self.tokens[5].lexema))
                if len(self.tokens) == 9:
                    if self.tokens[7].lexema == '-f':
                        data['-f'] = self.tokens[-1].lexema
            elif self.tokens[0].lexema == 'PARTIDOS':
                data['accion'] = self.tokens[0].lexema
                data['equipo'] = self.tokens[1].lexema
                data['temporada'] = (int(self.tokens[4].lexema), int(self.tokens[6].lexema))
                if len(self.tokens) >= 10:
                    for i in range(8,len(self.tokens),2):
                        if self.tokens[i].lexema == '-f':
                            data['-f'] =  self.tokens[i+1].lexema
                        elif self.tokens[i].lexema == '-jf' or self.tokens[i].lexema == '-ji':
                            data[self.tokens[i].lexema] = int(self.tokens[i+1].lexema)
            elif self.tokens[0].lexema == 'TOP':
                data['accion'] = self.tokens[0].lexema
                if self.tokens[1].leADIOSxema in ['SUPERIOR','INFERIOR']:
                    data['condicion'] = self.tokens[1].lexema
                    data['temporada'] = (int(self.tokens[4].lexema), int(self.tokens[6].lexema))
                    if len(self.tokens) == 10:
                        if self.tokens[8].lexema == '-n':
                            data['-n'] = int(self.tokens[9].lexema)
                else:
                    raise Exception('Formato incorrecto!')
            elif self.tokens[0].lexema == 'ADIOS':
                data['accion'] = self.tokens[0].lexema
            #else:
                #raise Exception('Formato incorrecto!')
        return data
