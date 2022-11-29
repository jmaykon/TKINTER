#from menu import *
from tkinter import Tk, PhotoImage, Label

import login
import login2

import menu


def mostrar_login():
    ventana = Tk()
    ventana.config(bg='gray63')
    ventana.geometry('350x650+500+50')
    ventana.overrideredirect(1)
    ventana.resizable(0, 0)

    imagenL = PhotoImage(file="logofinal.png")
    lblImagenL = Label(ventana, image=imagenL).place(x=-60, y=-5)


    app = login.Login(ventana)
    app.mainloop()


def mostrar_login2():
    ventana2 = Tk()
    ventana2.config(bg='gray63')
    ventana2.geometry('350x700+500+50')
    ventana2.overrideredirect(1)
    ventana2.resizable(0, 0)

    imagenL = PhotoImage(file="logofinal.png")
    lblImagenL = Label(ventana2, image=imagenL).place(x=-60, y=-5)


    app = login2.Login2(ventana2)
    app.mainloop()

def mostrar_menu():
    Men = Tk()
    Men.wm_title("Menu Administrador")
    Men.geometry('360x410+500+50')
    Men.iconbitmap('LOGOTVU.ico')
    app = menu.Menu(Men)#menu
    app.mainloop()

if __name__ == "__main__":
    #main()
    mostrar_login()
    #mostrar_menu()



