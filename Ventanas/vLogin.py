from ttkwidgets.autocomplete import AutocompleteCombobox
from tkinter import IntVar, Tk, ttk, messagebox, END, PhotoImage, Canvas
from vEstilo import vEstilo
from vTiempos import vTiempos

from vConfig import CentraPantalla, PreparaEstilos
import tkinter as tk
import mysql.connector


class vLogin:
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

        self.mydb = mysql.connector.connect(
        database='wolferp',
        host="localhost",
        user="root",
        password='Takkanklok1')
        
        if not self.mydb.is_connected():
            messagebox.showinfo(message='No se ha podido conectar\12con la base de datos', title='Conexión errónea')
        else:
            cursor = self.mydb.cursor()
            select_stmt = ("SELECT usuario FROM Usuarios")

            cursor.execute(select_stmt)

        self.usuarios = []
        for usr in cursor:
            self.usuarios.append(usr[0])

        self.PreparaLogin()

    def PreparaLogin(self):   
        self.labelInicio = ttk.Label(self.master, text='Inicio de Sesión', style='Custom.TLabel')
        self.labelInicio.place(x=420, y=20)

        self.labelUsuario = ttk.Label(self.master, text='Usuario', style='Custom.TLabel')
        self.labelUsuario.place(x=420, y=90)

        self.entradaUser = AutocompleteCombobox(width=19,font=('Source Serif Pro ExtraLight',13),completevalues=self.usuarios)
        self.entradaUser.place(x=420, y=130)

        self.labelPass = ttk.Label(self.master, text='Contraseña', style='Custom.TLabel')
        self.labelPass.place(x=420, y=180)

        self.entradaPass = ttk.Entry(width=20, show='*',font=('Source Serif Pro ExtraLight', 13))
        self.entradaPass.place(x=420, y=220)

        self.botonLogin = ttk.Button(self.master, text="Login", style='Custom.TButton', command=self.LoggedIn)
        self.botonLogin.place(x=487, y=300, height=40, width=120)

        self.imgTuercas = PhotoImage(file='images/tuercas.png')
        self.tuercas = ttk.Button(self.master, style='Custom.TButton', image=self.imgTuercas, command=self.goEstilo)
        self.tuercas.place(x=420, y=300, height=40, width=40)

        self.labelCuadrado = ttk.Label(self.master, background='#00455F', border=0)
        self.labelCuadrado.place(x=0, y=0, width=350, height=700)

        self.logo = PhotoImage(file='images/lobo.png')
        self.labelLogo = ttk.Label(self.master, image = self.logo, border=0)
        self.labelLogo.place(x=120, y=170)

        self.logoCFL = PhotoImage(file='images/logocfl.png')
        self.labelLogoCFL = ttk.Label(self.master, image = self.logoCFL, border=0)
        self.labelLogoCFL.place(x=650, y=350)

        self.labelTitulo = ttk.Label(self.master, text='WolfERP', style='Title.TLabel')
        self.labelTitulo.place(x=75, y=110)

        '''self.checkRecuerda = ttk.Checkbutton(self.master, text ='Recuérdame',onvalue=1, offvalue=0,
                                              bg="white", selectcolor = "black").place(x=518, y = 255)'''
        self.check = ttk.Checkbutton(self.master, text = "Recordáme")
        self.check.place(x=518, y = 255)
                 
    def goEstilo(self):
        self.master.destroy()
        vEstilo(config,Tk())

    def PreparaClicker(self):
        self.logoCFL = PhotoImage(file='images/reloj.png')
        self.boton1 = ttk.Button(self.master, style='Custom.TButton', image=self.logoCFL)
        self.boton1.place(x=5, y=285, height=110, width=118)

        self.boton2 = ttk.Button(self.master, style='Custom.TButton')
        self.boton2.place(x=135, y=285, height=110, width=118)

        self.boton3 = ttk.Button(self.master, style='Custom.TButton')
        self.boton3.place(x=265, y=285, height=110, width=118)

        self.boton4 = ttk.Button(self.master, style='Custom.TButton')
        self.boton4.place(x=395, y=285, height=110, width=118)

        self.boton5 = ttk.Button(self.master, style='Custom.TButton')
        self.boton5.place(x=525, y=285, height=110, width=118)

        self.boton6 = ttk.Button(self.master, style='Custom.TButton')
        self.boton6.place(x=655, y=285, height=110, width=118)


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
                    vTiempos([1600, 400, 'Imputación Tiempo', '#FFFFFF', 'arrow'], Tk())

            
###########################################################################
###########################################################################
########################## EJECUCIÓN PROGRAMA #############################
###########################################################################
###########################################################################
# PRUEBAS MAIN:
ANCHO = 700
ALTO = 400
TITULO = 'WolfERP'

# Pruebas Dentro App.
#TITULO = 'Clicker'

# PRUEBAS IMPUTACIÓN TIEMPOS.
#TITULO = 'Tiempos'
#ANCHO = 1200
#ALTO = 400
BGCOLOR = '#FFFFFF'


# Cursores disponibles:
# arrow, circle, clock, cross, dotbox, exchange sizing, spider, spraycan, star, target
# fleur, heart, man, mouse, pirate, plus, shuttle, tcross, trek, watch
CURSOR = 'arrow'


# Preparo configuración para la ventana
config = [ANCHO, ALTO, TITULO, BGCOLOR, CURSOR]


# Creación de Ventana
miVentana = vLogin(config,Tk())
#miVentana = vEstilo(config,Tk())
tk.mainloop()