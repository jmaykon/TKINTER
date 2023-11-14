from tkinter import Tk
import login
import login2
import menu


def mostrar_login():
    ventana = Tk()
    ventana.config(bg='gray63')
    ventana.geometry('350x650+500+50')
    ventana.overrideredirect(1)
    ventana.resizable(0, 0)
    app = login.Login(ventana)
    app.mainloop()


def mostrar_login2() -> object:
    ventana2 = Tk()
    ventana2.config(bg='gray63')
    ventana2.geometry('350x800+500+50')
    ventana2.overrideredirect(1)
    ventana2.resizable(0, 0)
    app = login2.Login2(ventana2)
    app.mainloop()


def mostrar_menu():
    Men1 = Tk()
    Men1.wm_title("Menu Administrador")
    Men1.geometry('410x450+500+50')
    app = menu.Menu(Men1)
    app.mainloop()


if __name__ == "__main__":
    mostrar_login()
