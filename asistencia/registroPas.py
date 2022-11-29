from tkinter import *
from tkinter import messagebox, ttk
from tkcalendar import Calendar
import main
from pasante import Pasante
class Registro(Frame):  # Herencia Frame <-- Ventana
    p1 = Pasante()
    #a1 = Asistencia()
    e = ""
    sw_cal = 0
    sw_cal2 = 0
    #c = Calendario()
    def __init__(self, master=None):  # Contructor de Ventana
        super().__init__(master, width=1550, height=675)  # Herencia constructor de Frame = master
        self.master = master  # declaracion de master = masterFrame
        self.pack()
        self.create_widgets()
        self.fMostrar()
        self.habilitarCaja("disabled")
        self.habilitarBtnOp1("normal")# nuevo mod, elim
        self.habilitarBtnOp2("disabled")
        self.id = -1

    def habilitarCaja(self, estado):
        self.cajaTxt_ci.configure(state=estado)
        self.cajaTxt_nom.configure(state=estado)
        self.cajaTxt_ap_pat.configure(state=estado)
        self.cajaTxt_ap_mat.configure(state=estado)
        self.cajaTxt_carrera.configure(state=estado)
        self.cajaTxt_area.configure(state=estado)
        self.cajaTxt_turno.configure(state=estado)
        self.cajaTxt_cel.configure(state=estado)
        self.opcionC.configure(state=estado)
        self.cajaTxt_fechaIni.configure(state=estado)
        self.cajaTxt_fechaFin.configure(state=estado)
        self.cajaTxt_gestion.configure(state=estado)
    def limpiarCaja(self):
        self.cajaTxt_ci.delete(0, END)
        self.cajaTxt_nom.delete(0, END)
        self.cajaTxt_ap_pat.delete(0, END)
        self.cajaTxt_ap_mat.delete(0, END)
        self.cajaTxt_cel.delete(0, END)
        self.var_tipoC.set(' ')
        self.cajaTxt_fechaIni.delete(0, END)
        self.cajaTxt_fechaFin.delete(0, END)
        self.cajaTxt_gestion.delete(0, END)
        self.cajaTxt_carrera.delete(0,END)
        self.cajaTxt_area.delete(0,END)
        self.cajaTxt_turno.delete(0,END)
    def limpiaGrid(self):
        for item in self.grid.get_children():
            self.grid.delete(item)
    def habilitarBtnOp1(self, estado):
        self.btnNuevo.configure(state=estado)
        self.btnModificar.configure(state=estado)
        self.btnEliminar.configure(state=estado)

    def habilitarBtnOp2(self, estado):
        self.btnGuardar.configure(state=estado)
        self.btnCancelar.configure(state=estado)

    def fMostrar(self):
        datos = self.p1.consulta_pasantes()
        for col in datos:
            # print(col[2]) #pruebita de un solo dato
            self.grid.insert("", END, text=col[0], values=(col[1], col[2], col[3], col[4], col[5], col[6], col[7], col[8], col[9], col[10], col[11], col[12]))
        if len(self.grid.get_children()) > 0:
            self.grid.selection_set(self.grid.get_children()[0])

    def fGuardar(self):
        if self.id == -1:
            self.p1.registra_pasante(self.cajaTxt_ci.get(), self.cajaTxt_nom.get(), self.cajaTxt_ap_pat.get(), self.cajaTxt_ap_mat.get(), self.cajaTxt_carrera.get(), self.cajaTxt_area.get(), self.cajaTxt_cel.get(), self.var_tipoC.get(), self.cajaTxt_fechaIni.get(), self.cajaTxt_fechaFin.get(), self.cajaTxt_turno.get(), self.cajaTxt_gestion.get())
            messagebox.showinfo("Insertar", "Elemento insertado correctamente")
        else:
            self.p1.modificar_pasante(self.id, self.cajaTxt_ci.get(), self.cajaTxt_nom.get(), self.cajaTxt_ap_pat.get(), self.cajaTxt_ap_mat.get(), self.cajaTxt_carrera.get(), self.cajaTxt_area.get(), self.cajaTxt_cel.get(), self.var_tipoC.get(), self.cajaTxt_fechaIni.get(), self.cajaTxt_fechaFin.get(), self.cajaTxt_turno.get(), self.cajaTxt_gestion.get())
            messagebox.showinfo("Modificar", "Elemento modificado correctamente")
            self.id = -1

        self.limpiaGrid()
        self.fMostrar()
        self.limpiarCaja()
        self.habilitarBtnOp2("disabled")
        self.habilitarBtnOp1("normal")
        self.habilitarCaja("disabled")
    def fCancelar(self):
        r = messagebox.askquestion("Cancelar", "Esta seguro que desea cancelar la operacion actual? ")
        if r == messagebox.YES:
            self.limpiarCaja()
            self.cajaTxt_ci.focus()
            self.habilitarBtnOp2("disabled")
            self.habilitarBtnOp1("normal")
            self.habilitarCaja("disabled")
    def fNuevo(self):
        self.habilitarCaja("normal")
        self.habilitarBtnOp1("disabled")
        self.habilitarBtnOp2("normal")
        self.limpiarCaja()
        self.cajaTxt_ci.focus()

    def fModificar(self):
        selected = self.grid.focus()  # apunta a nuestra seleccion
        clave = self.grid.item(selected, 'text')  # agarra el campo de ci

        if clave == '':
            messagebox.showwarning("Modificar", "Debes seleccionar un elemento.")
        else:

            self.id = clave
            self.habilitarCaja("normal")
            valores = self.grid.item(selected, 'values')
            self.limpiarCaja()

            self.cajaTxt_ci.insert(0, valores[0])
            self.cajaTxt_nom.insert(0, valores[1])
            self.cajaTxt_ap_pat.insert(0, valores[2])
            self.cajaTxt_ap_mat.insert(0, valores[3])
            self.cajaTxt_carrera.insert(0, valores[4])
            self.cajaTxt_area.insert(0, valores[5])
            self.cajaTxt_cel.insert(0, valores[6])
            self.cajaTxt_fechaIni.insert(0, valores[7])
            self.cajaTxt_fechaFin.insert(0, valores[8])
            self.cajaTxt_turno.insert(0, valores[9])
            self.cajaTxt_gestion.insert(0, valores[10])

            self.habilitarBtnOp1("disabled")
            self.habilitarBtnOp2("normal")
            self.cajaTxt_ci.focus()
    def fEliminar(self):
        selected = self.grid.focus() #  apunta a nuestra seleccion
        clave = self.grid.item(selected, 'text') # agarra el campo de ci
        if clave == '':
            messagebox.showwarning("Eliminar", "Debes seleccionar un elemento.")
        else:
            valores = self.grid.item(selected, 'values')
            datos = str(clave) + ", " + valores[0] + ", " + valores[1]
            r = messagebox.askquestion("Eliminar", "Deseas eliminar el registro eliminado? \n" + datos)
            if r == messagebox.YES:
                #self.id = -1
                print(type(valores[0]))
                print(valores[0])
                m = self.p1.eliminar_asistencia(valores[0])
                n = self.p1.eliminar_pasante(clave)

                if n == 1:
                    messagebox.showinfo("Eliminar", "Elemento eliminado correctamente")
                    self.limpiaGrid()
                    self.fMostrar()
                else:
                    messagebox.showinfo("Eliminar", "No fue posible eliminar el elemento")
    def fecha_calendario1(self):
        if self.sw_cal == 0:
            self.myCal = Calendar(self, setmode='day', date_pattern='dd/mm/yyyy')
            self.myCal.place(x=148, y=325, width=400, height=200)
            self.btnCal = Button(self, text="GUARDAR FECHA", bg="orange", fg="black", command=self.extraccionF1)
            self.btnCal.place(x=290, y=325, width=150, height=25)
            self.sw_cal = 1
        else:
            self.myCal.destroy()
            self.btnCal.destroy()
            self.sw_cal = 0

    def fecha_calendario2(self):
        if self.sw_cal2 == 0:
            self.myCal2 = Calendar(self, setmode='day', date_pattern='dd/mm/yyyy')
            self.myCal2.place(x=300, y=325, width=400, height=200) #x=0, y=0, width=400, height=200
            self.btnCal2 = Button(self, text="GUARDAR FECHA", bg="orange", fg="black", command=self.extraccionF2)
            self.btnCal2.place(x=450, y=325, width=150, height=25)
            self.sw_cal2 = 1
        else:
            self.myCal2.destroy()
            self.btnCal2.destroy()
            self.sw_cal2 = 0
    def extraccionF1(self):
        fechaS = self.myCal.get_date()
        self.selectFecha = Label(self, text=fechaS)
        self.selectFecha.place(x=50, y=260, width=80, height=25)
        #self.cajaTxt_fechaIni.delete(0, END)
        self.cajaTxt_fechaIni.insert(0, fechaS)

        self.btnCal.destroy()

        self.myCal.destroy()

    def extraccionF2(self):
        fechaS2 = self.myCal2.get_date()
        self.selectFecha2 = Label(self, text=fechaS2)
        self.selectFecha2.place(x=50, y=260, width=80, height=25)
        #self.cajaTxt_fechaFin.delete(0, END)
        self.cajaTxt_fechaFin.insert(0, fechaS2)

        self.btnCal2.destroy()
        self.selectFecha2.destroy()
        self.myCal2.destroy()

    def create_widgets(self):
        frame1 = Frame(self, bg="#bfdaff")  # Frame esta dentro ventana, existe solo en el metodo(No es mienbro de la clase )
        frame1.place(x=0, y=0, width=340, height=670)

        #fondo de registro del personal
        self.t = PhotoImage(file='fondoRegistros.png')  # FONDO DENTRO DEL FRAME
        Label(frame1, image=self.t).place(x=-75, y=0)

        self.titulo = Label(frame1, text="REGISTRO DEL PERSONAL", font=25)
        self.titulo.place(x=55, y=30)

        self.text_ci = Label(frame1, text="CI :")
        self.cajaTxt_ci = Entry(frame1, font="15", width=15)
        self.text_ci.place(x=20, y=70)
        self.cajaTxt_ci.place(x=150, y=70)

        self.text_nombre = Label(frame1, text="NOMBRE :")
        self.cajaTxt_nom = Entry(frame1, font="15", width=15)
        self.text_nombre.place(x=20, y=112)
        self.cajaTxt_nom.place(x=150, y=110)

        self.txt_ap_pat = Label(frame1, text="APELLIDO PATERNO :")
        self.cajaTxt_ap_pat = Entry(frame1, font="15", width=15)
        self.txt_ap_pat.place(x=20, y=152)
        self.cajaTxt_ap_pat.place(x=150, y=150)

        self.txt_ap_mat = Label(frame1, text="APELLIDO MATERNO :")
        self.cajaTxt_ap_mat = Entry(frame1, font="15", width=15)
        self.txt_ap_mat.place(x=20, y=192)
        self.cajaTxt_ap_mat.place(x=150, y=190)

        self.txt_carrera = Label(frame1, text="CARRERA :")
        self.cajaTxt_carrera = Entry(frame1, font="15", width=15)
        self.txt_carrera.place(x=20, y=232)
        self.cajaTxt_carrera.place(x=150, y=230)

        self.txt_area = Label(frame1, text="ÁREA :")
        self.cajaTxt_area = Entry(frame1, font="15", width=15)
        self.txt_area.place(x=20, y=272)
        self.cajaTxt_area.place(x=150, y=270)

        self.txt_cel = Label(frame1, text="CELULAR:")
        self.cajaTxt_cel = Entry(frame1, font="15", width=15)
        self.txt_cel.place(x=20, y=312)
        self.cajaTxt_cel.place(x=150, y=310)

        self.txt_tipoC = Label(frame1, text="TIPO DE CONTRATO:")
        self.txt_tipoC.place(x=20, y=352)
        self.var_tipoC = StringVar(frame1)
        self.var_tipoC.set('            ')

        self.opcionesC = ['PASANTE', 'CONTRATO']
        self.opcionC = OptionMenu(frame1, self.var_tipoC, *self.opcionesC)
        self.opcionC.config(width=15)
        self.opcionC.place(x=150, y=350)

        self.txt_turno = Label(frame1, text="TURNO:")
        self.cajaTxt_turno = Entry(frame1, font="15", width=15)
        self.txt_turno.place(x=20, y=392)
        self.cajaTxt_turno.place(x=150, y=390)


        self.txt_gestion = Label(frame1, text="GESTION:")
        self.cajaTxt_gestion = Entry(frame1, font="15", width=15)
        self.txt_gestion.place(x=20, y=432)
        self.cajaTxt_gestion.place(x=150, y=430)

        self.txt_fecha = Label(frame1, text="PERIODO DE CONTRATO: ")
        self.txt_fecha.place(x=20, y=482)

        self.txt_fechaD = Label(frame1, text="De:")
        self.txt_fechaD.place(x=14, y=522)
        self.cajaTxt_fechaIni = Entry(frame1, font="8", width=9)
        self.cajaTxt_fechaIni.place(x=41, y=522)
        self.btnFecha1 = Button(frame1, text=" .. ", command=self.fecha_calendario1)
        self.btnFecha1.place(x=130, y=520, width=20)

        self.txt_fechaH = Label(frame1, text="Hasta:")
        self.txt_fechaH.place(x=152, y=522)
        self.cajaTxt_fechaFin = Entry(frame1, font="8", width=9)
        self.cajaTxt_fechaFin.place(x=193, y=522)
        self.btnFecha2 = Button(frame1, text=" .. ", command=self.fecha_calendario2)
        self.btnFecha2.place(x=281, y=520, width=20)

        self.btnGuardar = Button(frame1, text="GUARDAR", command=self.fGuardar, width=10, bg="green", fg="white")
        self.btnCancelar = Button(frame1, text="CANCELAR", command=self.fCancelar, width=10, bg="red", fg="white")
        self.btnGuardar.place(x=70, y=580)
        self.btnCancelar.place(x=170, y=580)

        frame2 = Frame(self, bg="#d3dde3")  # Frame esta dentro ventana, existe solo en el metodo(No es mienbro de la clase )
        frame2.place(x=305, y=0, width=2150, height=670)

        #VENTANA MODIFICAR
        #self.um = PhotoImage(file='registropasantes.png')  # FONDO DENTRO DEL FRAME
        #Label(frame2, image=self.um).place(x=0, y=-110)  # LA POCISION DE LA IAMGEN DENTRO DEL FRAME

        self.btnNuevo = Button(frame2, text="NUEVO", command=self.fNuevo, width=10, bg='#063374', fg="white")
        self.btnNuevo.place(x=150, y=600)
        self.btnModificar = Button(frame2, text="MODIFICAR", command=self.fModificar, width=10, bg="green", fg="white")
        self.btnModificar.place(x=250, y=600)
        self.btnEliminar = Button(frame2, text="ELIMINAR", command=self.fEliminar, width=10, bg="red", fg="white")
        self.btnEliminar.place(x=350, y=600)

        self.btnRefrescar = Button(frame2, text="ACTUALIZAR", command=self.fRefrescar, width=15, bg="green", fg="white")
        self.btnRefrescar.place(x=20, y=45)

        self.btnOrdenar1 = Button(frame2, text="Ordenar por:", command=self.fOrdenar_por_Area, width=10, bg="red", fg="white")
        self.btnOrdenar1.place(x=150, y=45)
        self.var = StringVar(frame2)
        self.var.set('AREA')
        opciones = ['NINGUNO', 'PRENSA', 'ESTUDIO', 'PRODUCCION']
        opcion = OptionMenu(frame2, self.var, *opciones)
        opcion.config(width=10)
        opcion.place(x=240, y=45)

        self.btnOrdenar2 = Button(frame2, text="Ordenar por:", command=self.fOrdenar_por_Carrera, width=10, bg="red", fg="white")
        self.btnOrdenar2.place(x=380, y=45)
        self.var2 = StringVar(frame2)
        self.var2.set('CARRERA')
        opciones2 = ['NINGUNO', 'INFORMATICA', 'COMUNICACION SOCIAL']
        opcion2 = OptionMenu(frame2, self.var2, *opciones2)
        opcion2.config(width=15)
        opcion2.place(x=480, y=45)

        self.btnOrdenar3 = Button(frame2, text="Ordenar por:", command=self.fOrdenar_por_Contrato, width=15, bg="red", fg="white")
        self.btnOrdenar3.place(x=650, y=45)
        self.var3 = StringVar(frame2)
        self.var3.set('T.CONTRATO')
        opciones3 = ['PASANTE', 'CONTRATO']
        opcion3 = OptionMenu(frame2, self.var3, *opciones3)
        opcion3.config(width=10)
        opcion3.place(x=750, y=45)

        self.btnOrdenar4 = Button(frame2, text="Ordenar por:", command=self.fOrdenar_por_Turno, width=10, bg="red",
                                  fg="white")
        self.btnOrdenar4.place(x=245, y=95)
        self.var4 = StringVar(frame2)
        self.var4.set('TURNO')
        opciones4 = ['NINGUNO', 'MAÑANA', 'TARDE', 'COMPLETO']
        opcion4 = OptionMenu(frame2, self.var4, *opciones4)
        opcion4.config(width=10)
        opcion4.place(x=345, y=95)

        self.btnOrdenar5 = Button(frame2, text="Ordenar por:", command=self.fOrdenar_por_Gestion, width=10, bg="red",
                                  fg="white")
        self.btnOrdenar5.place(x=465, y=95)
        self.var5 = StringVar(frame2)
        self.var5.set('GESTION')
        opciones5 = ['2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029',
                     '2030']  # agregar mas gestiones
        opcion5 = OptionMenu(frame2, self.var5, *opciones5)
        opcion5.config(width=10)
        opcion5.place(x=565, y=95)

        self.btnAtras = Button(frame1, text="<-- Atras", command=self.fAtras, bg="gray", fg="white")
        self.btnAtras.place(x=0, y=0)

        #self.um = PhotoImage(file='LOGOTVU.png')  # FONDO DENTRO DEL FRAME
        #Label(frame2, image=self.um).place(x=0, y=500)  # LA POCISION DE LA IAMGEN DENTRO DEL FRAME

        frame3 = Frame(self, bg="yellow") # esta detras del grid
        frame3.place(x=330, y=150, width=1025, height=400)
        # GRID
        self.grid = ttk.Treeview(frame3, columns=("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9", "col10", "col11", "col12"))

        self.grid.column("#0", width=5)
        self.grid.column("col1", width=25, anchor=CENTER)
        self.grid.column("col2", width=70, anchor=CENTER)
        self.grid.column("col3", width=70, anchor=CENTER)
        self.grid.column("col4", width=70, anchor=CENTER)
        self.grid.column("col5", width=70, anchor=CENTER)
        self.grid.column("col6", width=50, anchor=CENTER)
        self.grid.column("col7", width=35, anchor=CENTER)
        self.grid.column("col8", width=50, anchor=CENTER)
        self.grid.column("col9", width=45, anchor=CENTER)
        self.grid.column("col10", width=45, anchor=CENTER)
        self.grid.column("col11", width=40, anchor=CENTER)
        self.grid.column("col12", width=30, anchor=CENTER)

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
        self.grid.heading("col12", text="T.Contrato", anchor=CENTER)

        # self.grid.insert("", END, text="9974462", values=("Miguel Angel", "Aguirre", "Villarroel", "Informatica", "Produccion", "78860670"))

        self.grid.place(x=0, y=0, width=1010, height=400)

        sb = Scrollbar(frame3, orient=VERTICAL)
        sb.pack(side=RIGHT, fill=Y) #ubica el desplazador a la derecha y ocupatodo el alto del grid
        self.grid.config(yscrollcommand=sb.set)
        sb.config(command=self.grid.yview) #config para que el grid siga el srollbar en Y

        #sb2 = Scrollbar(frame3, orient=HORIZONTAL)
        #sb2.pack(side=BOTTOM, fill=X)  # ubica el desplazador a la derecha y ocupatodo el alto del grid
        #self.grid.config(xscrollcommand=sb2.set)
        #sb2.config(command=self.grid.xview)

        self.grid['selectmode'] = 'browse'

    def fAtras(self):
        self.master.destroy()
        main.mostrar_menu()
    def fRefrescar(self):
        self.limpiaGrid()
        datosP = self.p1.ordenar_por_apellido()
        for col in datosP:
            # print(col[2]) #pruebita de un solo dato
            self.grid.insert("", END, text=col[0], values=(col[1], col[2], col[3], col[4], col[5], col[6], col[7], col[8], col[9], col[10], col[11], col[12]))
        #self.fMostrar()

    def fOrdenar_por_Carrera(self):
        self.limpiaGrid()
        datosP = self.p1.consulta_por_carrera(self.var2.get())
        for col in datosP:
            # print(col[2]) #pruebita de un solo dato
            self.grid.insert("", END, text=col[0], values=(
            col[1], col[2], col[3], col[4], col[5], col[6], col[7], col[8], col[9], col[10], col[11], col[12]))

    def fOrdenar_por_Area(self):
        self.limpiaGrid()
        datosP = self.p1.consulta_por_area(self.var.get())
        for col in datosP:
            # print(col[2]) #pruebita de un solo dato
            self.grid.insert("", END, text=col[0], values=(col[1], col[2], col[3], col[4], col[5], col[6], col[7], col[8], col[9], col[10], col[11], col[12]))

    def fOrdenar_por_Contrato(self):
        self.limpiaGrid()
        datosP = self.p1.consulta_por_tContrato(self.var3.get())
        for col in datosP:
            # print(col[2]) #pruebita de un solo dato
            self.grid.insert("", END, text=col[0], values=(
            col[1], col[2], col[3], col[4], col[5], col[6], col[7], col[8], col[9], col[10], col[11], col[12]))

    def fOrdenar_por_Turno(self):
        self.limpiaGrid()
        datosP = self.p1.consulta_por_turno(self.var4.get())
        for col in datosP:
            # print(col[2]) #pruebita de un solo dato
            self.grid.insert("", END, text=col[0], values=(
            col[1], col[2], col[3], col[4], col[5], col[6], col[7], col[8], col[9], col[10], col[11], col[12]))

    def fOrdenar_por_Gestion(self):
        self.limpiaGrid()
        datosP = self.p1.consulta_por_gestion(self.var5.get())
        for col in datosP:
            # print(col[2]) #pruebita de un solo dato
            self.grid.insert("", END, text=col[0], values=(col[1], col[2], col[3], col[4], col[5], col[6], col[7], col[8], col[9], col[10], col[11], col[12]))

