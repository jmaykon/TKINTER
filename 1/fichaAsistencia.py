import tkinter as tk
import datetime
from tkinter import *
from tkinter import ttk, messagebox
import main
import functools
import operator
#from login import * #Ventana
from asistencia import *
from pasante import *
from registroPas import *

class CAsistencia(Frame):  # Herencia Frame <-- Ventana
    print("holaA")
    a1 = Asistencia()
    t1 = Asistencia()
    p1 = Pasante()
    swE = 0
    swB = 0
    varci = ''
    swBB = 0

    swH = 0
    horatE=0
    horatS=0
    he = 0
    hs = 0
    ht = 0
    me = 0
    ms = 0
    mt = 0
    se = 0
    ss = 0
    st = 0
    #hoy = ''
    def __init__(self, master=None):  # Contructor de Ventana
        super().__init__(master, width=940, height=450)  # Herencia constructor de Frame = master
        self.master = master  # declaracion de master = masterFrame
        self.pack()
        self.create_widgets()
        self.id = -1
    def create_widgets(self):
        frame1 = Frame(self, bg="#016797")  # Frame esta dentro ventana, existe solo en el metodo(No es mienbro de la clase )
        frame1.place(x=0, y=0, width=940, height=450)

        #IMG
        self.re = PhotoImage(file='registroPasantefondo.png')  # FONDO DENTRO DEL FRAME
        Label(frame1, image=self.re).place(x=70, y=50)  # LA POCISION DE LA IAMGEN DENTRO DEL FRAME


        self.titulo = Label(frame1, text="CONTROL DE ASISTENCIA", font=("Arial Black", 15), fg="black", bg="orange")
        self.titulo.place(x=320, y=55)

        self.text_ci = Label(frame1, text="CI :")
        self.cajaTxt_ci = Entry(frame1, font="15", width=15)
        self.text_ci.place(x=80, y=100)
        self.cajaTxt_ci.place(x=150, y=100)

        self.btnBuscar = Button(frame1, text="Buscar", command=self.fbuscarCi, bg="green", fg="white")  # fNuevo
        self.btnBuscar.place(x=300, y=95, width=50, height=30)
        # Hora Total
        #self.btnBuscarHT = Button(frame1, text="BuscarHT", command=self.fGuardar_HoraT, bg="green", fg="white")  # fNuevo
        #self.text_HT = Label(frame1, text="Hora Total :")
        #self.cajaTxt_HT = Entry(frame1, font="15", width=15)
        #self.btnBuscarHT.place(x=300, y=90, width=50, height=30)
        #self.text_HT.place(x=380, y=100)
        #self.cajaTxt_HT.place(x=450, y=100)

        self.text_nombre = Label(frame1, text="NOMBRE :")
        self.cajaTxt_nom = Entry(frame1, font="15", width=15)
        self.text_nombre.place(x=80, y=162)
        self.cajaTxt_nom.place(x=150, y=160)

        self.txt_ap_pat = Label(frame1, text="APELLIDO PATERNO :")
        self.cajaTxt_ap_pat = Entry(frame1, font="15", width=15)
        self.txt_ap_pat.place(x=310, y=162)
        self.cajaTxt_ap_pat.place(x=440, y=162)

        self.txt_ap_mat = Label(frame1, text="APELLIDO MATERNO :")
        self.cajaTxt_ap_mat = Entry(frame1, font="15", width=15)
        self.txt_ap_mat.place(x=600, y=162)
        self.cajaTxt_ap_mat.place(x=730, y=162)

        self.txt_carrera = Label(frame1, text="CARRERA :")
        self.cajaTxt_carrera = Entry(frame1, font="15", width=15)
        self.txt_carrera.place(x=80, y=222)
        self.cajaTxt_carrera.place(x=150, y=220)

        self.txt_area = Label(frame1, text="ÁREA :")
        self.cajaTxt_area = Entry(frame1, font="15", width=15)
        self.txt_area.place(x=310, y=222)
        self.cajaTxt_area.place(x=440, y=220)

        self.txt_turno = Label(frame1, text="TURNO :")
        self.cajaTxt_turno = Entry(frame1, font="15", width=15)
        self.txt_turno.place(x=600, y=222)
        self.cajaTxt_turno.place(x=720, y=220)

        ################# Asistencia #####################
        self.txt_fechaHoy = Label(frame1, text="Fecha Actual: ")
        self.txt_fechaHoy.place(x=600, y=100)
        self.cajaTxt_fechaA = Entry(frame1, font="15", width=10)
        self.cajaTxt_fechaA.place(x=700, y=100)
        # Fecha
        fechaA = datetime.datetime.now()
        print(fechaA)
        print(type(fechaA))
        fechaA = str(fechaA.day), '/', str(fechaA.month), '/', str(fechaA.year)

        print(fechaA)
        print(type(fechaA), "fechaa")
        self.hoy = functools.reduce(operator.add, (fechaA))
        self.cajaTxt_fechaA.insert(0, self.hoy)
        print(type(self.hoy))

        self.cajaTxt_horaE = Entry(frame1, font="15", width=15)
        self.cajaTxt_horaE.place(x=180, y=325)

        self.cajaTxt_horaS = Entry(frame1, font="15", width=15)
        self.cajaTxt_horaS.place(x=450, y=325)

        self.txt_D = Label(frame1, text="Tiempo Acumulado:")
        self.txt_D.place(x=630, y=325)
        self.cajaTxt_horaD = Entry(frame1, font="15", width=10)
        self.cajaTxt_horaD.place(x=760, y=325)

        self.btnGuardarE = Button(frame1, text="Hora Entrada", command=self.fGuardarE, bg='#063374', fg="white")  # fNuevo
        self.btnGuardarE.place(x=80, y=320, width=80, height=30)

        self.btnGuardarS = Button(frame1, text="Hora Salida", command=self.fGuardarS, bg="red", fg="white")  # fNuevo
        self.btnGuardarS.place(x=350, y=320, width=80, height=30)

        self.btnAtras = Button(frame1, text="<-- Atras", command=self.fAtras, bg="gray", fg="white")
        self.btnAtras.place(x=0, y=0)

    def fGuardar_Asistencia(self):
        pass
    def fGuardar_HoraT(self):
        datosD = self.t1.buscar_HoraDia(self.cajaTxt_ci.get())
        total_h = 0
        total_m = 0
        for fila in datosD:
            dato_hd = fila
            dato_dia = functools.reduce(operator.add, (dato_hd)) #string

            horas_dia = dato_dia[0:2]
            minutos_dia = dato_dia[4:6]

            horaD = int(horas_dia)
            minutoD = int(minutos_dia)
            #print(minutoD, "minutos")

            total_h = total_h + horaD
            total_m = total_m + minutoD
            print(total_m, "tm")
            if total_m > 60:
                total_h = total_h + 1
                total_m = total_m - 60

            if total_m == 60:
                total_m = 0
                total_h = total_h + 1
        total_h = str(total_h)
        total_m = str(total_m)
        hora_minuto = total_h + ':' + total_m
        print(hora_minuto)

        #self.cajaTxt_HT.insert(0, hora_minuto)

    def fGuardarS(self):
        if self.swBB == 1:
            self.swBB = 0
            ahora = datetime.datetime.now()
            self.hs = ahora.hour
            self.ms = ahora.minute
            # self.ss = ahora.second
            a = ahora.strftime("%H:%M") + ""
            self.horatS = a
            self.habilitarHoraS('normal')
            self.limpiarHoraS()
            self.cajaTxt_horaS.insert(0, a)
            hh2 = self.hs * 60
            hm2 = hh2 + self.ms
            print("2da Hora hm2: ", hm2)

            self.cajaTxt_ci.configure(state='normal')

            datosH1 = self.a1.buscar_asistencia_nomFe(self.cajaTxt_ci.get(), self.hoy)
            hora_entrada = datosH1[1]  # hora entrada en cadena

            hee = hora_entrada[0] + hora_entrada[1]  # hora
            mee = hora_entrada[3] + hora_entrada[4]  # min
            hee = int(hee)
            mee = int(mee)

            hh1 = hee * 60
            hm1 = hh1 + mee
            print("Entrada Hora hm1: ", hm1)

            dhm = hm2 - hm1
            if dhm < 0:
                dhm = dhm * (-1)
            nh = 0
            nm = 0
            dhmx = dhm
            while nh + nm < dhm:
                if dhmx < 60:
                    nm = dhmx
                    dhmx = 0
                else:
                    dhmx = dhmx - 60
                    nh = nh + 60
            nh = int(nh / 60)
            print("Total Horas: ", nh, ":", nm)
            sumaH = str(nh), ':', str(nm)
            self.cajaTxt_horaD.configure(state='normal')
            self.cajaTxt_horaD.delete(0, END)
            self.cajaTxt_horaD.insert(0, sumaH)
            self.cajaTxt_horaD.configure(state='disabled')

            print(self.hoy)
            print(type(self.hoy))  #

            datosA = self.a1.buscar_asistencia_nomFe(self.cajaTxt_ci.get(), self.hoy)  # hoy cambiar
            print(datosA)
            self.cajaTxt_horaE.delete(0, END)  # reseteamos la casilla
            self.cajaTxt_horaE.insert(0, datosA[1])  # entra
            # self.cajaTxt_fechaA.insert(0, datosA[4])  # dfecha
            # self.btnGuardarS.configure(state="normal")#---

            datos = self.a1.modificar_asistencia(self.cajaTxt_ci.get(), self.cajaTxt_horaE.get(),
                                                 self.cajaTxt_horaS.get(),
                                                 self.cajaTxt_horaD.get(), self.cajaTxt_fechaA.get())
            messagebox.showinfo("Modificar", "Elemento modificado correctamente")
            print(type(datos), "****")
            print(datos)  # creo te devuelve la cantidad de filas encontradas
        else:
            messagebox.showwarning("RELLENE LOS CAMPOS", "INSERTE EL CI DEL PASANTE Y PRESIONE BUSCAR")
    def fGuardarE(self):
        if self.swBB == 1:
            self.swBB = 0
            ahora = datetime.datetime.now()
            # print(ahora.hour, " : ",ahora.minute," : ",ahora.second)
            self.he = ahora.hour
            self.me = ahora.minute
            print(type(self.me))
            a = ahora.strftime("%H:%M") + ""
            print("***Hora Entrada****")
            print(type(a))
            print(a)
            self.horatE = a

            # ---- nuevo ---

            self.habilitarCaja('normal')
            if self.cajaTxt_horaE.get():
                self.cajaTxt_horaE.delete(0, END)
                self.cajaTxt_horaE.insert(0, a)
                print("verdad")
                self.a1.modificar_asistencia(self.cajaTxt_ci.get(), self.cajaTxt_horaE.get(), self.cajaTxt_horaS.get(),
                                             self.cajaTxt_horaD.get(), self.cajaTxt_fechaA.get())
                messagebox.showinfo("Hora de Entrada Modificacion",
                                    "Modificado exitosamente, Hora de Entrada: " + a + " con fecha: " + self.hoy)
                self.limpiarCaja()
            else:
                self.cajaTxt_horaE.delete(0, END)
                self.cajaTxt_horaE.insert(0, a)
                print("falso")
                self.a1.registra_asistencia(self.cajaTxt_ci.get(), self.cajaTxt_horaE.get(), self.cajaTxt_horaS.get(),
                                            self.cajaTxt_horaD.get(), self.cajaTxt_fechaA.get())
                messagebox.showinfo("Hora de Entrada",
                                    "Registrado exitosamente, Hora de Entrada: " + a + " con fecha: " + self.hoy)
                self.limpiarCaja()
        else:
            messagebox.showwarning("RELLENE LOS CAMPOS", "INSERTE EL CI DEL PASANTE Y PRESIONE BUSCAR")
    def fbuscarCi(self):
        if self.cajaTxt_ci.get() != "":
            self.swBB = 1
            try:
                datosP = self.p1.buscar_pasante(self.cajaTxt_ci.get())
                messagebox.showinfo("Buscar", "Pasante Encontrado: " + datosP[2] + ", " + datosP[3] + ", " + datosP[4])
                self.habilitarCaja('normal')
                self.limpiarCaja()
                self.cajaTxt_ci.insert(0, datosP[1])
                self.cajaTxt_nom.insert(0, datosP[2])
                self.cajaTxt_ap_pat.insert(0, datosP[3])
                self.cajaTxt_ap_mat.insert(0, datosP[4])
                self.cajaTxt_carrera.insert(0, datosP[5])
                self.cajaTxt_area.insert(0, datosP[6])
                self.cajaTxt_turno.insert(0, datosP[10])
                self.habilitarCaja('disabled')
            except:
                messagebox.showwarning("No Encontrado", "El Pasante No Esta Registrado")
            try:
                datosCA = self.a1.buscar_asistencia_nomFe(self.cajaTxt_ci.get(), self.hoy)
                print(datosCA)
                self.habilitarHoraS('normal')
                self.habilitarHoraE('normal')
                self.limpiarHoraE()

                self.cajaTxt_horaE.insert(0, datosCA[1])
                self.habilitarHoraE('disabled')
            except:
                print("Hora de Entrada Aun No Registrada")
                self.habilitarHoraS('disabled')
        else:
            messagebox.showwarning("RELLENE LOS CAMPOS", "INSERTE EL CI DEL PASANTE PRIMERO")

    def habilitarCaja(self, estado):
        #self.cajaTxt_ci.configure(state=estado)
        self.cajaTxt_fechaA.configure(state=estado)
        self.cajaTxt_nom.configure(state=estado)
        self.cajaTxt_ap_pat.configure(state=estado)
        self.cajaTxt_ap_mat.configure(state=estado)
        self.cajaTxt_carrera.configure(state=estado)
        self.cajaTxt_area.configure(state=estado)
        self.cajaTxt_turno.configure(state=estado)
        self.cajaTxt_horaE.configure(state=estado)
        self.cajaTxt_horaS.configure(state=estado)
        self.cajaTxt_horaD.configure(state=estado)

    def habilitarHoraE(self,estado):
        self.cajaTxt_horaE.configure(state=estado)
    def habilitarHoraS(self, estado):
        self.cajaTxt_horaS.configure(state=estado)

    def limpiarHoraE(self):
        self.cajaTxt_horaE.delete(0, END)
    def limpiarHoraS(self):
        self.cajaTxt_horaS.delete(0, END)

    def limpiarCaja(self):
        self.cajaTxt_ci.delete(0, END)
        self.cajaTxt_nom.delete(0, END)
        self.cajaTxt_ap_pat.delete(0, END)
        self.cajaTxt_ap_mat.delete(0, END)
        self.cajaTxt_carrera.delete(0, END)
        self.cajaTxt_area.delete(0, END)
        self.cajaTxt_turno.delete(0, END)
        #self.cajaTxt_fechaA.delete(0, END)
        self.cajaTxt_horaE.delete(0, END)
        self.cajaTxt_horaS.delete(0, END)
        self.cajaTxt_horaD.delete(0, END)


    def fAtras(self):
        self.master.destroy()
        main.mostrar_login()