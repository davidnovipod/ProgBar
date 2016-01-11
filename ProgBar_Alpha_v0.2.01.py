# new program
# ProgBar_Alphav0.1
# The purpose of this program is to take Longitude and Latitude inputs
# and calculate the distance between them.

# Second example code
# http://stackoverflow.com/questions/15736995/how-can-i-quickly-estimate-the-distance-between-two-latitude-longitude-points
from math import radians, cos, sin, asin, sqrt
from time import sleep
import serial


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
    print ('c:', c)
    km = 6367 * c
    print ("km:", km)
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
        print (lat3,lon3)

# Define some coordinates
# coord1 = [40.933456,-76.872849]
# coord2 = [40.963580,-76.886541]

# print (distance_on_unit_sphere(40.933456, -76.872849, 40.963580, -76.886541))
# print ()
# Test print to make sure we're getting a distance
#print (haversine(-76.872849, 40.933456, -76.886541, 40.963580))

# We have our function that calculates distance between two coordinates
# With that we have a zero distance for the progress bar being empty, and
# a max distance for it being full. But we need a third variable that serves
# as the bars current status. After the first input the Start coordinate
# (lat/lon1) and the End coordinate (lat/lon2) won't change. However, the
# third variable will. Because of that we need a the program to check for
# changes in our third variable.



# Let's define our start and end coordinates
"""
lat1  = float(input('Please enter Start Point Latitude:')) # Working coordinate 1 latitude
lon1  = float(input('Please enter Start Point Longitude:')) # Working coordinate 1 longitude
lat2  = float(input('Please enter End Point Latitude:')) # Working coordinate 2 latitude
lon2  = float(input('Please enter End Point Longitude:')) # Working coordinate 2 longitude
"""
#"""
lat1  = 40.933456   # Working coordinate 1 latitude
lon1  = -76.872849  # Working coordinate 1 longitude
lat2  = 40.963580   # Working coordinate 2 latitude
lon2  = -76.886541  # Working coordinate 2 longitude
#"""
print (lat1, lon1)
print (lat2, lon2)

# Run haversine() to get total distance
totalDis = abs(haversine(lat1, lon1, lat2, lon2))
print (totalDis)
endTrigger = float(input("Arrival Notification (distance):"))

# This is our variable coordinate
#lat3  = 0 # Stored coordinate 3 latitude
#3lon3  = 0 # Stored coordinate 3 longitude
Tlat3 = 0 # Temp coordinate 3 latitude
Tlon3 = 0 # Temp coordinate 3 longitude


"""
# Now we'll be comparing the variable point to the end point
def run_check(lat3,lon3,Tlat3,Tlon3):
    
    while (lat3 == Tlat3) and (lon3 == Tlon3):
        pass #Do nothing should only run once
    else:
        # run our function with variable
        print (haversine(lat3, lon3, lat2, lon2))
        # update temp varaibles with the current location
        Tlat3 = lat3
        Tlon3 = lon3
"""
currentDis = totalDis
if currentDis >= endTrigger:
    # Test code for manual variable change
    Tlat3 = float(input("Variable Point Latitude:")) # Temp coordinate 3 latitude
    Tlon3 = float(input("Variable Point Longitude:")) # Temp coordinate 3 longitude

    #arduinoPull(True)

    # run our function with variable
    currentDis = haversine(Tlat3, Tlon3, lat2, lon2)
    print ('Current distance:', currentDis)
else:
    print (currentDis)
    print ("You have arrived!")




