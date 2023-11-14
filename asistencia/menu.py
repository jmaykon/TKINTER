from Licencia import Licencia
from Password import Password
from registroPas import *
from reporte import Reporte

class Menu(Frame):  # Herencia Frame <-- Ventana
    print("holaM")
    def __init__(self, master=None):  # Contructor de Ventana
        super().__init__(master, width=410, height=450)  # Herencia constructor de Frame = master
        self.master = master  # declaracion de master = masterFrame
        self.pack()
        self.create_widgets()


    def create_widgets(self):
        frame1 = Frame(self, )  # Frame esta dentro ventana, existe solo en el metodo(No es mienbro de la clase )
        frame1.place(x=0, y=0, width=410, height=450)







        #IMAGEN DEL REGISTRO DE PASANTES Y REPORTE
        self.um = PhotoImage(file='img/LOGO3.png')  # FONDO DENTRO DEL FRAME
        Label(frame1, image=self.um).place(x=0, y=0)  # LA POCISION DE LA IAMGEN DENTOR DEL FRAME


        #self.titulo = Label(frame1, text="Opciones",  bg='#baaa9a', fg='black', font=('Lucida Sans', 16, 'bold'))
        #self.titulo.place(x=130, y=100)


        self.btnRegistro = Button(frame1, text="Registro Pasante", command=self.fRegistro, bg="red2", fg="white", bd=4)  # fNuevo
        self.btnRegistro.place(x=130, y=180, width=150, height=30)

        self.btnReporte = Button(frame1, text="Reporte", command=self.fReporte, bg='#063374', fg="white", bd=4)  # fNuevo
        self.btnReporte.place(x=130, y=250, width=150, height=30)

        #BTN PEDIR PERMISO
        self.btnPermiso = Button(frame1, text="Pedir Licencia", command=self.fpedirpermiso, bg="red",fg="white", bd=4)  # fNuevo
        self.btnPermiso.place(x=130, y=320, width=150, height=30)

        #btn cambiar contraseña
        self.btnPassword = Button(frame1, text="Cambiar Contraseña", command=self.fcambiarPass, bg='#063374', fg="white",bd=4)  # fNuevo
        self.btnPassword.place(x=130, y=380, width=150, height=30)

        self.btnAtras = Button(frame1, text="<-- Atras", command=self.fAtras, bg="gray", fg="white")
        self.btnAtras.place(x=0, y=0)

    def fAtras(self):
        self.master.destroy()
        main.mostrar_login()
    def fRegistro(self):
        self.master.destroy()
        reg = Tk()
        reg.wm_title("Registro de Pasantes")

        reg.geometry('1400x675+0+0')# Ancho x Alto + x + y
        app = Registro(reg)
        app.mainloop()
    def fReporte(self):
        self.master.destroy()
        root = Tk()
        root.wm_title("Reporte")

        root.geometry('1145x475+0+0')
        app = Reporte(root)
        app.mainloop()

    def fcambiarPass(self):
        self.master.destroy()
        root = Tk()
        root.wm_title("Contraseña")
        root.geometry('400x500+620+30')
        app = Password(root)
        app.mainloop()

    def fpedirpermiso(self):
        self.master.destroy()
        root = Tk()
        root.wm_title("Licencia")
        root.geometry('400x500+620+30')
        app = Licencia(root)
        app.mainloop()

