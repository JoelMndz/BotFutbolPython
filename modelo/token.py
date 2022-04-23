
class Token:
    def __init__(self, lexema, tipo, linea, columna):
        self.lexema = lexema
        self.tipo = tipo
        self.linea = linea
        self.columna = columna

    def __str__(self):
        return f'Lexema: {self.lexema}\nTipo: {self.tipo}\nLinea:{self.linea}\nColumna: {self.columna}'

    def html(self):
        return f"""
            <tr>
                <td>{self.lexema}</td>
                <td>{self.tipo}</td>
                <td>{self.linea}</td>
                <td>{self.columna}</td>
            </tr>    
        """