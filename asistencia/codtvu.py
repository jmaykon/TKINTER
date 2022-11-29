
import tkinter
from tkinter import *
from tkinter import ttk

def ingresar():
    ventana.withdraw()
    #ventana.destroy()
    #pag1.opciones()
    ventana2 = tkinter.Toplevel()
    ventana2.title("login1TVU")
    ventana2.geometry("500x400")
    #ventana2.iconbitmap(r'C:\Users\PRENSA\PycharmProjects\Proyecto1\icono\tv.ico')

    tituloV2 = Label(ventana2, text="Bienvenido al Sistema", font=25)
    tituloV2.place(x=145, y=65)

    boton1 = tkinter.Button(ventana2, text="CONTROL DE ASISTENCIA", command=Basistencia, width=30, bg="#006", fg ="white")
    boton2 = tkinter.Button(ventana2, text="REGISTRO PASANTE", command=Bregistro, width=30, bg="#006", fg="white")
    boton3 = tkinter.Button(ventana2, text="REPORTE", command=Breporte, width=30, bg="#006", fg="white")

    boton1.place(x=145, y=140)
    boton2.place(x=145, y=200)
    boton3.place(x=145, y=260)
#image=ImageTk.PhotoImage(Image.open(r'C:\Users\PRENSA\Desktop\python\icono\tvulogo.jpg')).re

def Basistencia():
    #v2.destroy()
    ventanaB1 = Tk()
    ventanaB1.title("Control de Asistencia")
    ventanaB1.geometry("500x400")
    #ventanaB1.iconbitmap(r'C:\Users\PRENSA\PycharmProjects\Proyecto1\icono\tv.ico')
    tituloBA = Label(ventanaB1, text="CONTROL DE ASISTENCIA", font=25)
    tituloBA.place(x=145, y=65)


class BMostrar():
    pass


def Bregistro():
    #v2.destroy()
    ventanaB2 = Tk()
    ventanaB2.title("Control de Asistencia")
    ventanaB2.geometry("500x600")
    #ventanaB2.iconbitmap(r'C:\Users\PRENSA\PycharmProjects\Proyecto1\icono\tv.ico')
    tituloRG = Label(ventanaB2, text="REGISTRO DE PASANTE", font=25)

    rgCI = Label(ventanaB2, text="CI :")
    cajaTextReg = Entry(ventanaB2, font="Helventica 20", width=15)

    rgNom = Label(ventanaB2, text="NOMBRE :")
    cajaTextNom = Entry(ventanaB2, font="Helventica 20", width=15)

    rgApPat = Label(ventanaB2, text="APELLIDO PATERNO :")
    cajaTextApPat = Entry(ventanaB2, font="Helventica 20", width=15)

    rgApMat = Label(ventanaB2, text="APELLIDO MATERNO :")
    cajaTextoApMat = Entry(ventanaB2, font="Helventica 20", width=15)

    rgCarr = Label(ventanaB2, text="CARRERA :")
    cajaTextCarr = Entry(ventanaB2, font="Helventica 20", width=15)

    rgArea = Label(ventanaB2, text="ÁREA :")
    cajaTextArea = Entry(ventanaB2, font="Helventica 20", width=15)

    rgfono = Label(ventanaB2, text="TELEFONO:")
    cajaTextfono = Entry(ventanaB2, font="Helventica 20", width=15)

    botonRegis = tkinter.Button(ventanaB2, text="REGISTRAR", command=Bregistrar, width=10, bg="#006",fg="white")
    botonMostrar = tkinter.Button(ventanaB2, text="MOSTRAR", command=BMostrar, width=10, bg="#006", fg="white")


    tituloRG.place(x=145, y=65)

    rgCI.place(x=60, y=148)
    cajaTextReg.place(x=185, y=140)

    rgNom.place(x=60, y=210)
    cajaTextNom.place(x=185, y=200)

    rgApPat.place(x=60, y=270)
    cajaTextApPat.place(x=185, y=260)

    rgApMat.place(x=60, y=330)
    cajaTextoApMat.place(x=185, y=320)

    rgCarr.place(x=60, y=390)
    cajaTextCarr.place(x=185, y=380)

    rgArea.place(x=60, y=450)
    cajaTextArea.place(x=185, y=440)

    rgfono.place(x=60, y=500)
    cajaTextArea.place(x=185, y=490)

    botonRegis.place(x=150, y=500)

    botonMostrar.place(x=250, y=500)


def Bregistrar():
    pass

def Breporte():
    #v2.destroy()
    ventanaB3 = Tk()
    ventanaB3.title("Control de Asistencia3")
    ventanaB3.geometry("500x400")
    #ventanaB3.iconbitmap(r'C:\Users\PRENSA\PycharmProjects\Proyecto1\icono\tv.ico')
    tituloRP = Label(ventanaB3, text="CONTROL DE ASISTENCIA3", font=25)
    tituloRP.place(x=145, y=65)


ventana = Tk()

ventana.title("login")
ventana.geometry("500x400")
#ventana.iconbitmap(r'C:\Users\PRENSA\PycharmProjects\Proyecto1\icono\tv.ico')

titulo = Label(ventana, text="SISTEMA CPU", font=("Arial Black",25), fg="blue", bg="white")


texto1 = Label(ventana, text = "USUARIO :")
cajaTexto1 = Entry(ventana, font = "Helventica 20", width= 15)



texto2 = Label(ventana, text = "CONTRASEÑA :")
cajaTexto2 = Entry(ventana, font = "Helventica 20", width= 15, show="*")

boton = Button(ventana, text = "INGRESAR", command=ingresar, width=10, bg="#006", fg="white")


titulo.place(x=125, y=35)

texto1.place(x=40, y=148)
cajaTexto1.place(x=150, y=140)

texto2.place(x=40, y=210)
cajaTexto2.place(x=150, y=200)

boton.place(x=220, y=290)



ventana.mainloop()

