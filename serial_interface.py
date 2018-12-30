# This file was created using python 3.5, on ubuntun 16.04 note you need to install pyserial to use it.
import serial

class LoRaInterface:
    def __init__(self, comport):
        # You will need to replace this string with the location of your comport
        self.s = serial.Serial(comport)

    def write(self, data):
        self.s.write(data.encode('utf-8'))

    def read_100(self):
        return self.s.read(100)

    def readline(self):
        return self.s.readline()


# example usage
l = LoRaInterface('/dev/ttyACM0')
l.write('Test data')

while(True):
    print('Data is ' + str(l.readline()))
