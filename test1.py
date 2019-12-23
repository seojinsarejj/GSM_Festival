import serial

ARD = serial.Serial('COM4', 9600)

ARD.write('1'.encode())
print("done")