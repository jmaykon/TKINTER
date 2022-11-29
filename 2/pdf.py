import pymysql
from tkinter import messagebox
from registroPas import *
class PDF:
    def __init__(self):
        self.cnn = pymysql.connect(host="127.0.0.1", user="root", passwd="root", port=3306, database="bdmcdd")
    def __str__(self):
        datos = self.consulta_pasantes()
        aux = ""
        for fila in datos:
            aux = aux + str(fila) + "\n"
        return aux
    def consulta_pasantes(self):
        cur = self.cnn.cursor()
        cur.execute("select * from pasante")
        datos = cur.fetchall()
        cur.close()
        return datos
    def buscar_pasante(self, ci): #id
        cur = self.cnn.cursor()
        sql = "select * from pasante where ci = {}".format(ci)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()
        return datos

    def registra_pasante(self, ci, nombre, apPat, apMat, carrera, area, cel, fechaini, fechafin, turno, gestion):
        cur = self.cnn.cursor()
        sql = '''INSERT INTO pasante (ci, nombre, appaterno, apmaterno, carrera, area, cel, fechaini, fechafin, turno, gestion)
        VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')'''.format(ci, nombre, apPat, apMat,
                                                                                           carrera, area, cel, fechaini,
                                                                                           fechafin, turno, gestion)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n
    def eliminar_pasante(self, clave):
        cur = self.cnn.cursor()
        sql = '''DELETE FROM pasante WHERE id = {}'''.format(clave)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n
    # metodo para eliminar por seleccion de clave
    def modificar_pasante(self, id, ci, nom, appat, apmat, carr, area, cel, fechaini, fechafin, turno, gestion):
        cur = self.cnn.cursor()
        sql = '''UPDATE pasante SET ci = {}, nombre = '{}', appaterno = '{}', apmaterno = '{}', carrera = '{}', 
        area = '{}', cel = '{}', fechaini = '{}', fechafin = '{}', turno = '{}', gestion = '{}' WHERE id = {} '''.format(
            ci, nom, appat, apmat, carr, area, cel, fechaini, fechafin, turno, gestion, id)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n

    def consulta_asistencia(self):
        cur = self.cnn.cursor()
        cur.execute("select * from asistencia")
        datos = cur.fetchall()
        cur.close()
        return datos

    def buscar_asistencia(self, cip):  # id
        cur = self.cnn.cursor()
        sql = "select * from asistencia where cip = {}".format(cip)
        cur.execute(sql)
        datos = cur.fetchall()#
        cur.close()
        return datos
    def buscar_HoraDia(self, cip): #id
        cur = self.cnn.cursor()
        sql = "SELECT hora_dia FROM asistencia WHERE cip = {}".format(cip)
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()
        return datos





    def registra_asistencia(self, cip, hora_e, hora_s, hora_dia, fecha_a):
        cur = self.cnn.cursor()
        sql = '''INSERT INTO asistencia (cip, hora_entrada, hora_salida, hora_total, fecha_a)
        VALUES('{}', '{}', '{}', '{}', '{}')'''.format(cip, hora_e, hora_s, hora_dia, fecha_a)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n
    #Maykon
    def Buscar_todospasantes(self):  # id
        cur = self.cnn.cursor()
        sql = "select * from pasante"
        cur.execute(sql)
        datos = cur.fetchall()  #
        cur.close()
        return datos

    def Buscar_Gestion_2021(self):  # id
        cur = self.cnn.cursor()
        a = "2021"
        sql = "select * from pasante where gestion = '{}'".format(a)
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()
        return datos

    def Buscar_Gestion_2022(self):  # id
        cur = self.cnn.cursor()
        a = "2022"
        sql = "select * from pasante where gestion = '{}'".format(a)
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()
        return datos

    def Buscar_Gestion_2023(self):  # id
        cur = self.cnn.cursor()
        a = "2023"
        sql = "select * from pasante where gestion = '{}'".format(a)
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()
        return datos

    def Buscar_Gestion_2024(self):  # id
        cur = self.cnn.cursor()
        a = "2024"
        sql = "select * from pasante where gestion = '{}'".format(a)
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()
        return datos

    def Buscar_Gestion_2025(self):  # id
        cur = self.cnn.cursor()
        a = "2025"
        sql = "select * from pasante where gestion = '{}'".format(a)
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()
        return datos

    def Buscar_informatica(self):  # id
        cur = self.cnn.cursor()
        a = "informatica"
        sql = "select * from pasante where carrera = '{}'".format(a)
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()
        return datos

    def Buscar_Estudio(self):
        cur = self.cnn.cursor()
        a = "estudio"
        self.ar = a
        sql = "select * from pasante where area = '{}'".format(a)
        cur.execute(sql)
        datos = cur.fetchall()  #
        cur.close()
        return datos

    def Buscar_mnn(self):
        cur = self.cnn.cursor()
        a = "mañana"
        self.tu = a
        sql = "select * from pasante where turno = '{}'".format(a)
        cur.execute(sql)
        datos = cur.fetchall()  #
        cur.close()
        return datos

    def Buscar_tarde(self):
        cur = self.cnn.cursor()
        a = "tarde"
        self.tu = a
        sql = "select * from pasante where turno = '{}'".format(a)
        cur.execute(sql)
        datos = cur.fetchall()  #
        cur.close()
        return datos

    def Buscar_completo(self):
        cur = self.cnn.cursor()
        a = "completo"
        self.tu = a
        sql = "select * from pasante where turno = '{}'".format(a)
        cur.execute(sql)
        datos = cur.fetchall()  #
        cur.close()
        return datos

    def Buscar_tecnica(self):
        cur = self.cnn.cursor()
        a = "tec"
        self.te = a
        sql = "select * from pasante where carrera LIKE '%{}%'".format(a)
        cur.execute(sql)
        datos = cur.fetchall()  #
        cur.close()
        return datos

    def Buscar_comunicacion(self):
        cur = self.cnn.cursor()
        a = "comuni"
        self.co = a
        sql = "select * from pasante where carrera LIKE '%{}%'".format(a)
        cur.execute(sql)
        datos = cur.fetchall()  #
        cur.close()
        return datos

    def Buscar_prensa(self):  # id
        cur = self.cnn.cursor()
        a = "prensa"
        sql = "select * from pasante where area = '{}'".format(a)
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()
        return datos

    def Buscar_Contrato(self):
        cur = self.cnn.cursor()
        a = "contrato"
        sql = "select * from pasante where tcontrato = '{}'".format(a)
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()
        return datos

    def Buscar_Pasante(self):
        cur = self.cnn.cursor()
        a = "pasa"
        sql = "select * from pasante where tcontrato LIKE '%{}%'".format(a)
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()
        return datos

    def Buscar_Produccion(self):
        cur = self.cnn.cursor()
        a = "produ"
        sql = "select * from pasante where area LIKE '%{}%'".format(a)
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()
        return datos

    def Buscar_CI_Contrato(self,ci):
        cur = self.cnn.cursor()
        a = "contr"
        sql = "select tcontrato from pasante where ci LIKE '{}'".format(ci) +"and tcontrato LIKE '%{}%'".format(a)
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()
        return datos

    def Buscar_CI_CONTRATO2(self,ci):
        cur = self.cnn.cursor()
        a = "CONTRATO"
        sql = "select tcontrato from pasante where ci LIKE '{}'".format(ci) +"and tcontrato LIKE '{}%'".format(a)
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()
        return datos

    def Buscar_CI_Pasante(self,ci):
        cur = self.cnn.cursor()
        a = "pasa"
        sql = "select tcontrato from pasante where ci LIKE '{}'".format(ci) + "and tcontrato LIKE '%{}%'".format(a)
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()
        return datos

    def Buscar_CI_PASANTE2(self,ci):
        cur = self.cnn.cursor()
        a = "PASANTE"
        sql = "select tcontrato from pasante where ci LIKE '{}'".format(ci) + "and tcontrato LIKE '%{}%'".format(a)
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()
        return datos

    def buscar_Mes(self, cip): #id
        cur = self.cnn.cursor()
        sql = "SELECT fecha_a FROM asistencia WHERE cip = {}".format(cip)
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()
        return datos

    #******BUSCAR DATOS POR MES************************************************
    def buscar_Mes_Enero(self, cip): #id
        cur = self.cnn.cursor()
        sql = "SELECT * FROM asistencia WHERE fecha_a LIKE '%/01/%'"+"and cip like {}".format(cip)
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()
        return datos

    def buscar_Mes_Febrero(self, cip): #id
        cur = self.cnn.cursor()
        sql = "SELECT * FROM asistencia WHERE fecha_a LIKE '%/02/%'"+"and cip like {}".format(cip)
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()
        return datos

    def buscar_Mes_Marzo(self, cip): #id
        cur = self.cnn.cursor()
        sql = "SELECT * FROM asistencia WHERE fecha_a LIKE '%/03/%'"+"and cip like {}".format(cip)
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()
        return datos

    def buscar_Mes_Abril(self, cip): #id
        cur = self.cnn.cursor()
        sql = "SELECT * FROM asistencia WHERE fecha_a LIKE '%/04/%'"+"and cip like {}".format(cip)
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()
        return datos

    def buscar_Mes_Mayo(self, cip): #id
        cur = self.cnn.cursor()
        sql = "SELECT * FROM asistencia WHERE fecha_a LIKE '%/05/%'"+"and cip like {}".format(cip)
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()
        return datos

    def buscar_Mes_Junio(self, cip): #id
        cur = self.cnn.cursor()
        sql = "SELECT * FROM asistencia WHERE fecha_a LIKE '%/06/%'"+"and cip like {}".format(cip)
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()
        return datos

    def buscar_Mes_Julio(self, cip): #id
        cur = self.cnn.cursor()
        sql = "SELECT * FROM asistencia WHERE fecha_a LIKE '%/07/%'"+"and cip like {}".format(cip)
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()
        return datos

    def buscar_Mes_Agosto(self, cip): #id
        cur = self.cnn.cursor()
        sql = "SELECT * FROM asistencia WHERE fecha_a LIKE '%/08/%'"+"and cip like {}".format(cip)
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()
        return datos

    def buscar_Mes_Septiembre(self, cip): #id
        cur = self.cnn.cursor()
        sql = "SELECT * FROM asistencia WHERE fecha_a LIKE '%/09/%'"+"and cip like {}".format(cip)
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()
        return datos

    def buscar_Mes_Octubre(self, cip): #id
        cur = self.cnn.cursor()
        sql = "SELECT * FROM asistencia WHERE fecha_a LIKE '%/10/%'"+"and cip like {}".format(cip)
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()
        return datos

    def buscar_Mes_Noviembre(self, cip): #id
        cur = self.cnn.cursor()
        sql = "SELECT * FROM asistencia WHERE fecha_a LIKE '%/11/%'"+"and cip like {}".format(cip)
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()
        return datos

    def buscar_Mes_Diciembre(self, cip): #id
        cur = self.cnn.cursor()
        sql = "SELECT * FROM asistencia WHERE fecha_a LIKE '%/12/%'"+"and cip like {}".format(cip)
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()
        return datos

    #********************************************************************************

    def buscar_HoraDia_Enero(self, cip): #id
        cur = self.cnn.cursor()
        sql = "SELECT hora_dia FROM asistencia WHERE fecha_a LIKE '%/01/%'" + "and cip like {}".format(cip)
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()
        return datos

    def buscar_HoraDia_Febrero(self, cip): #id
        cur = self.cnn.cursor()
        sql = "SELECT hora_dia FROM asistencia WHERE fecha_a LIKE '%/02/%'" + "and cip like {}".format(cip)
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()
        return datos
    def buscar_HoraDia_Marzo(self, cip): #id
        cur = self.cnn.cursor()
        sql = "SELECT hora_dia FROM asistencia WHERE fecha_a LIKE '%/03/%'" + "and cip like {}".format(cip)
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()
        return datos

    def buscar_HoraDia_Abril(self, cip): #id
        cur = self.cnn.cursor()
        sql = "SELECT hora_dia FROM asistencia WHERE fecha_a LIKE '%/04/%'" + "and cip like {}".format(cip)
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()
        return datos

    def buscar_HoraDia_Mayo(self, cip): #id
        cur = self.cnn.cursor()
        sql = "SELECT hora_dia FROM asistencia WHERE fecha_a LIKE '%/05/%'" + "and cip like {}".format(cip)
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()
        return datos

    def buscar_HoraDia_Junio(self, cip): #id
        cur = self.cnn.cursor()
        sql = "SELECT hora_dia FROM asistencia WHERE fecha_a LIKE '%/06/%'" + "and cip like {}".format(cip)
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()
        return datos

    def buscar_HoraDia_Julio(self, cip): #id
        cur = self.cnn.cursor()
        sql = "SELECT hora_dia FROM asistencia WHERE fecha_a LIKE '%/07/%'" + "and cip like {}".format(cip)
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()
        return datos

    def buscar_HoraDia_Agosto(self, cip): #id
        cur = self.cnn.cursor()
        sql = "SELECT hora_dia FROM asistencia WHERE fecha_a LIKE '%/08/%'" + "and cip like {}".format(cip)
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()
        return datos

    def buscar_HoraDia_Septiembre(self, cip): #id
        cur = self.cnn.cursor()
        sql = "SELECT hora_dia FROM asistencia WHERE fecha_a LIKE '%/09/%'" + "and cip like {}".format(cip)
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()
        return datos

    def buscar_HoraDia_Octubre(self, cip): #id
        cur = self.cnn.cursor()
        sql = "SELECT hora_dia FROM asistencia WHERE fecha_a LIKE '%/10/%'" + "and cip like {}".format(cip)
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()
        return datos

    def buscar_HoraDia_Noviembre(self, cip): #id
        cur = self.cnn.cursor()
        sql = "SELECT hora_dia FROM asistencia WHERE fecha_a LIKE '%/11/%'" + "and cip like {}".format(cip)
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()
        return datos

    def buscar_HoraDia_Diciembre(self, cip): #id
        cur = self.cnn.cursor()
        sql = "SELECT hora_dia FROM asistencia WHERE fecha_a LIKE '%/12/%'" + "and cip like {}".format(cip)
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()
        return datos

