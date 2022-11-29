import serial
import time

arduino = serial.Serial("COM14", 57600)
time.sleep(2)
#dev = serial.Serial("COM14", 57600)
while True:
    #rawString = arduino.readline().decode('ascii')
    cad = arduino.readline().decode('ascii')
    print(cad)
