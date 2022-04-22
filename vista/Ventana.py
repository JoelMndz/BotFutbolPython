import tkinter as tk
from tkinter import END, ttk
from tkinter.messagebox import showerror

class Ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.configurar_ventana()
        self.cargar_componentes()

    def configurar_ventana(self):
        # Tamaño
        self.geometry('720x480')
        self.resizable(0, 0)
        self.configure(bg='#0489B1')
        self.title('La Liga Bot')

    def cargar_componentes(self):
        print('OK')


v= Ventana()
v.mainloop()