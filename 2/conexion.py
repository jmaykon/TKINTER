import mysql.connector

class Registro_datos():

    def __init__(self):
        self.conexion = mysql.connector.connect( host='127.0.0.1',
                                            database ='bdmcdd',
                                            user = 'root',port = 3306,
                                            password ='root')
    def busca_users(self, Usuario):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM administrador WHERE usuario = {}".format(Usuario)
        cur.execute(sql)
        usersx = cur.fetchall()
        cur.close()
        return usersx

    def busca_password(self, password):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM administrador WHERE password = {}".format(password) #
        cur.execute(sql)
        passwordx = cur.fetchall()
        cur.close()
        return passwordx