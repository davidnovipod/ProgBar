from time import sleep
import serial

ser = serial.Serial('/dev/cu.usbserial-DA01KZ3C', 115200) # Establish the connection on a specific port

def arduinoPull(bool):
    if True:
        ser = serial.Serial('/dev/cu.usbserial-DA01KZ3C', 115200) # Establish the connection on a specific port
        ser.inWaiting()==0 #Wait here until there is data
        rawString = str(ser.readline())
        String = rawString.replace('b','').replace('r','').replace('n','').replace('\\','').replace("'",'')
        locationArray = String.split(',')
        lat3 = float( locationArray[0])
        lon3 = float( locationArray[1])
        print (lat3,lon3)

print (arduinoPull(True))
