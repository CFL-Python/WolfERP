from tkinter import Tk, ttk, messagebox, END, PhotoImage, Canvas
from tkinter.colorchooser import askcolor
from turtle import bgcolor
from vTiempos import vTiempos

from vConfig import CentraPantalla, PreparaEstilos
import tkinter as tk
import mysql.connector


class vEstilo:
    def __init__(self, config, master):
        ancho, alto, titulo, bgroundcolor, cursor = config[:5]

        self.master = master
        
        self.master.resizable(0, 0)
        self.master.title(titulo)
        self.master.attributes('-alpha', 0.94)
        self.master['bg'] = bgroundcolor
        self.master['cursor'] = cursor

        self.master.geometry(CentraPantalla(self.master, ancho, alto))

        #self.PreparaEstilo()
        self.botonLogin = ttk.Button(self.master,command=self.ColorPicker)
        self.botonLogin.place(x=15, y=15, height=15, width=15)
        #self.PreparaClicker()

    
    def ColorPicker(self):
        colors = askcolor(title="Cambiar Color")
        print(colors)