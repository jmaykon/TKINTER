from tkinter import *

import main


from registroPas import *#Registro
from reporte import Reporte

class Menu(Frame):  # Herencia Frame <-- Ventana
    print("holaM")
    def __init__(self, master=None):  # Contructor de Ventana
        super().__init__(master, width=380, height=420)  # Herencia constructor de Frame = master
        self.master = master  # declaracion de master = masterFrame
        self.pack()
        self.create_widgets()


    def create_widgets(self):
        frame1 = Frame(self, )  # Frame esta dentro ventana, existe solo en el metodo(No es mienbro de la clase )
        frame1.place(x=0, y=0, width=370, height=410)

        self.um = PhotoImage(file='fondoAdmin.png')  #FONDO DENTRO DEL FRAME
        Label(frame1, image=self.um).place(x=0, y=-10)          #LA POCISION DE LA IAMGEN DENTOR DEL FRAME

        self.titulo = Label(frame1, text="OPCIONES",font = 15, fg="white", bg="#063374")
        self.titulo.place(x=150, y=110)


        self.btnRegistro = Button(frame1, text="Registro Pasante", command=self.fRegistro, bg="red2", fg="white")  # fNuevo
        self.btnRegistro.place(x=120, y=180, width=150, height=30)

        self.btnReporte = Button(frame1, text="Reporte", command=self.fReporte, bg="blue", fg="white")  # fNuevo
        self.btnReporte.place(x=120, y=240, width=150, height=30)

        self.btnAtras = Button(frame1, text="<-- Atras", command=self.fAtras, bg="gray", fg="white")
        self.btnAtras.place(x=0, y=0)

    def fAtras(self):
        self.master.destroy()
        #main.mostrar_login()
        main.mostrar_login2()
    def fRegistro(self):
        self.master.destroy()
        reg = Tk()
        reg.wm_title("Registro de Pasantes")
        app = Registro(reg)
        app.mainloop()
    def fReporte(self):
        self.master.destroy()
        root = Tk()
        root.wm_title("Reporte")
        app = Reporte(root)
        app.mainloop()


