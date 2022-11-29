import datetime
import functools
import operator
import tkinter
import os
from tkinter import *
from tkinter import ttk, messagebox
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
        super().__init__(master, width=1800, height=570)  # Herencia constructor de Frame = master
        self.master = master  # declaracion de master = masterFrame
        self.pack()
        self.create_widgets()
        self.conexionDB = pymysql.connect(host="127.0.0.1", user="root", passwd="root", port=3306, database="bdmcdd")
    def create_widgets(self):
        frame1 = Frame(self, bg="red")    # Frame esta dentro ventana, existe solo en el metodo(No es mienbro de la clase )
        frame1.place(x=0, y=0, width=1800, height=570)


        self.log = PhotoImage(file='estudio.png')  # FONDO DENTRO DEL FRAME
        Label(frame1, image=self.log).place(x=0, y=0)  # LA POCISION DE LA IAMGEN DENTRO DEL FRAME

        self.titulo = Label(frame1, text="GENERAR REPORTE", font='Helvetica 25 bold', fg='green')
        self.titulo.place(x=330, y=40)

        self.cajapasante = Entry(frame1)
        self.cajapasante.place(x=130, y=140, width=150, height=25)

        self.btnBuscar = Button(frame1, text="BUSCAR CI", command=self.fBuscarCI, width=10, bg="green", fg="white")
        self.btnBuscar.place(x=30, y=140)
        # =============================BTN GENERA PDF DE 1 PASANTE===============
        self.btnPdf = Button(frame1, text="DESCARGAR PDF", command=self.fPdf2, width=15, bg="green", fg="white")
        self.btnPdf.place(x=300, y=140)

        self.btnAtras = Button(frame1, text="<-- Atras", command=self.fAtras, bg="gray", fg="white")
        self.btnAtras.place(x=0, y=0)


        #tabla
        self.grid = ttk.Treeview(frame1,
                                 columns=("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9","col10", "col11", "col12"))
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
        self.grid.column("col12", width=40, anchor=CENTER)

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
        self.grid.heading("col12", text="T. Contrato", anchor=CENTER)


        # self.grid.insert("", END, text="9974462", values=("Miguel Angel", "Aguirre", "Villarroel", "Informatica", "Produccion", "78860670"))

        self.grid.place(x=30, y=210, width=1050, height=200)
        sb = Scrollbar(frame1, orient=VERTICAL)
        sb.pack(side=RIGHT, fill=Y)  # ubica el desplazador a la derecha y ocupatodo el alto del grid
        self.grid.config(yscrollcommand=sb.set)
        sb.config(command=self.grid.yview)  # config para que el grid siga el srollbar en Y

        self.grid['selectmode'] = 'browse'


        #=====================MENU DESPLEGABLE PARA PDF POR CARRERA===============================
        self.carrera = ['INFORMATICA','COMUNICACIÓN','TÉCNICA'
                    ,'PDF DE TODOS LOS PASANTES','PRENSA','ESTUDIO','PRODUCCIÓN'     #7
                    ,'TURNO MAÑANA','TURNO TARDE','TURNO COMPLETO','POR PASANTIAS','POR CONTRATO'
                    ,'POR GESTION 2021','POR GESTION 2022','POR GESTION 2023','POR GESTION 2024','POR GESTION 2025']
        self.var1 = tkinter.StringVar(frame1)
        self.var1.set('SELECCIONE EL REPORTE')
        self.opcion1 = tkinter.OptionMenu(frame1, self.var1, *self.carrera)
        self.opcion1.config(width=25)
        self.opcion1.place(x=530, y=140)
        #================BTN PARA GENERAR PDF================
        self.btngpdf  = Button(frame1, text="DESCARGAR REPORTE (PDF)", command=self.fMenuPDF,width=25, bg="red", fg="white")
        self.btngpdf.place(x=730, y=140)
        #=================================================

        #=============MENU DESPLEGABLE POR MES==================
        self.mes = ['ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO','JULIO','AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE']
        self.var2 = tkinter.StringVar(frame1)
        self.var2.set('SELECCIONE EL MES')
        self.opcion2 = tkinter.OptionMenu(frame1, self.var2, *self.mes)
        self.opcion2.config(width=25)
        self.opcion2.place(x=930, y=140)
        # ================BTN PARA GENERAR PDF================
        self.btngpdfM = Button(frame1, text="REPORTE MENSUAL (PDF)", command=self.fPdfMes, width=25, bg="red",
                              fg="white")
        self.btngpdfM.place(x=1130, y=140)
        #=======================================================
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
                      "F FINAL", "TURNO", "GESTION","TIPO DE CONTRATO"]

            # ======================================


            file.write('<table border="1" align="center">')
            sw = 0
            c = 1
            j = 1
            k = 1
            pasa=0
            contr=0
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
                                       10] + '</td>' + '<td>' + datos2[11] + '</td>' + '</td>' + '<td>' + datos2[12] + '</td>')
                        file.write('<tr align="center">')
                        sw = sw + 1
                    # ==============================================================
                    if (j == k):
                        file.write('<td align="center">' + str(c) + '</td>')
                        j = j + 1
                        c = c + 1
                        k = k + 13
                    else:
                        j = j + 1
                        file.write('<td align="center">' + str(col) + '</td>')
                        if col == "contrato":
                            contr=contr+1
                        if col == "CONTRATO":
                            contr=contr+1
                        if col == "pasante":
                            pasa=pasa+1
                        if col == "PASANTE":
                            pasa=pasa+1
            file.write('</table>')
            if(a=="PDF DE TODOS LOS PASANTES"):
                file.write('<h3>CON CONTRATO : ' + str(contr) + '</h3>')
                file.write('<h3>CON PASANTIAS : ' + str(pasa) + '</h3>')
                file.write('<h3>TOTAL : ' + str(c - 1) + '</h3>')
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

        if (self.var1.get() == "DESCARGAR PDFs"):
            self.inforpdf()

        if (self.var1.get() == self.carrera[0]):
            dato = self.p.Buscar_informatica()
            self.generaPDF(dato, self.carrera[0])
            print("INFORMATICA")
            os.system('ReporteT.pdf')

        if (self.var1.get() == self.carrera[1]):
            dato = self.p.Buscar_comunicacion()
            self.generaPDF(dato, self.carrera[1])
            print("COMUNICACION")
            os.system('ReporteT.pdf')

        if (self.var1.get() == self.carrera[2]):
            dato = self.p.Buscar_tecnica()
            self.generaPDF(dato, self.carrera[2])
            print("TECNICA")
            os.system('ReporteT.pdf')

        if (self.var1.get() == self.carrera[3]):
            dato = self.p.Buscar_todospasantes()
            self.generaPDF(dato, self.carrera[3])
            print("PDF TODOS")
            os.system('ReporteT.pdf')
        if (self.var1.get() == self.carrera[4]):
            dato = self.p.Buscar_prensa()
            self.generaPDF(dato, self.carrera[4])
            print("PRENSA")
            os.system('ReporteT.pdf')

        if (self.var1.get() == self.carrera[5]):
            dato = self.p.Buscar_Estudio()
            self.generaPDF(dato, self.carrera[5])
            print("ESTUDIO")
            os.system('ReporteT.pdf')

        if (self.var1.get() == self.carrera[6]):
            dato = self.p.Buscar_Produccion()
            self.generaPDF(dato,self.carrera[6])
            os.system('ReporteT.pdf')
            print("2021")

        if (self.var1.get() == self.carrera[7]):
            dato = self.p.Buscar_mnn()
            self.generaPDF(dato, self.carrera[7])
            print("TURNO MÑN")
            os.system('ReporteT.pdf')

        if (self.var1.get() == self.carrera[8]):
            dato = self.p.Buscar_tarde()
            self.generaPDF(dato, self.carrera[8])
            print("TARDE")
            os.system('ReporteT.pdf')

        if (self.var1.get() == self.carrera[9]):
            dato = self.p.Buscar_completo()
            self.generaPDF(dato, self.carrera[9])
            print("COMPLETO")
            os.system('ReporteT.pdf')

        if (self.var1.get() == self.carrera[10]):
            dato = self.p.Buscar_Pasante()
            self.generaPDF(dato, self.carrera[10])
            print("COMPLETO")
            os.system('ReporteT.pdf')
        if (self.var1.get() == self.carrera[11]):
            dato = self.p.Buscar_Contrato()
            self.generaPDF(dato, self.carrera[11])
            print("COMPLETO")
            os.system('ReporteT.pdf')
        if(self.var1.get() == "SELECCIONE EL REPORTE"):
            self.inforpdf()



        a1 = 2021
        a2 = 2022
        a3 = 2023
        a4 = 2024
        a5 = 2025

        if (self.var1.get() == self.carrera[12]):
            dato = self.p.Buscar_Gestion_2021()
            self.generaPDF(dato, a1)
            os.system('ReporteT.pdf')
            print("2021")


        if (self.var1.get() == self.carrera[13]):
            dato = self.p.Buscar_Gestion_2022()
            self.generaPDF(dato, a2)
            os.system('ReporteT.pdf')
            print("2022")
        if (self.var1.get() == self.carrera[14]):
            dato = self.p.Buscar_Gestion_2023()
            self.generaPDF(dato, a3)
            os.system('ReporteT.pdf')
            print("2023")
        if (self.var1.get() == self.carrera[15]):
            dato = self.p.Buscar_Gestion_2024()
            self.generaPDF(dato, a4)
            os.system('ReporteT.pdf')
            print("2024")

        if (self.var1.get() == self.carrera[16]):
            dato = self.p.Buscar_Gestion_2025()
            self.generaPDF(dato, a5)
            os.system('ReporteT.pdf')
            print("2025")


    # ==================================
    def inforpdf(self):
        messagebox.showinfo("DESCARGAR PDF", "SELECCIONE UNA OPCION \nPARA DESCARGAR EL PDF")

    def infoPCI(self):
        messagebox.showinfo("PASANTE CI", "INSERTE CI DEL PASANTE \nA BUSCAR")

    def infoPCI2(self):
        messagebox.showinfo("PASANTE CI", "INSERTE CI DEL PASANTE \nPARA DESCARGAR EL PDF")

    def infoMes(self):
        messagebox.showinfo("PDF MES", "SELECCIONE LA OPCION \n A DESCARGAR")

    def limpiaGrid(self):
        for item in self.grid.get_children():
            self.grid.delete(item)
    def fBuscarCI2(self):
        self.limpiaGrid()
        datos = self.p.buscar_pasante(self.cajapasante.get())
        self.grid.insert("", END, text=datos[0], values=(datos[1], datos[2], datos[3], datos[4], datos[5], datos[6], datos[7], datos[8], datos[9], datos[10], datos[11]))

    def fBuscarCI(self):
        self.limpiaGrid()
        if(self.cajapasante.get()!=""):
            datos = self.p.buscar_pasante(self.cajapasante.get())
            self.grid.insert("", END, text=datos[0], values=(datos[1], datos[2], datos[3], datos[4], datos[5], datos[6], datos[7], datos[8], datos[9], datos[10], datos[11],datos[12]))
        else:
            self.infoPCI()

    def fPDFcontrato(self,datosP):
        with open('prueba2.html', 'w') as file:
            time = datetime.datetime.now()
            file.write(
                '<h1><FONT COLOR="BLUE">TV</font>' + '<FONT COLOR="RED">U</font>' + '<FONT COLOR="BLUE"> UMSA</font>' + '</h1>'
                '<h2><center><FONT COLOR="0000CD">TELEVISIÓN UNIVERSITARIA </font></center></h2>' +
                '<h2><center><FONT COLOR="0000CD">UNIVERSIDAD MAYOR DE SAN ANDRES </font></center></h2>')
            file.write('<p><h3><p style="text-align:length;"> Fecha del Reporte :' + time.strftime(
                '%d/%m/%Y') + '</p></h3>')
            file.write('<h2><center><FONT COLOR="0000CD">REPORTE : </font></center></h2>')

            file.write('<p>CI : <FONT COLOR="0000CD">' + datosP[1] + '</font></p>')
            file.write('<p>NOMBRE : <FONT COLOR="0000CD">' + datosP[2] + '</font></p>')
            file.write('<p>APELLIDO PATERNO : <FONT COLOR="0000CD">' + datosP[3] + '</font></p>')
            file.write('<p>APELLIDO MATERNO : <FONT COLOR="0000CD">' + datosP[4] + '</font></p>')
            file.write('<p>CELULAR : <FONT COLOR="0000CD">' + datosP[7] + '</font><br></p>')
            file.write('<p>FECHA DE INICIO DE CONTRATO : <FONT COLOR="0000CD">' + datosP[8] + '</font></p>')
            file.write('<p>FECHA DE SALIDA DE CONTRATO : <FONT COLOR="0000CD">' + datosP[9] + '</font></p>')
            file.write('<p>GESTIÓN : <FONT COLOR="0000CD">' + datosP[11] + '</font></p>')

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
                        file.write('<td align="center">' + datos2[0] + '</td>' + '<td  align="center">' + datos2[
                            1] + '</td>' + '<td  align="center">' + datos2[
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
            file.write('<h3>TOTAL ASISTENCIAS : ' + str(c - 1) + '</h3>')
            a = self.fGuardar_HoraT()
            file.write('<h3><p style="text-align:length;">HORAS TOTAL GENERAL ' + str(self.hora) + ':' + str(
                self.minuto) + '</p></h3>')

        exe = 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
        config = pdfkit.configuration(wkhtmltopdf=exe)
        pdfkit.from_file('prueba2.html', 'ReportI.pdf', configuration=config)

    def fPDFpasante(self,datosP):
        with open('prueba2.html', 'w') as file:
            time = datetime.datetime.now()
            file.write(
                '<h1><FONT COLOR="BLUE">TV</font>' + '<FONT COLOR="RED">U</font>' + '<FONT COLOR="BLUE"> UMSA</font>' + '</h1>'
                                                                                                                        '<h2><center><FONT COLOR="0000CD">TELEVISIÓN UNIVERSITARIA </font></center></h2>' +
                '<h2><center><FONT COLOR="0000CD">UNIVERSIDAD MAYOR DE SAN ANDRES </font></center></h2>')
            file.write('<p><h3><p style="text-align:length;"> Fecha del Reporte :' + time.strftime(
                '%d/%m/%Y') + '</p></h3>')
            file.write('<h2><center><FONT COLOR="0000CD">REPORTE DEL PASANTE:</font></center></h2>')

            file.write('<p>CI : <FONT COLOR="0000CD">' + datosP[1] + '</font></p>')
            file.write('<p>NOMBRE : <FONT COLOR="0000CD">' + datosP[2] + '</font></p>')
            file.write('<p>APELLIDO PATERNO : <FONT COLOR="0000CD">' + datosP[3] + '</font></p>')
            file.write('<p>APELLIDO MATERNO : <FONT COLOR="0000CD">' + datosP[4] + '</font></p>')
            file.write('<p>CARRERA : <FONT COLOR="0000CD">' + datosP[5] + '</font><br></p>')
            file.write('<p>ÁREA : <FONT COLOR="0000CD">' + datosP[6] + '</font><br></p>')
            file.write('<p>CELULAR : <FONT COLOR="0000CD">' + datosP[7] + '</font><br></p>')
            file.write('<p>FECHA DE INICIO DE PASANTIA : <FONT COLOR="0000CD">' + datosP[8] + '</font></p>')
            file.write('<p>FECHA DE SALIDA DE PASANTIA : <FONT COLOR="0000CD">' + datosP[9] + '</font></p>')
            file.write('<p>TURNO : <FONT COLOR="0000CD">' + datosP[10] + '</font></p>')
            file.write('<p>GESTIÓN : <FONT COLOR="0000CD">' + datosP[11] + '</font></p>')

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
                        file.write('<td align="center">' + datos2[0] + '</td>' + '<td  align="center">' + datos2[
                            1] + '</td>' + '<td  align="center">' + datos2[
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
            file.write('<h3>TOTAL ASISTENCIAS : ' + str(c - 1) + '</h3>')
            a = self.fGuardar_HoraT()

            file.write('<h3><p style="text-align:length;">HORAS TOTAL GENERAL ' + str(self.hora) + ':' + str(
                self.minuto) + '</p></h3>')

        exe = 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
        config = pdfkit.configuration(wkhtmltopdf=exe)
        pdfkit.from_file('prueba2.html', 'ReportI.pdf', configuration=config)


    #============================================
    def fPDFmes_Pasante(self,datosP):
        with open('prueba2.html', 'w') as file:
            time = datetime.datetime.now()
            file.write(
                '<h1><FONT COLOR="BLUE">TV</font>' + '<FONT COLOR="RED">U</font>' + '<FONT COLOR="BLUE"> UMSA</font>' + '</h1>'
                '<h2><center><FONT COLOR="0000CD">TELEVISIÓN UNIVERSITARIA </font></center></h2>' +
                '<h2><center><FONT COLOR="0000CD">UNIVERSIDAD MAYOR DE SAN ANDRES </font></center></h2>')
            file.write('<p><h3><p style="text-align:length;"> Fecha del Reporte :' + time.strftime(
                '%d/%m/%Y') + '</p></h3>')
            file.write('<h2><center><FONT COLOR="0000CD">REPORTE DEL PASANTE:</font></center></h2>')

            file.write('<p>CI : <FONT COLOR="0000CD">' + datosP[1] + '</font></p>')
            file.write('<p>NOMBRE : <FONT COLOR="0000CD">' + datosP[2] + '</font></p>')
            file.write('<p>APELLIDO PATERNO : <FONT COLOR="0000CD">' + datosP[3] + '</font></p>')
            file.write('<p>APELLIDO MATERNO : <FONT COLOR="0000CD">' + datosP[4] + '</font></p>')
            file.write('<p>CARRERA : <FONT COLOR="0000CD">' + datosP[5] + '</font><br></p>')
            file.write('<p>ÁREA : <FONT COLOR="0000CD">' + datosP[6] + '</font><br></p>')
            file.write('<p>CELULAR : <FONT COLOR="0000CD">' + datosP[7] + '</font><br></p>')
            file.write('<p>FECHA DE INICIO DE PASANTIA : <FONT COLOR="0000CD">' + datosP[8] + '</font></p>')
            file.write('<p>FECHA DE SALIDA DE PASANTIA : <FONT COLOR="0000CD">' + datosP[9] + '</font></p>')
            file.write('<p>TURNO : <FONT COLOR="0000CD">' + datosP[10] + '</font></p>')
            file.write('<p>GESTIÓN : <FONT COLOR="0000CD">' + datosP[11] + '</font></p>')


            file.write('<b>ASISTENCIA: </b><br>')
            if self.var2.get() == 'SELECCIONE EL MES':
                self.infoMes()
            if self.var2.get() == "ENERO":
                dato = self.p.buscar_Mes_Enero(self.cajapasante.get())
            if self.var2.get() == "FEBRERO":
                dato = self.p.buscar_Mes_Febrero(self.cajapasante.get())
            if self.var2.get() == "MARZO":
                dato = self.p.buscar_Mes_Marzo(self.cajapasante.get())
            if self.var2.get() == "ABRIL":
                dato = self.p.buscar_Mes_Abril(self.cajapasante.get())
            if self.var2.get() == "MAYO":
                dato = self.p.buscar_Mes_Mayo(self.cajapasante.get())
            if self.var2.get() == "JUNIO":
                dato = self.p.buscar_Mes_Junio(self.cajapasante.get())
            if self.var2.get() == "JULIO":
                dato = self.p.buscar_Mes_Julio(self.cajapasante.get())
            if self.var2.get() == "AGOSTO":
                dato = self.p.buscar_Mes_Agosto(self.cajapasante.get())
            if self.var2.get() == "SEPTIEMBRE":
                dato = self.p.buscar_Mes_Septiembre(self.cajapasante.get())
            if self.var2.get() == "OCTUBRE":
                dato = self.p.buscar_Mes_Octubre(self.cajapasante.get())
            if self.var2.get() == "NOVIEMBRE":
                dato = self.p.buscar_Mes_Noviembre(self.cajapasante.get())
            if self.var2.get() == "DICIEMBRE":
                dato = self.p.buscar_Mes_Diciembre(self.cajapasante.get())
            datos2 = ["Nro", "Hra ENTRADA", "Hra SALIDA", "Hras TOTAL DEL DIA", "FECHA"]
            #**********************************************

            #**********************************************
            file.write('<table border="1" align="center">')

            sw = 0
            c = 1
            j = 1
            k = 1
            l = 5

            for i in dato:
                file.write('<tr align="center">')

                for col in i:
                        # ==================TITULO DE LA TABLA==========================
                    if (sw == 0):
                        file.write('<td align="center">' + datos2[0] + '</td>' + '<td  align="center">' + datos2[1] + '</td>' + '<td  align="center">' + datos2[2] + '</td  align="center">' + '<td  align="center">' + datos2[3] + '</td>'
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
            file.write('<h3>TOTAL ASISTENCIAS : ' + str(c - 1) + '</h3>')
            a = self.fGuardar_Hora_Mes()

            file.write('<h3><p style="text-align:length;">HORAS TOTAL GENERAL ' + str(self.hora2) + ':' + str(
                self.minuto2) + '</p></h3>')

        exe = 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
        config = pdfkit.configuration(wkhtmltopdf=exe)
        pdfkit.from_file('prueba2.html', 'ReportI.pdf', configuration=config)


    #============================================
    def fPDFmes_Contrato(self,datosP):
        with open('prueba2.html', 'w') as file:
            time = datetime.datetime.now()
            file.write(
                '<h1><FONT COLOR="BLUE">TV</font>' + '<FONT COLOR="RED">U</font>' + '<FONT COLOR="BLUE"> UMSA</font>' + '</h1>'
                '<h2><center><FONT COLOR="0000CD">TELEVISIÓN UNIVERSITARIA </font></center></h2>' +
                '<h2><center><FONT COLOR="0000CD">UNIVERSIDAD MAYOR DE SAN ANDRES </font></center></h2>')
            file.write('<p><h3><p style="text-align:length;"> Fecha del Reporte :' + time.strftime(
                '%d/%m/%Y') + '</p></h3>')
            file.write('<h2><center><FONT COLOR="0000CD">REPORTE : </font></center></h2>')

            file.write('<p>CI : <FONT COLOR="0000CD">' + datosP[1] + '</font></p>')
            file.write('<p>NOMBRE : <FONT COLOR="0000CD">' + datosP[2] + '</font></p>')
            file.write('<p>APELLIDO PATERNO : <FONT COLOR="0000CD">' + datosP[3] + '</font></p>')
            file.write('<p>APELLIDO MATERNO : <FONT COLOR="0000CD">' + datosP[4] + '</font></p>')
            file.write('<p>ÁREA : <FONT COLOR="0000CD">' + datosP[6] + '</font><br></p>')
            file.write('<p>CELULAR : <FONT COLOR="0000CD">' + datosP[7] + '</font><br></p>')
            file.write('<p>FECHA DE INICIO DEL CONTRATO : <FONT COLOR="0000CD">' + datosP[8] + '</font></p>')
            file.write('<p>FECHA DE SALIDA DEL CONTRATO : <FONT COLOR="0000CD">' + datosP[9] + '</font></p>')
            file.write('<p>GESTIÓN : <FONT COLOR="0000CD">' + datosP[11] + '</font></p>')


            file.write('<b>ASISTENCIA: </b><br>')
            if self.var2.get() == 'SELECCIONE EL MES':
                self.infoMes()
            if self.var2.get() == "ENERO":
                dato = self.p.buscar_Mes_Enero(self.cajapasante.get())
            if self.var2.get() == "FEBRERO":
                dato = self.p.buscar_Mes_Febrero(self.cajapasante.get())
            if self.var2.get() == "MARZO":
                dato = self.p.buscar_Mes_Marzo(self.cajapasante.get())
            if self.var2.get() == "ABRIL":
                dato = self.p.buscar_Mes_Abril(self.cajapasante.get())
            if self.var2.get() == "MAYO":
                dato = self.p.buscar_Mes_Mayo(self.cajapasante.get())
            if self.var2.get() == "JUNIO":
                dato = self.p.buscar_Mes_Junio(self.cajapasante.get())
            if self.var2.get() == "JULIO":
                dato = self.p.buscar_Mes_Julio(self.cajapasante.get())
            if self.var2.get() == "AGOSTO":
                dato = self.p.buscar_Mes_Agosto(self.cajapasante.get())
            if self.var2.get() == "SEPTIEMBRE":
                dato = self.p.buscar_Mes_Septiembre(self.cajapasante.get())
            if self.var2.get() == "OCTUBRE":
                dato = self.p.buscar_Mes_Octubre(self.cajapasante.get())
            if self.var2.get() == "NOVIEMBRE":
                dato = self.p.buscar_Mes_Noviembre(self.cajapasante.get())
            if self.var2.get() == "DICIEMBRE":
                dato = self.p.buscar_Mes_Diciembre(self.cajapasante.get())
            datos2 = ["Nro", "Hra ENTRADA", "Hra SALIDA", "Hras TOTAL DEL DIA", "FECHA"]
            #**********************************************

            #**********************************************
            file.write('<table border="1" align="center">')

            sw = 0
            c = 1
            j = 1
            k = 1
            l = 5

            for i in dato:
                file.write('<tr align="center">')

                for col in i:
                        # ==================TITULO DE LA TABLA==========================
                    if (sw == 0):
                        file.write('<td align="center">' + datos2[0] + '</td>' + '<td  align="center">' + datos2[1] + '</td>' + '<td  align="center">' + datos2[2] + '</td  align="center">' + '<td  align="center">' + datos2[3] + '</td>'
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
            file.write('<h3>TOTAL ASISTENCIAS : ' + str(c - 1) + '</h3>')
            a = self.fGuardar_Hora_Mes()

            file.write('<h3><p style="text-align:length;">HORAS TOTAL GENERAL ' + str(self.hora2) + ':' + str(
                self.minuto2) + '</p></h3>')

        exe = 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
        config = pdfkit.configuration(wkhtmltopdf=exe)
        pdfkit.from_file('prueba2.html', 'ReportI.pdf', configuration=config)


    def fPdf2(self):
        if(self.cajapasante.get()!=""):
            datosP = self.p.buscar_pasante(self.cajapasante.get())

            def eliminarcaracter(c):
                carateres = ("(", ")", "'", ",")
                n1 = str(c)
                vs = ""
                for letteres in n1:
                    if letteres not in carateres:
                        vs = vs + letteres
                return vs
            a =self.p.Buscar_CI_Contrato(self.cajapasante.get())
            b=eliminarcaracter(a)

            a2 = self.p.Buscar_CI_CONTRATO2(self.cajapasante.get())
            b2 = eliminarcaracter(a2)

            c = self.p.Buscar_CI_Pasante(   self.cajapasante.get())
            d = eliminarcaracter(c)

            c2 = self.p.Buscar_CI_PASANTE2(self.cajapasante.get())
            d2 = eliminarcaracter(c2)

            if b == "contrato":
                self.fPDFcontrato(datosP)
                os.system('ReportI.pdf')

            if b2 == "CONTRATO":
                self.fPDFcontrato(datosP)
                os.system('ReportI.pdf')

            if d == "pasante":
                #self.fPDFpasante(datosP)
                self.fPDFpasante(datosP)
                os.system('ReportI.pdf')

            if d2 == "PASANTE":
                #self.fPDFpasante(datosP)
                self.fPDFpasante(datosP)
                os.system('ReportI.pdf')



        else:
            self.infoPCI2()

    def fPdfMes(self):
        if(self.cajapasante.get()!=""):
            datosP = self.p.buscar_pasante(self.cajapasante.get())

            def eliminarcaracter(c):
                carateres = ("(", ")", "'", ",")
                n1 = str(c)
                vs = ""
                for letteres in n1:
                    if letteres not in carateres:
                        vs = vs + letteres
                return vs
            a =self.p.Buscar_CI_Contrato(self.cajapasante.get())
            a2=self.p.Buscar_CI_CONTRATO2(self.cajapasante.get())
            b=eliminarcaracter(a)
            b2 = eliminarcaracter(a2)

            c = self.p.Buscar_CI_Pasante(   self.cajapasante.get())
            d = eliminarcaracter(c)

            c2 = self.p.Buscar_CI_PASANTE2(self.cajapasante.get())
            d2 = eliminarcaracter(c2)

            if b == "contrato":
                print(b)
                print("contrato")
                self.fPDFmes_Contrato(datosP)
                os.system('ReportI.pdf')

            if b2 == "CONTRATO":
                print(b2 + "   AAAAAA")
                print(datosP)
                self.fPDFmes_Contrato(datosP)
                os.system('ReportI.pdf')
            if d == "pasante":

                print("PASANTE")
                # self.fPDFpasante(datosP)
                self.fPDFmes_Pasante(datosP)
                os.system('ReportI.pdf')
            if d2 == "PASANTE":
                print("PASANTE")
                # self.fPDFpasante(datosP)
                self.fPDFmes_Pasante(datosP)
                os.system('ReportI.pdf')
        else:
            self.infoPCI2()



    def fMostrar(self):
        datos = self.p.consulta_pasantes()
        print(datos)
        for col in datos:
            # print(col[2]) #pruebita de un solo dato
            self.grid.insert("", END, text=col[0], values=(col[1], col[2], col[3], col[4], col[5], col[6],
                                                           col[7], col[8], col[9], col[10], col[11], col[12]))
        if len(self.grid.get_children()) > 0:
            self.grid.selection_set(self.grid.get_children()[0])

    def fGuardar_Hora_Mes(self):
        if self.var2.get()=="ENERO":
            datosD2 = self.t1.buscar_HoraDia_Enero(self.cajapasante.get())
            total_h2 = 0
            total_m2 = 0
            tm = 0
            for fila in datosD2:
                dato_hd2 = fila
                # print(dato_hd)
                dato_dia2 = functools.reduce(operator.add, (dato_hd2))  # string
                if (dato_dia2 != ""):
                    horas_dia2 = dato_dia2[0:2]
                    minutos_dia2 = dato_dia2[4:6]

                    horaD2 = int(horas_dia2)
                    minutoD2 = int(minutos_dia2)
                    total_h2 = total_h2 + horaD2
                    total_m2 = total_m2 + minutoD2

                    if total_m2 >= 60:
                        total_h2 = total_h2 + 1
                        total_m2 = total_m2 - 60

            total_h2 = str(total_h2)
            total_m2 = str(total_m2)
            self.minuto2 = total_m2
            self.hora2 = total_h2
            hora_minuto2 = total_h2 + ':' + total_m2
            print("HORA TOTAL PASANTE: ", hora_minuto2)

        if self.var2.get()=="FEBRERO":
            datosD2 = self.t1.buscar_HoraDia_Febrero(self.cajapasante.get())
            total_h2 = 0
            total_m2 = 0
            tm = 0
            for fila in datosD2:
                dato_hd2 = fila
                # print(dato_hd)
                dato_dia2 = functools.reduce(operator.add, (dato_hd2))  # string
                if (dato_dia2 != ""):
                    horas_dia2 = dato_dia2[0:2]
                    minutos_dia2 = dato_dia2[4:6]

                    horaD2 = int(horas_dia2)
                    minutoD2 = int(minutos_dia2)
                    total_h2 = total_h2 + horaD2
                    total_m2 = total_m2 + minutoD2

                    if total_m2 >= 60:
                        total_h2 = total_h2 + 1
                        total_m2 = total_m2 - 60

            total_h2 = str(total_h2)
            total_m2 = str(total_m2)
            self.minuto2 = total_m2
            self.hora2 = total_h2
            hora_minuto2 = total_h2 + ':' + total_m2
            print("HORA TOTAL PASANTE: ", hora_minuto2)

        if self.var2.get()=="MARZO":
            datosD2 = self.t1.buscar_HoraDia_Mayo(self.cajapasante.get())
            total_h2 = 0
            total_m2 = 0
            tm = 0
            for fila in datosD2:
                dato_hd2 = fila
                # print(dato_hd)
                dato_dia2 = functools.reduce(operator.add, (dato_hd2))  # string
                if (dato_dia2 != ""):
                    horas_dia2 = dato_dia2[0:2]
                    minutos_dia2 = dato_dia2[4:6]

                    horaD2 = int(horas_dia2)
                    minutoD2 = int(minutos_dia2)
                    total_h2 = total_h2 + horaD2
                    total_m2 = total_m2 + minutoD2

                    if total_m2 >= 60:
                        total_h2 = total_h2 + 1
                        total_m2 = total_m2 - 60

            total_h2 = str(total_h2)
            total_m2 = str(total_m2)
            self.minuto2 = total_m2
            self.hora2 = total_h2
            hora_minuto2 = total_h2 + ':' + total_m2
            print("HORA TOTAL PASANTE: ", hora_minuto2)

        if self.var2.get()=="ABRIL":
            datosD2 = self.t1.buscar_HoraDia_Abril(self.cajapasante.get())
            total_h2 = 0
            total_m2 = 0
            tm = 0
            for fila in datosD2:
                dato_hd2 = fila
                # print(dato_hd)
                dato_dia2 = functools.reduce(operator.add, (dato_hd2))  # string
                if (dato_dia2 != ""):
                    horas_dia2 = dato_dia2[0:2]
                    minutos_dia2 = dato_dia2[4:6]

                    horaD2 = int(horas_dia2)
                    minutoD2 = int(minutos_dia2)
                    total_h2 = total_h2 + horaD2
                    total_m2 = total_m2 + minutoD2

                    if total_m2 >= 60:
                        total_h2 = total_h2 + 1
                        total_m2 = total_m2 - 60

            total_h2 = str(total_h2)
            total_m2 = str(total_m2)
            self.minuto2 = total_m2
            self.hora2 = total_h2
            hora_minuto2 = total_h2 + ':' + total_m2
            print("HORA TOTAL PASANTE: ", hora_minuto2)

        if self.var2.get()=="MAYO":
            datosD2 = self.t1.buscar_HoraDia_Mayo(self.cajapasante.get())
            total_h2 = 0
            total_m2 = 0
            tm = 0
            for fila in datosD2:
                dato_hd2 = fila
                # print(dato_hd)
                dato_dia2 = functools.reduce(operator.add, (dato_hd2))  # string
                if (dato_dia2 != ""):
                    horas_dia2 = dato_dia2[0:2]
                    minutos_dia2 = dato_dia2[4:6]

                    horaD2 = int(horas_dia2)
                    minutoD2 = int(minutos_dia2)
                    total_h2 = total_h2 + horaD2
                    total_m2 = total_m2 + minutoD2

                    if total_m2 >= 60:
                        total_h2 = total_h2 + 1
                        total_m2 = total_m2 - 60

            total_h2 = str(total_h2)
            total_m2 = str(total_m2)
            self.minuto2 = total_m2
            self.hora2 = total_h2
            hora_minuto2 = total_h2 + ':' + total_m2
            print("HORA TOTAL PASANTE: ", hora_minuto2)

        if self.var2.get()=="JUNIO":
            datosD2 = self.t1.buscar_HoraDia_Junio(self.cajapasante.get())
            total_h2 = 0
            total_m2 = 0
            tm = 0
            for fila in datosD2:
                dato_hd2 = fila
                # print(dato_hd)
                dato_dia2 = functools.reduce(operator.add, (dato_hd2))  # string
                if (dato_dia2 != ""):
                    horas_dia2 = dato_dia2[0:2]
                    minutos_dia2 = dato_dia2[4:6]

                    horaD2 = int(horas_dia2)
                    minutoD2 = int(minutos_dia2)
                    total_h2 = total_h2 + horaD2
                    total_m2 = total_m2 + minutoD2

                    if total_m2 >= 60:
                        total_h2 = total_h2 + 1
                        total_m2 = total_m2 - 60

            total_h2 = str(total_h2)
            total_m2 = str(total_m2)
            self.minuto2 = total_m2
            self.hora2 = total_h2
            hora_minuto2 = total_h2 + ':' + total_m2
            print("HORA TOTAL PASANTE: ", hora_minuto2)

        if self.var2.get()=="JULIO":
            datosD2 = self.t1.buscar_HoraDia_Julio(self.cajapasante.get())
            total_h2 = 0
            total_m2 = 0
            tm = 0
            for fila in datosD2:
                dato_hd2 = fila
                # print(dato_hd)
                dato_dia2 = functools.reduce(operator.add, (dato_hd2))  # string
                if (dato_dia2 != ""):
                    horas_dia2 = dato_dia2[0:2]
                    minutos_dia2 = dato_dia2[4:6]

                    horaD2 = int(horas_dia2)
                    minutoD2 = int(minutos_dia2)
                    total_h2 = total_h2 + horaD2
                    total_m2 = total_m2 + minutoD2

                    if total_m2 >= 60:
                        total_h2 = total_h2 + 1
                        total_m2 = total_m2 - 60

            total_h2 = str(total_h2)
            total_m2 = str(total_m2)
            self.minuto2 = total_m2
            self.hora2 = total_h2
            hora_minuto2 = total_h2 + ':' + total_m2
            print("HORA TOTAL PASANTE: ", hora_minuto2)

        if self.var2.get()=="AGOSTO":
            datosD2 = self.t1.buscar_HoraDia_Agosto(self.cajapasante.get())
            total_h2 = 0
            total_m2 = 0
            tm = 0
            for fila in datosD2:
                dato_hd2 = fila
                # print(dato_hd)
                dato_dia2 = functools.reduce(operator.add, (dato_hd2))  # string
                if (dato_dia2 != ""):
                    horas_dia2 = dato_dia2[0:2]
                    minutos_dia2 = dato_dia2[4:6]

                    horaD2 = int(horas_dia2)
                    minutoD2 = int(minutos_dia2)
                    total_h2 = total_h2 + horaD2
                    total_m2 = total_m2 + minutoD2

                    if total_m2 >= 60:
                        total_h2 = total_h2 + 1
                        total_m2 = total_m2 - 60

            total_h2 = str(total_h2)
            total_m2 = str(total_m2)
            self.minuto2 = total_m2
            self.hora2 = total_h2
            hora_minuto2 = total_h2 + ':' + total_m2
            print("HORA TOTAL PASANTE: ", hora_minuto2)

        if self.var2.get()=="SEPTIEMBRE":
            datosD2 = self.t1.buscar_HoraDia_Septiembre(self.cajapasante.get())
            total_h2 = 0
            total_m2 = 0
            tm = 0
            for fila in datosD2:
                dato_hd2 = fila
                # print(dato_hd)
                dato_dia2 = functools.reduce(operator.add, (dato_hd2))  # string
                if (dato_dia2 != ""):
                    horas_dia2 = dato_dia2[0:2]
                    minutos_dia2 = dato_dia2[4:6]

                    horaD2 = int(horas_dia2)
                    minutoD2 = int(minutos_dia2)
                    total_h2 = total_h2 + horaD2
                    total_m2 = total_m2 + minutoD2

                    if total_m2 >= 60:
                        total_h2 = total_h2 + 1
                        total_m2 = total_m2 - 60

            total_h2 = str(total_h2)
            total_m2 = str(total_m2)
            self.minuto2 = total_m2
            self.hora2 = total_h2
            hora_minuto2 = total_h2 + ':' + total_m2
            print("HORA TOTAL PASANTE: ", hora_minuto2)

        if self.var2.get()=="OCTUBRE":
            datosD2 = self.t1.buscar_HoraDia_Octubre(self.cajapasante.get())
            total_h2 = 0
            total_m2 = 0
            tm = 0
            for fila in datosD2:
                dato_hd2 = fila
                # print(dato_hd)
                dato_dia2 = functools.reduce(operator.add, (dato_hd2))  # string
                if (dato_dia2 != ""):
                    horas_dia2 = dato_dia2[0:2]
                    minutos_dia2 = dato_dia2[4:6]

                    horaD2 = int(horas_dia2)
                    minutoD2 = int(minutos_dia2)
                    total_h2 = total_h2 + horaD2
                    total_m2 = total_m2 + minutoD2

                    if total_m2 >= 60:
                        total_h2 = total_h2 + 1
                        total_m2 = total_m2 - 60

            total_h2 = str(total_h2)
            total_m2 = str(total_m2)
            self.minuto2 = total_m2
            self.hora2 = total_h2
            hora_minuto2 = total_h2 + ':' + total_m2
            print("HORA TOTAL PASANTE: ", hora_minuto2)

        if self.var2.get()=="NOVIEMBRE":
            datosD2 = self.t1.buscar_HoraDia_Noviembre(self.cajapasante.get())
            total_h2 = 0
            total_m2 = 0
            tm = 0
            for fila in datosD2:
                dato_hd2 = fila
                # print(dato_hd)
                dato_dia2 = functools.reduce(operator.add, (dato_hd2))  # string
                if (dato_dia2 != ""):
                    horas_dia2 = dato_dia2[0:2]
                    minutos_dia2 = dato_dia2[4:6]

                    horaD2 = int(horas_dia2)
                    minutoD2 = int(minutos_dia2)
                    total_h2 = total_h2 + horaD2
                    total_m2 = total_m2 + minutoD2

                    if total_m2 >= 60:
                        total_h2 = total_h2 + 1
                        total_m2 = total_m2 - 60

            total_h2 = str(total_h2)
            total_m2 = str(total_m2)
            self.minuto2 = total_m2
            self.hora2 = total_h2
            hora_minuto2 = total_h2 + ':' + total_m2
            print("HORA TOTAL PASANTE: ", hora_minuto2)

        if self.var2.get()=="DICIEMBRE":
            datosD2 = self.t1.buscar_HoraDia_Diciembre(self.cajapasante.get())
            total_h2 = 0
            total_m2 = 0
            tm = 0
            for fila in datosD2:
                dato_hd2 = fila
                # print(dato_hd)
                dato_dia2 = functools.reduce(operator.add, (dato_hd2))  # string
                if (dato_dia2 != ""):
                    horas_dia2 = dato_dia2[0:2]
                    minutos_dia2 = dato_dia2[4:6]

                    horaD2 = int(horas_dia2)
                    minutoD2 = int(minutos_dia2)
                    total_h2 = total_h2 + horaD2
                    total_m2 = total_m2 + minutoD2

                    if total_m2 >= 60:
                        total_h2 = total_h2 + 1
                        total_m2 = total_m2 - 60

            total_h2 = str(total_h2)
            total_m2 = str(total_m2)
            self.minuto2 = total_m2
            self.hora2 = total_h2
            hora_minuto2 = total_h2 + ':' + total_m2
            print("HORA TOTAL PASANTE: ", hora_minuto2)


    def fGuardar_HoraT(self):
        datosD = self.t1.buscar_HoraDia(self.cajapasante.get())
        total_h = 0
        total_m = 0
        tm = 0
        for fila in datosD:
            dato_hd = fila
            # print(dato_hd)
            dato_dia = functools.reduce(operator.add, (dato_hd))  # string
            if (dato_dia != ""):
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
        self.minuto = total_m
        self.hora = total_h
        hora_minuto = total_h + ':' + total_m
        print("HORA TOTAL PASANTE: ", hora_minuto)


    def fAtras(self):
        self.master.destroy()
        main.mostrar_menu()