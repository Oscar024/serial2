import serial

port = 'COM3'

ser = serial.Serial(port,baudrate=9600,timeout= 2)
print(ser.name + ' is open')
ser.write(b'\x55 \xAA \x01 \x00 \x00 \x00 \x00 \x00 \x01 \x00 \x01 \x01')

ser.close()