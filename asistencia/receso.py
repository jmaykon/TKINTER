import pymysql
from tkinter import messagebox
from registroPas import *

'''
cnn = pymysql.connect(host="127.0.0.1", user="root", passwd="root", port=3306, database="bdmcdd")

cur = cnn.cursor()
cur.execute("select * from pasante")
datos = cur.fetchall()

for fila in datos:
    print(fila)
#print(cnn)
'''
class Receso:
    def __init__(self):
        self.cnn = pymysql.connect(host="127.0.0.1", user="root", passwd="root", port=3306, database="bdmcdd")
    def __str__(self):
        datos = self.consulta_receso()
        aux = ""
        for fila in datos:
            aux = aux + str(fila) + "\n"
        return aux
    def consulta_receso(self):
        cur = self.cnn.cursor()
        cur.execute("select * from receso")
        datos = cur.fetchall()
        cur.close()
        return datos
    def buscar_asistencia(self, cip): #id
        cur = self.cnn.cursor()
        sql = "select * from receso where cip = {}".format(cip)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()
        return datos
    def buscar_asistencia_nomFe(self, cip, fecha_a): #id
        cur = self.cnn.cursor()
        sql = "SELECT * FROM receso where fecha_a = '{}' AND cip = {} ".format(fecha_a, cip) # tener cuidado en la consulta Where  '{String}' y {int}
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()
        return datos
    def buscar_HoraDia(self, cip): #id
        cur = self.cnn.cursor()
        sql = "SELECT hora_dia FROM receso WHERE cip = {}".format(cip)
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()
        return datos
    def registra_asistencia(self, cip, hora_e, hora_s, hora_dia, fecha_a):
        cur = self.cnn.cursor()
        sql = '''INSERT INTO receso (cip, hora_entrada, hora_salida, hora_dia, fecha_a)
        VALUES('{}', '{}', '{}', '{}', '{}')'''.format(cip, hora_e, hora_s, hora_dia, fecha_a)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n
    def eliminar_asistencia(self, clave):
        cur = self.cnn.cursor()
        sql = '''DELETE FROM receso WHERE cip = '{}' '''.format(clave) #id
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n
    # metodo para eliminar por seleccion de clave
    def modificar_asistencia(self, cip, hora_entrada, hora_salida, hora_dia, fecha_a):
        cur = self.cnn.cursor()
        sql = '''UPDATE receso SET hora_entrada = '{}', hora_salida = '{}', hora_dia = '{}' WHERE fecha_a = '{}' AND cip = {} '''.format(hora_entrada, hora_salida, hora_dia, fecha_a, cip)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n