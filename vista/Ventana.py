import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

from controlador.gestor import Gestor


class Ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.configurarVentana()
        self.cargarComponentes()
        self.gestor = Gestor()

    def configurarVentana(self):
        # Tamaño
        self.geometry('680x400')
        self.resizable(0, 0)
        self.configure(bg='#0489B1')
        self.title('La Liga Bot')

    def enviarMensaje(self):
        if len(self.mensaje.get()) > 0:
            texto = self.mensaje.get()+'\n'
            texto += '-'*120
            data = self.gestor.recibirInstruccion(self.mensaje.get())

            if 'respuesta' in data:
                if data['respuesta'] == 'ADIOS':
                    self.quit()
                texto += '\n' + data['respuesta']
            else:
                texto += '\nNo hay resultados'

            self.txtTexto['state'] = 'normal'
            self.txtTexto.delete('1.0',tk.END)
            self.txtTexto.insert('1.0', texto)
            self.txtTexto['state'] = 'disable'
        self.mensaje.set('')


    def cargarComponentes(self):
        self.txtTexto = tk.Text(self,height=20,width=75,font=("Helvetica", 10))
        self.txtTexto.grid(column=0,row=0,padx=15,pady=15,rowspan=20)
        self.txtTexto['state']='disable'

        self.btnReporteErrores = tk.Button(self,text="Reporte errores",width=13,font=("Helvetica", 10),command=lambda:self.gestor.reporteErrores())
        self.btnReporteErrores.grid(column=1,row=1)

        self.btnLimpiarErrores = tk.Button(self, text="Limpiar log errores", width=13, font=("Helvetica", 10),command=lambda:self.limpiarErrores())
        self.btnLimpiarErrores.grid(column=1, row=2)

        self.btnReporteTokens = tk.Button(self, text="Reporte de tokens", width=13, font=("Helvetica", 10),command=lambda:self.gestor.reporteTokens())
        self.btnReporteTokens.grid(column=1, row=3)

        self.btnLimpiarTokens = tk.Button(self, text="Limpiar log tokens", width=13, font=("Helvetica", 10),command=lambda:self.limpiarTokens())
        self.btnLimpiarTokens.grid(column=1, row=4)

        self.btnManualUsuario = tk.Button(self, text="Manual de usuario", width=13, font=("Helvetica", 10),command=lambda:self.gestor.abrirManualUsuario())
        self.btnManualUsuario.grid(column=1, row=5)

        self.btnManualTecnico = tk.Button(self, text="Manual técnico", width=13, font=("Helvetica", 10),command=lambda:self.gestor.abrirManualTecnico())
        self.btnManualTecnico.grid(column=1, row=6)

        self.mensaje = tk.StringVar()
        self.txtMensaje = ttk.Entry(self,textvariable=self.mensaje,font=("Helvetica", 11))
        self.txtMensaje.grid(column=0,row=20,padx=15,sticky=tk.EW)

        self.btnEnviar = tk.Button(self,text="Enviar", width=10,font=("Helvetica", 12),command=lambda:self.enviarMensaje())
        self.btnEnviar.grid(column=1,row=20,padx=5)

    def limpiarTokens(self):
        self.gestor.limpiarTokens()
        showinfo('Informacion','Lista de tokens vacía')

    def limpiarErrores(self):
        self.gestor.limpiarErrores()
        showinfo('Informacion', 'Lista de errores vacía')

v= Ventana()
v.mainloop()