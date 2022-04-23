
class Error:
    def __init__(self, descripcion, tipo, linea, columna):
        self.descripcion = descripcion
        self.tipo = tipo
        self.linea = linea
        self.columna = columna

    def __str__(self) -> str:
        return f'Descripcion: {self.descripcion}\nTipo: {self.tipo}\nLinea:{self.linea}\nColumna: {self.columna}'

    def html(self):
        return f"""
            <tr>
                <td>{self.descripcion}</td>
                <td>{self.tipo}</td>
                <td>{self.linea}</td>
                <td>{self.columna}</td>
            </tr>    
        """