# new program
# ProgBar_Alphav0.3
# The purpose of this program is to take Longitude and Latitude inputs
# and calculate the distance between them.

from math import radians, cos, sin, asin, sqrt
from time import sleep
import serial

#Function for calculating distance between two coordinates
def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    km = 6367 * c
    return km


def arduinoPull(bool):
    if True:
        ser = serial.Serial('/dev/cu.usbserial-DA01KZ3C', 115200) # Establish the connection on a specific port
        ser.inWaiting()==0 #Wait here until there is data
        rawString = str(ser.readline())
        String = rawString.replace('b','').replace('r','').replace('n','').replace('\\','').replace("'",'')
        locationArray = String.split(',')
        lat3 = float( locationArray[0])
        lon3 = float( locationArray[1])
        return (lat3, lon3)


def locationCheck(currentDis):
    while currentDis >= endTrigger:
        # Test code for manual variable change
        #lat3 = float(input("Variable Point Latitude:")) # Temp coordinate 3 latitude
        #lon3 = float(input("Variable Point Longitude:")) # Temp coordinate 3 longitude

        lat3, lon3 = arduinoPull(True)
        
        # run our function with variable
        print ('Coords', lat3, lon3)
        currentDis = haversine(lat3, lon3, lat2, lon2)
        print ('Current distance:', currentDis)
    else:
        print (currentDis)
        print ("You have arrived!")
    
#-----------------------------------------------------

# Let's define our start and end coordinates
#"""
lat1  = 40.933456   # Working coordinate 1 latitude
lon1  = -76.872849  # Working coordinate 1 longitude
lat2  = 40.963580   # Working coordinate 2 latitude
lon2  = -76.886541  # Working coordinate 2 longitude
lat3 = 0 # Temp coordinate 3 latitude
lon3 = 0 # Temp coordinate 3 longitude
endTrigger = float(input("Arrival Notification (distance):"))
totalDis = abs(haversine(lat1, lon1, lat2, lon2))
print (totalDis)
currentDis = totalDis
print (currentDis)
#"""
"""
lat1  = float(input('Please enter Start Point Latitude:')) # Working coordinate 1 latitude
lon1  = float(input('Please enter Start Point Longitude:')) # Working coordinate 1 longitude
lat2  = float(input('Please enter End Point Latitude:')) # Working coordinate 2 latitude
lon2  = float(input('Please enter End Point Longitude:')) # Working coordinate 2 longitude
lat3 = 0 # Temp coordinate 3 latitude
lon3 = 0 # Temp coordinate 3 longitude
endTrigger = float(input("Arrival Notification (distance):"))
totalDis = abs(haversine(lat1, lon1, lat2, lon2))
print (totalDis)
currentDis = totalDis
print (currentDis)
"""
    
#-----------------------------------------------------

print ('Here we go')
locationCheck(currentDis)
#haversine(40.9335, -76.8729, 40.963580, -76.886541)
