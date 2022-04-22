
class AnalizadorLexico:
    def __init__(self):
        self.tokens = []
        self.errores = []

    def analizar(self, cadena: str):
        # Limpiar las listas
        self.tokens = []
        self.errores = []

        # variables
        linea = 1
        columna = 0
        indice = 0
        buffer = ''
        estado = 'TITULO'

