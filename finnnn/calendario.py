import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkcalendar import *
#from registroPas import Registro
'''
v_calendario = Tk()
v_calendario.wm_minsize(800,600)
v_calendario.title("Calendario")
v_calendario.configure(bg="#A1CDEC")
'''
class Calendario(Frame):  # Herencia Frame <-- Ventana
    #r1 = Registro()
    def __init__(self, master=None):  # Contructor de Ventana
        super().__init__(master, width=405, height=300)  # Herencia constructor de Frame = master
        self.master = master  # declaracion de master = masterFrame
        self.pack()
        self.create_widgets()

#calendario iconname
    def extraccionF(self):
        fechaS = self.myCal.get_date()
        print(fechaS)
        selectFecha = Label(self, text=fechaS)
        selectFecha.place(x=50, y=260, width=80, height=25)
        #self.r1.cajaTxt_fechaIni = fechaS

    def create_widgets(self):
        frame1 = Frame(self, bg="#bfdaff")
        frame1.place(x=0, y=0, width=405, height=250)

        self.myCal = Calendar(frame1, setmode='day', date_pattern='dd/mm/yyyy')
        self.myCal.place(x=0, y=0, width=400, height=200)
        btnCal = Button(frame1, text="Seleccione la Fecha", command=self.extraccionF)
        btnCal.place(x=50, y=210, width=150, height=30)
        #fecha1 = self.extraccionF()

