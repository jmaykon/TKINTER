from menu import *
from fichaAsistencia import CAsistencia

class Login(Frame):
    def __init__(self, master, *args):
        super().__init__(master, *args)
        self.user_marcar = "Administrador"
        self.contra_marcar = "Ingrese su contraseña"
        self.fila1 = ''
        self.fila2 = ''
        self.widgets()
        self.master = master
        self.pack()
    def fIngresar(self):
        self.master.destroy()
        log = Tk()
        log.wm_title("Ficha de Asistencia")
        log.geometry('1345x675+0+0')
        app = CAsistencia(log)
        app.mainloop()




    def salir(self):
        self.master.destroy()
        self.master.quit()

    def IrAlogin2(self):
        self.master.destroy()
        main.mostrar_login2()

    def widgets(self):
        Label(self.master, text='UNIDAD DE COMUNICACIÓN', bg='#a2b6d0', fg='black', font=('Lucida Sans', 16, 'bold')).pack(pady=5)
        Label(self.master, text='SOCIAL Y GENERACIÓN DE', bg='#a2b6d0', fg='black',font=('Lucida Sans', 16, 'bold')).pack(pady=5)
        Label(self.master, text='CONTENIDOS CULTURALES', bg='#a2b6d0', fg='black',font=('Lucida Sans', 16, 'bold')).pack(pady=5)
        Label(self.master, text='MCDyD', bg='#a2b6d0', fg='black', font=('Lucida Sans', 16, 'bold')).pack(pady=5)

        self.entry1 = Entry(self.master, font=('Comic Sans MS', 12), justify='center', fg='grey',
                            highlightbackground="#E65561",
                            highlightcolor="green2", highlightthickness=5)
        self.tvu = PhotoImage(file='img/LOGO1.png')
        Label(self.master, image=self.tvu, height=200, width=200).pack()
        Button(self.master, text='ADMINISTRADOR', bg='#063374', activebackground='gray', bd=5, fg='white',
               font=('Lucida Sans', 15, 'italic'), command=self.IrAlogin2).pack(pady=10)

        Button(self.master, text='ASISTENCIA DE PASANTES', bg='red2', activebackground='#063374', bd=5, fg='white',
               font=('Lucida Sans', 18, 'italic'), command=self.fIngresar).pack(pady=10)

        Button(self.master, text='Salir', bg='grey', activebackground='#063374', bd=5, fg='white',
               font=('Lucida Sans', 15, 'italic'), command=self.salir).pack(pady=10)

        Label(self.master, text='DESARROLLADO POR:\nMAYKON QUISBERT', bg='#a2b6d0', fg='black',
              font=('Lucida Sans', 6, 'bold')).place(x=0, y=625, width=350)


