
# @autor:
# Youtube: https://www.youtube.com/c/MagnoEfren

from tkinter import Tk, Button, Entry, Label, ttk, PhotoImage, Menu
from tkinter import StringVar, END, HORIZONTAL, Frame, Toplevel
import time
import conexion
from menu import *#Menu
from fichaAsistencia import CAsistencia


class Login(Frame):
    def __init__(self, master, *args):
        super().__init__(master, *args)

        self.user_marcar = "Administrador"
        self.contra_marcar = "Ingrese su contraseña"
        self.fila1 = ''
        self.fila2 = ''
        self.datos = conexion.Registro_datos()
        self.widgets()

        self.master = master  # declaracion de master = masterFrame
        self.pack()


    def fIngresar(self):
        self.master.destroy()
        log = Tk()
        log.wm_title("Ficha de Asistencia")
        log.iconbitmap('LOGOTVU.ico')
        log.geometry('1345x675+0+0')
        app = CAsistencia(log)
        app.mainloop()




    def salir(self):
        self.master.destroy()
        self.master.quit()


    def IrAlogin2(self):
        self.master.destroy()
        #main.mostrar_login()
        main.mostrar_login2()

    def widgets(self):
        Label(self.master, text='UNIVERSIDAD MAYOR DE', bg='#a2b6d0', fg='black', font=('Lucida Sans', 16, 'bold')).pack(pady=5)
        Label(self.master, text='SAN ANDRES', bg='#a2b6d0', fg='black',
              font=('Lucida Sans', 16, 'bold')).pack(pady=5)

        self.entry1 = Entry(self.master, font=('Comic Sans MS', 12), justify='center', fg='grey',
                            highlightbackground="#E65561",
                            highlightcolor="green2", highlightthickness=5)
        Label(self.master, bg='#aa9b92').pack(pady=90)
        #self.tvu = PhotoImage(file='LOGOTVU.png')



        Button(self.master, text='ADMINISTRADOR', bg='#063374', activebackground='gray', bd=5, fg='white',
               font=('Lucida Sans', 15, 'italic'), command=self.IrAlogin2).pack(pady=10)

        Button(self.master, text='ASISTENCIA DE PASANTES', bg='red2', activebackground='#063374', bd=5, fg='white',
               font=('Lucida Sans', 18, 'italic'), command=self.fIngresar).pack(pady=10)

        Button(self.master, text='Salir', bg='grey', activebackground='#063374', bd=5, fg='white',
               font=('Lucida Sans', 15, 'italic'), command=self.salir).pack(pady=10)

        Label(self.master, text='DESARROLLADORES:\n MIGUEL AGUIRRE, MAYKON QUISBERT, DIEGO GOROSTIAGA, VLADIMIR BILBAO ', bg='#a2b6d0', fg='black',
              font=('Lucida Sans', 6, 'bold')).place(x=0, y=625, width=350)


