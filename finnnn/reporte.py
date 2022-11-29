import datetime
import functools
import operator
import tkinter
import os
from tkinter import *
from tkinter import ttk
import pymysql
#from fpdf import FPDF
#import matplotlib.pyplot as plt
import webbrowser as wb
import pdfkit
import main
from pdf import PDF
#from generarPDF import GenerarPDF
#from pdf import *
class Reporte(Frame):  # Herencia Frame <-- Ventana
    p = PDF()
    o = 0
    t1 = PDF()
    def __init__(self, master=None):  # Contructor de Ventana
        super().__init__(master, width=1150, height=650)  # Herencia constructor de Frame = master
        self.master = master  # declaracion de master = masterFrame
        self.pack()
        self.create_widgets()
        self.conexionDB = pymysql.connect(host="127.0.0.1", user="root", passwd="root", port=3306, database="bdmcdd")
    def create_widgets(self):
        frame1 = Frame(self, bg="snow2")  # Frame esta dentro ventana, existe solo en el metodo(No es mienbro de la clase )
        frame1.place(x=5, y=5, width=1150, height=650)

        self.re = PhotoImage(file='LOGOTVU.png')  # FONDO DENTRO DEL FRAME
        Label(frame1, image=self.re).place(x=300, y=430)  # LA POCISION DE LA IAMGEN DENTRO DEL FRAME

        self.log = PhotoImage(file='umsa.png')  # FONDO DENTRO DEL FRAME
        Label(frame1, image=self.log).place(x=700, y=450)  # LA POCISION DE LA IAMGEN DENTRO DEL FRAME

        self.titulo = Label(frame1, text="GENERAR REPORTE ", font='Helvetica 25 bold', fg='green')
        self.titulo.place(x=280, y=0)

        self.pasante = Label(frame1, text="CI PASANTE: ", font=30)
        self.pasante.place(x=370, y=60)

        self.cajapasante = Entry(frame1)
        self.cajapasante.place(x=350, y=125, width=150, height=35)

        self.btnBuscar = Button(frame1, text="BUSCAR CI", command=self.fBuscarCI, width=10, bg="green", fg="white")
        self.btnBuscar.place(x=250, y=130)
        # =============================BTN GENERA PDF DE 1 PASANTE===============
        self.btnPdf = Button(frame1, text="BUSCAR PDF DE:", command=self.fPdf2, width=20, bg="green", fg="white")
        self.btnPdf.place(x=520, y=130)

        self.btnAtras = Button(frame1, text="<-- Atras", command=self.fAtras, bg="gray", fg="white")
        self.btnAtras.place(x=0, y=0)

        self.grid = ttk.Treeview(frame1,
                                 columns=("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9","col10", "col11"))

        self.grid.column("#0", width=10)
        self.grid.column("col1", width=10, anchor=CENTER)
        self.grid.column("col2", width=65, anchor=CENTER)
        self.grid.column("col3", width=65, anchor=CENTER)
        self.grid.column("col4", width=65, anchor=CENTER)
        self.grid.column("col5", width=50, anchor=CENTER)
        self.grid.column("col6", width=50, anchor=CENTER)
        self.grid.column("col7", width=45, anchor=CENTER)
        self.grid.column("col8", width=40, anchor=CENTER)
        self.grid.column("col9", width=40, anchor=CENTER)
        self.grid.column("col10", width=40, anchor=CENTER)
        self.grid.column("col11", width=40, anchor=CENTER)

        self.grid.heading("#0", text="Id", anchor=CENTER)
        self.grid.heading("col1", text="Ci", anchor=CENTER)
        self.grid.heading("col2", text="Nombre", anchor=CENTER)
        self.grid.heading("col3", text="Ap.Paterno", anchor=CENTER)
        self.grid.heading("col4", text="Ap.Materno", anchor=CENTER)
        self.grid.heading("col5", text="Carrera", anchor=CENTER)
        self.grid.heading("col6", text="Area", anchor=CENTER)
        self.grid.heading("col7", text="Cel", anchor=CENTER)
        self.grid.heading("col8", text="FechaIni", anchor=CENTER)
        self.grid.heading("col9", text="FechaFin", anchor=CENTER)
        self.grid.heading("col10", text="Turno", anchor=CENTER)
        self.grid.heading("col11", text="Gestion", anchor=CENTER)

        # self.grid.insert("", END, text="9974462", values=("Miguel Angel", "Aguirre", "Villarroel", "Informatica", "Produccion", "78860670"))

        self.grid.place(x=0, y=250, width=1050, height=200)
        sb = Scrollbar(frame1, orient=VERTICAL)
        sb.pack(side=RIGHT, fill=Y)  # ubica el desplazador a la derecha y ocupatodo el alto del grid
        self.grid.config(yscrollcommand=sb.set)
        sb.config(command=self.grid.yview)  # config para que el grid siga el srollbar en Y

        self.grid['selectmode'] = 'browse'


        #=====================MENU DESPLEGABLE PARA PDF POR CARRERA===============================
        self.carrera = ['INFORMATICA','COMUNICACIÓN','TÉCNICA'
                    ,'PDF DE TODOS LOS PASANTES','PRENSA','ESTUDIO'
                    ,'POR GESTION 2021','POR GESTION 2022','POR GESTION 2023','POR GESTION 2024','POR GESTION 2025'
                    ,'TURNO MAÑANA','TURNO TARDE','TURNO COMPLETO']
        self.var1 = tkinter.StringVar(frame1)
        self.var1.set(' DESCARGAR PDFs')
        self.opcion1 = tkinter.OptionMenu(frame1, self.var1, *self.carrera)
        self.opcion1.config(width=30)
        self.opcion1.place(x=680,y=130)
        #================BTN PARA GENERAR PDF================
        self.btngpdf  = Button(frame1, text="DESCARGAR PDF", command=self.fMenuPDF,width=20, bg="green", fg="white")
        self.btngpdf.place(x=930, y=130)
        #=================================================
    def generaPDF(self,dato,a):
        with open('prueba2.html', 'w') as file:

            time = datetime.datetime.now()
            file.write('<h1><FONT COLOR="BLUE">TV</font>'+'<FONT COLOR="RED">U</font>'+'<FONT COLOR="BLUE"> UMSA</font>'+'</h1>'
                        '<p><h2><center><FONT COLOR="0000CD">TELEVISIÓN UNIVERSITARIA </font></center></h2>'+
                       '<h2><center><FONT COLOR="0000CD">UNIVERSIDAD MAYOR DE SAN ANDRES </font></center></h2></p>')
            file.write('<h3><p style="text-align:length"> FECHA DEL REPORTE :'+time.strftime('%d/%m/%Y')+'</p></h3>')
            # IMG

            # ========================00
            file.write('<center><h2><FONT COLOR="BLUE">REPORTE DE LOS PASANTES DE TELEVISIÓN UNIVERSITARIA</font><br></h2></center>')
            # print(datosA)

            if(a=="INFORMATICA"):
                file.write('<b>PASANTES DE LA CARRERA '+a+': </b><br>')
            if(a=="COMUNICACIÓN"):
                file.write('<b>PASANTES DE LA CARRERA' + a + ': </b><br>')
            if(a=="TÉCNICA"):
                file.write('<b>PASANTES DE LA CARRERA' + a + ': </b><br>')
            if (a == "PRENSA"):
                file.write('<b>ÁREA DE ' + a + ': </b><br>')
            if (a == "ESTUDIO"):
                file.write('<b>ÁREA DE ' + a + ': </b><br>')
            if (a == "2021"):
                file.write('<b>POR GESTIÓN 2021: </b><br>')
            if (a == "2022"):
                file.write('<b>POR GESTIÓN 2022: </b><br>')
            if (a == "2023"):
                file.write('<b>POR GESTIÓN 2023: </b><br>')
            if (a == "2024"):
                file.write('<b>POR GESTIÓN 2024: </b><br>')
            if (a == "2025"):
                file.write('<b>POR GESTIÓN 2025: </b><br>')
            if (a == "TURNO MAÑANA"):
                file.write('<b>POR ' + a + ': </b><br>')
            if (a == "TURNO TARDE"):
                file.write('<b>POR ' + a + ': </b><br>')
            if (a == "TURNO COMPLETO"):
                file.write('<b>POR ' + a + ': </b><br>')
            if (a == "PDF DE TODOS LOS PASANTES"):
                file.write('<b>TODOS LOS PASANTES DE TELEVISION UNIVERSITARIA : </b><br>')
            # ==================    ====================

            datos2 = ["Nro", "CI", "NOMBRE", "APATERNO", "AMATERNO", "CARRERA", "ÁREA", "CELULAR", "F INICIO",
                      "F FINAL", "TURNO", "GESTION"]

            # ======================================


            file.write('<table border="1" align="center">')
            sw = 0
            c = 1
            j = 1
            k = 1
            for i in dato:
                file.write('<tr align="center">')
                for col in i:
                    # ==================TITULO DE LA TABLA==========================
                    if (sw == 0):
                        file.write('<td>' + datos2[0] + '</td>' + '<td>' + datos2[1] + '</td>' + '<td>' + datos2[
                            2] + '</td>' + '<td>' + datos2[3] + '</td>'
                                   + '<td>' + datos2[4] + '</td>' + '<td>' + datos2[5] + '</td>' + '<td>' + datos2[
                                       6] + '</td>' + '<td>' + datos2[7] + '</td>'
                                   + '<td>' + datos2[8] + '</td>' + '<td>' + datos2[9] + '</td>' + '<td>' + datos2[
                                       10] + '</td>' + '<td>' + datos2[11] + '</td>')
                        file.write('<tr align="center">')
                        sw = sw + 1
                    # ==============================================================
                    if (j == k):
                        file.write('<td align="center">' + str(c) + '</td>')
                        j = j + 1
                        c = c + 1
                        k = k + 12
                    else:
                        j = j + 1
                        file.write('<td align="center">' + str(col) + '</td>')

            file.write('</table>')
            if(a=="PDF DE TODOS LOS PASANTES"):
                file.write('<h3>TOTAL PASANTES : ' + str(c-1) + '</h3>')
            if (a == "INFORMATICA"):
                file.write('<h3>TOTAL PASANTES DE INFORMATICA : ' + str(c - 1) + '</h3>')
            if (a == "COMUNICACIÓN"):
                file.write('<h3>TOTAL PASANTES DE COMUNICACION : ' + str(c - 1) + '</h3>')
            if (a == "TÉCNICA"):
                file.write('<h3>TOTAL PASANTES DE LA TÉCNICA : ' + str(c - 1) + '</h3>')
            if (a == "PRENSA"):
                file.write('<h3>TOTAL PASANTES DEL ÁREA DE PRENSA : ' + str(c - 1) + '</h3>')
            if (a == "ESTUDIO"):
                file.write('<h3>TOTAL PASANTES DEL ÁREA DE ESTUDIO : ' + str(c - 1) + '</h3>')
            if (a == "2021"):
                file.write('<h3>TOTAL PASANTES DE LA GESTIÓN 2021: '+str(c - 1) + '</h3>')
            if (a == "2022"):
                file.write('<h3>TOTAL PASANTES DE LA GESTIÓN 2022: '+str(c - 1) + '</h3>')
            if (a == "2023"):
                file.write('<h3>TOTAL PASANTES DE LA GESTIÓN 2023: '+str(c - 1) + '</h3>')
            if (a == "2024"):
                file.write('<h3>TOTAL PASANTES DE LA GESTIÓN 2024: '+str(c - 1) + '</h3>')
            if (a == "2025"):
                file.write('<h3>TOTAL PASANTES DE LA GESTIÓN 2025: '+str(c - 1) + '</h3>')
            if (a == "TURNO MAÑANA"):
                file.write('<h3>TOTAL PASANTES DEL TURNO DE LA MAÑANA : ' + str(c - 1) + '</h3>')
            if (a == "TURNO TARDE"):
                file.write('<h3>TOTAL PASANTES DEL TURNO DE LA TARDE : ' + str(c - 1) + '</h3>')
            if (a == "TURNO COMPLETO"):
                file.write('<h3>TOTAL PASANTES DEL TURNO COMPLETO : ' + str(c - 1) + '</h3>')
        exe = 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
        config = pdfkit.configuration(wkhtmltopdf=exe)
        pdfkit.from_file('prueba2.html', 'ReporteT.pdf', configuration=config)
        #=================================================
    def fMenuPDF(self):

        if(self.var1.get()==self.carrera[0]):
            dato = self.p.Buscar_informatica()
            self.generaPDF(dato,self.carrera[0])
            print("INFORMATICA")


        if(self.var1.get()==self.carrera[1]):
            dato = self.p.Buscar_comunicacion()
            self.generaPDF(dato, self.carrera[1])
            print("COMUNICACION")

        if(self.var1.get() == self.carrera[2]):
            dato = self.p.Buscar_tecnica()
            self.generaPDF(dato, self.carrera[2])
            print("TECNICA")

        if (self.var1.get() == self.carrera[3]):
            dato = self.p.Buscar_todospasantes()
            self.generaPDF(dato, self.carrera[3])
            print("PDF TODOS")
        if (self.var1.get() == self.carrera[4]):
            dato = self.p.Buscar_prensa()
            self.generaPDF(dato, self.carrera[4])
            print("PRENSA")
        if (self.var1.get() == self.carrera[5]):
            dato = self.p.Buscar_Estudio()
            self.generaPDF(dato, self.carrera[5])
            print("ESTUDIO")

        a  = "2021"
        a2 = "2022"
        a3 = "2023"
        a4 = "2024"
        a5 = "2025"
        if (self.var1.get() == self.carrera[6]):
            dato = self.p.Buscar_Gestion_2021()
            self.generaPDF(dato,a)
            print("2021")
        if (self.var1.get() == self.carrera[7]):
            dato = self.p.Buscar_Gestion_2022()
            self.generaPDF(dato, a2)
            print("2022")
        if (self.var1.get() == self.carrera[8]):
            dato = self.p.Buscar_Gestion_2023()
            self.generaPDF(dato, a3)
            print("2023")
        if (self.var1.get() == self.carrera[9]):
            dato = self.p.Buscar_Gestion_2024()
            self.generaPDF(dato, a4)
            print("2024")

        if (self.var1.get() == self.carrera[10]):
            dato = self.p.Buscar_Gestion_2025()
            self.generaPDF(dato, a5)
            print("2025")

        if (self.var1.get() == self.carrera[11]):
            dato = self.p.Buscar_mnn()
            self.generaPDF(dato, self.carrera[11])
            print("TURNO MÑN")
        if (self.var1.get() == self.carrera[12]):
            dato = self.p.Buscar_tarde()
            self.generaPDF(dato, self.carrera[12])
            print("TARDE")
        if (self.var1.get() == self.carrera[13]):
            dato = self.p.Buscar_completo()
            self.generaPDF(dato, self.carrera[13])
            print("COMPLEO")

        # ==========ABRIR PDF=============
        # import OS
        os.system('ReporteT.pdf')
    def fBuscarCI(self):

        datos = self.p.buscar_pasante(self.cajapasante.get())
        self.grid.insert("", END, text=datos[0], values=(datos[1], datos[2], datos[3], datos[4], datos[5], datos[6], datos[7], datos[8], datos[9], datos[10], datos[11]))

    def fPdf2(self):
        datosP = self.p.buscar_pasante(self.cajapasante.get())
        with open('prueba2.html', 'w') as file:
            time = datetime.datetime.now()
            file.write(
                '<h1><FONT COLOR="BLUE">TV</font>' + '<FONT COLOR="RED">U</font>' + '<FONT COLOR="BLUE"> UMSA</font>' + '</h1>'
                '<h2><center><FONT COLOR="0000CD">TELEVISIÓN UNIVERSITARIA </font></center></h2>' +
                '<h2><center><FONT COLOR="0000CD">UNIVERSIDAD MAYOR DE SAN ANDRES </font></center></h2>')
            file.write('<p><h3><p style="text-align:length;"> Fecha del Reporte :' + time.strftime('%d/%m/%Y') + '</p></h3>')
            file.write('<h2><center><FONT COLOR="0000CD">REPORTE DEL PASANTE:</font></center></h2>')

            file.write('<p>CI : <FONT COLOR="0000CD">'+ datosP[1]+'</font></p>')
            file.write('<p>NOMBRE : <FONT COLOR="0000CD">'+ datosP[2]+'</font></p>')
            file.write('<p>APELLIDO PATERNO : <FONT COLOR="0000CD">'+ datosP[3]+'</font></p>')
            file.write('<p>APELLIDO MATERNO : <FONT COLOR="0000CD">'+ datosP[4]+'</font></p>')
            file.write('<p>CARRERA : <FONT COLOR="0000CD">'+ datosP[5]+'</font><br></p>')
            file.write('<p>ÁREA : <FONT COLOR="0000CD">'+ datosP[6]+'</font><br></p>')
            file.write('<p>CELULAR : <FONT COLOR="0000CD">'+ datosP[7]+'</font><br></p>')
            file.write('<p>FECHA DE INICIO DE PASANTIA : <FONT COLOR="0000CD">'+ datosP[8]+'</font></p>')
            file.write('<p>FECHA DE SALIDA DE PASANTIA : <FONT COLOR="0000CD">'+ datosP[9]+'</font></p>')
            file.write('<p>TURNO : <FONT COLOR="0000CD">'+ datosP[10]+'</font></p>')
            file.write('<p>GESTIÓN : <FONT COLOR="0000CD">'+ datosP[11]+'</font></p>')

            file.write('<b>ASISTENCIA: </b><br>')
            dato = self.p.buscar_asistencia(self.cajapasante.get())
            datos2 = ["Nro", "Hra ENTRADA", "Hra SALIDA", "Hras TOTAL DEL DIA", "FECHA"]


            # ======================================
            file.write('<table border="1" align="center">')

            sw = 0
            c = 1
            j = 1
            k = 1
            for i in dato:
                file.write('<tr align="center">')

                for col in i:
                    # ==================TITULO DE LA TABLA==========================
                    if (sw == 0):
                        file.write('<td align="center">' + datos2[0] + '</td>' + '<td  align="center">' + datos2[1] + '</td>' + '<td  align="center">' + datos2[
                            2] + '</td  align="center">' + '<td  align="center">' + datos2[3] + '</td>'
                                   + '<td  align="center">' + datos2[4])
                        file.write('<tr  align="center">')
                        sw = sw + 1
                    # ==============================================================
                    if (j == k):
                        file.write('<td>' + str(c) + '</td>')
                        j = j + 1
                        c = c + 1
                        k = k + 5
                    else:
                        j = j + 1
                        file.write('<td>' + str(col) + '</td>')

            file.write('</table>')
            file.write('<h3>TOTAL ASISTENCIAS : '+str(c-1)+'</h3>')
            a=self.fGuardar_HoraT()

            file.write('<h3><p style="text-align:length;">HORAS TOTAL GENERAL '+str(self.hora)+':'+str(self.minuto)+'</p></h3>')

        exe = 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
        config = pdfkit.configuration(wkhtmltopdf=exe)
        pdfkit.from_file('prueba2.html', 'ReportI.pdf', configuration=config)
    #=================================================================0
        # ==========ABRIR PDF=============
        # import OS
        os.system('ReportI.pdf')



    def fMostrar(self):
        datos = self.p.consulta_pasantes()
        for col in datos:
            # print(col[2]) #pruebita de un solo dato
            self.grid.insert("", END, text=col[0], values=(col[1], col[2], col[3], col[4], col[5], col[6], col[7], col[8], col[9], col[10], col[11]))
        if len(self.grid.get_children()) > 0:
            self.grid.selection_set(self.grid.get_children()[0])


    def fGuardar_HoraT(self):
        datosD = self.t1.buscar_HoraDia(
            self.cajapasante.get())
        total_h = 0
        total_m = 0
        tm = 0
        for fila in datosD:
            dato_hd = fila
            dato_dia = functools.reduce(operator.add, (dato_hd))  # string

            horas_dia = dato_dia[0:2]
            minutos_dia = dato_dia[4:6]

            horaD = int(horas_dia)
            minutoD = int(minutos_dia)
            total_h = total_h + horaD
            total_m = total_m + minutoD

            if total_m >= 60:
                total_h = total_h + 1
                total_m = total_m - 60
        total_h = str(total_h)
        total_m = str(total_m)
        self.minuto=total_m
        self.hora=total_h
        hora_minuto = total_h + ':' + total_m
        print("HORA TOTAL: ", hora_minuto)

    def fAtras(self):
        self.master.destroy()
        main.mostrar_menu()