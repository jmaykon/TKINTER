import pymysql
from tkinter import messagebox
from registroPas import *
class Pasante:
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

    def ordenar_por_apellido(self):
        cur = self.cnn.cursor()
        cur.execute("select * from pasante ORDER BY appaterno asc")
        datos = cur.fetchall()
        cur.close()
        return datos
    def consulta_por_area(self, area):
        cur = self.cnn.cursor()
        sql = "select * from pasante where area = '{}'".format(area)
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()
        return datos
    def consulta_por_carrera(self, carrera):
        cur = self.cnn.cursor()
        sql = "select * from pasante where carrera = '{}'".format(carrera)
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()
        return datos
    def consulta_por_gestion(self, gestion):
        cur = self.cnn.cursor()
        sql = "select * from pasante where gestion = '{}'".format(gestion)
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()
        return datos
    def consulta_por_turno(self, turno):
        cur = self.cnn.cursor()
        sql = "select * from pasante where turno = '{}'".format(turno)
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()
        return datos
    def consulta_por_tContrato(self, tcontrato):
        cur = self.cnn.cursor()
        sql = "select * from pasante where tcontrato = '{}'".format(tcontrato)
        cur.execute(sql)
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
    def registra_pasante(self, ci, nombre, apPat, apMat , carrera, area, cel, tcontrato, fechaini, fechafin, turno, gestion):
        cur = self.cnn.cursor()
        sql = '''INSERT INTO pasante (ci, nombre, appaterno, apmaterno, carrera, area, cel, tcontrato, fechaini, fechafin, turno, gestion)
        VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')'''.format(ci, nombre, apPat, apMat, carrera, area, cel, tcontrato, fechaini, fechafin, turno, gestion)
        cur.execute(sql)
        cur2 = self.cnn.cursor()
        sql2 = ''' UPDATE pasante SET nombre = UPPER(nombre), appaterno = UPPER(appaterno), apmaterno = UPPER(apmaterno), carrera = UPPER(carrera), area = UPPER(area), tcontrato = UPPER(tcontrato) , turno = UPPER(turno) '''
        cur2.execute(sql2)
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
    def eliminar_asistencia(self, clave):
        cur = self.cnn.cursor()
        sql = '''DELETE FROM asistencia WHERE cip = '{}' '''.format(clave) #id
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n
    # metodo para eliminar por seleccion de clave
    def modificar_pasante(self, id, ci, nom, appat, apmat, carr, area, cel, tcontrato, fechaini, fechafin, turno, gestion):
        cur = self.cnn.cursor()
        sql = '''UPDATE pasante SET ci = {}, nombre = '{}', appaterno = '{}', apmaterno = '{}', carrera = '{}', 
        area = '{}', cel = '{}', tcontrato = '{}', fechaini = '{}', fechafin = '{}', turno = '{}', gestion = '{}' WHERE id = {} '''.format(ci, nom, appat, apmat, carr, area, cel, tcontrato, fechaini, fechafin, turno, gestion, id)
        cur.execute(sql)
        cur2 = self.cnn.cursor()
        sql2 = ''' UPDATE pasante SET nombre = UPPER(nombre), appaterno = UPPER(appaterno), apmaterno = UPPER(apmaterno), carrera = UPPER(carrera), area = UPPER(area), tcontrato = UPPER(tcontrato) , turno = UPPER(turno) '''
        cur2.execute(sql2)

        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n