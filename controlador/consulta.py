from controlador.archivo import cargarArchivo


class Consulta:
    def __init__(self):
        self.data = cargarArchivo()

    #AQUI DEFININEMOS LAS FUNCIONES PARA CONSULTAR DATOS DEL .CSV
