from builtins import int
from datetime import datetime, date, time, timedelta
import calendar

import tkinter as tk
ventana = tk.Tk()
ventana.geometry('380x300+1200+100')
var = tk.StringVar(ventana)
var.set('prensa')
opciones = ['estudio', 'produccion']
opcion = tk.OptionMenu(ventana, var, *opciones)
opcion.config(width=30)
opcion.place(x=50, y=50)
ventana.mainloop()


formato = "%H:%M:%S"

horaS = "09:40:31"
horaS = datetime.strptime(horaS,formato) #datetime.datetime
h1 = horaS.hour # int
m1 = horaS.minute
s1 = horaS.second
print(h1,m1,s1)
#ahora = datetime.now() # fecha y hora
ahora = "10:10:25"
ahora = datetime.strptime(ahora,formato) #datetime.datetime

h2 = ahora.hour
m2 = ahora.minute
s2 = ahora.second
print(h2,m2,s2)

hh1 = h1 * 60
hm1 = (hh1 + m1)
print("1ra Hora hm1: ",hm1)

hh2 = h2 * 60  #
hm2 = (hh2 + m2)
print("2da Hora hm2: ",hm2)

dhm = hm1 - hm2
if dhm < 0:
    dhm = dhm * (-1)
nh = 0
nm = 0
ns = 0

dhmx = dhm
while nh+nm  < dhm:
    if dhmx < 60:
        nm = dhmx
        dhmx = 0
    else:
        dhmx = dhmx - 60
        nh = nh + 60
nh = int(nh / 60)

###############
mm1 = m1 * 60 # seg
ms1 = mm1 + s1
print("minE = ",ms1)
mm2 = m2 * 60 # seg
ms2 = mm2 + s2
print("minS = ",ms2)

dms = ms2 - ms1
print("minD = ",dms)
sws = 1
if dms < 0:
    dms = dms * (-1)
    sws = -1
print("minD = ",dms)
nmin = 0
nseg = 0

dmsx = dms # 1806

while nmin+nseg < dms:
    if dmsx < 60:
        nseg = dmsx
        print("seg Extra = ", nseg)
        dmsx = 0
    else:
        print("********")
        dmsx = dmsx - 60
        nmin = nmin + 60 # min expresados en segundos
        print("nmin = ", nmin)

nmin = int(nmin / 60)
if sws == (-1):
    nm = nmin - 1
    ns = 60 - nseg
else:
    nm = nmin
print("Total Horas: ",nh,":",nm,":",ns)
