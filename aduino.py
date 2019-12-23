import serial
ard=serial.Serial('COM5',9600)
while(1):
    c=input()
    if c=='q':
        break
    else:
        c=c.encode('UTF-8')
        ard.write(c)