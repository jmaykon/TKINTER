import serial
import time

arduino = serial.Serial("COM14", 9600, timeout=1.0)
time.sleep(1)
while True:
    #rawString = arduino.readline().decode('ascii')
    cad = arduino.readline().decode('ascii')
    print(cad)



#arduino.close()