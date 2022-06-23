from tkinter import Tk, ttk, messagebox, END, PhotoImage, Canvas
from vConfig import CentraPantalla, PreparaEstilos
import tkinter as tk
import mysql.connector


class vTiempos:
    def __init__(self, config, master):
        ancho, alto, titulo, bgroundcolor, cursor = config[:5]

        self.master = master
        
        self.master.resizable(0, 0)
        self.master.title(titulo)
        self.master.attributes('-alpha', 0.94)
        self.master['bg'] = bgroundcolor
        self.master['cursor'] = cursor

        self.master.geometry(CentraPantalla(self.master, ancho, alto))

        PreparaEstilos()

        self.PreparaTiempos()

    def PreparaTiempos(self):
        self.labelInicio = ttk.Label(self.master, text='Imputar Tiempo', style='TimesTitle.TLabel')
        self.labelInicio.place(x=30, y=20)

        self.labelEmpresa = ttk.Label(self.master, text='Empresa', style='Times.TLabel')
        self.labelEmpresa.place(x=30, y=85)

        self.entradaEmpresa = ttk.Entry(width=20,font=('Source Serif Pro ExtraLight',13))
        self.entradaEmpresa.place(x=30, y=120)

        self.labelTiempo = ttk.Label(self.master, text='Tiempo', style='Times.TLabel')
        self.labelTiempo.place(x=30, y=185)

        self.entradaTiempo = ttk.Entry(width=20, font=('Source Serif Pro ExtraLight', 13))
        self.entradaTiempo.place(x=30, y=220)

        self.labelComentario = ttk.Label(self.master, text='Comentario', style='Times.TLabel')
        self.labelComentario.place(x=330, y=90)

        self.text = tk.Text(self.master, height=8, width=50, border=0, background='#EEEEE5')
        self.text.place(x=330,y=130)
        self.scroll = tk.Scrollbar(self.master)
        self.text.configure(yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.text.yview)

        self.botonAñadir = ttk.Button(self.master, text="Añadir", style='Times.TButton', command=self.Imputar())
        self.botonAñadir.place(x=50, y=270, height=40, width=120)

        self.labelCuadrado = ttk.Label(self.master, background='#00455F', border=0)
        self.labelCuadrado.place(x=850, y=0, width=350, height=400)

    '''
    def Imputar(self):
        self.entradaEmpresa.get()
        self.entradaTiempo.get()

    def LoggedIn(self):
        user = self.entradaUser.get()
        passw = self.entradaPass.get()

        mydb = mysql.connector.connect(
        database='wolferp',
        host="localhost",
        user="root",
        password='Takkanklok1')
        
        if not mydb.is_connected():
            messagebox.showinfo(message='No se ha podido conectar\12con la base de datos', title='Conexión errónea')
        else:
            cursor = mydb.cursor()
            select_stmt = ("SELECT contraseña FROM Usuarios WHERE usuario = %s")

            cursor.execute(select_stmt, (user,))

            for password in cursor:
                if passw != password[0]:
                     messagebox.showinfo(message='La contraseña que has introducido\12no es correcta', title='Contraseña Incorrecta')
                else:
        self.master.destroy()
        vLogin([1600, 400, 'Clicker', '#FFFFFF', 'arrow'], Tk())
                    

    def BorraElementos(self):
        self.labelInicio.destroy()
        self.labelUsuario.destroy()
        self.entradaUser.destroy()
        self.labelTitulo.destroy()
        self.labelPass.destroy()
        self.entradaPass.destroy()
        self.botonLogin.destroy()
        self.labelCuadrado.destroy()
        self.labelLogo.destroy()
        self.labelLogoCFL.destroy()

    def Grabar(self):
        self.master.destroy()
        vLogin([800, 800, 'Tiempos', '#FFFFFF', 'arrow'], Tk())
        '''