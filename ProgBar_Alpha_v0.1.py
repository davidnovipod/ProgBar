# new program
# ProgBar_Alphav0.1
# The purpose of this program is to take Longitude and Latitude inputs
# and calculate the distance between them.

# Phase 1 - Manual Inpout
# Manual coordinates will be used

# First example code
# http://www.johndcook.com/blog/python_longitude_latitude/
import math
 
def distance_on_unit_sphere(lat1, long1, lat2, long2):
 
    # Convert latitude and longitude to 
    # spherical coordinates in radians.
    degrees_to_radians = math.pi/180.0
         
    # phi = 90 - latitude
    phi1 = (90.0 - lat1)*degrees_to_radians
    phi2 = (90.0 - lat2)*degrees_to_radians
         
    # theta = longitude
    theta1 = long1*degrees_to_radians
    theta2 = long2*degrees_to_radians
         
    # Compute spherical distance from spherical coordinates.
         
    # For two locations in spherical coordinates 
    # (1, theta, phi) and (1, theta', phi')
    # cosine( arc length ) = 
    #    sin phi sin phi' cos(theta-theta') + cos phi cos phi'
    # distance = rho * arc length
     
    cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + 
           math.cos(phi1)*math.cos(phi2))
    arc = math.acos( cos )
 
    # Remember to multiply arc by the radius of the earth 
    # in your favorite set of units to get length.
    return arc

# Second example code
# http://stackoverflow.com/questions/15736995/how-can-i-quickly-estimate-the-distance-between-two-latitude-longitude-points
from math import radians, cos, sin, asin, sqrt
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


# Define some coordinates
# coord1 = [40.933456,-76.872849]
# coord2 = [40.963580,-76.886541]

# print (distance_on_unit_sphere(40.933456, -76.872849, 40.963580, -76.886541))
# print ()
# Test print to make sure we're getting a distance
print (haversine(-76.872849, 40.933456, -76.886541, 40.963580))

# We have our function that calculates distance between two coordinates
# With that we have a zero distance for the progress bar being empty, and
# a max distance for it being full. But we need a third variable that serves
# as the bars current status. After the first input the Start coordinate
# (lat/lon1) and the End coordinate (lat/lon2) won't change. However, the
# third variable will. Because of that we need a the program to check for
# changes in our third variable.

# Let's define our start and end coordinates
lat1  = 0 # Working coordinate 1 latitude
lon1  = 0 # Working coordinate 1 longitude
lat2  = 0 # Working coordinate 2 latitude
lon2  = 0 # Working coordinate 2 longitude
# This is our variable coordinate
lat3  = 0 # Working coordinate 3 latitude
lon3  = 0 # Working coordinate 3 longitude
Tlat3 = 0 # Temp coordinate 3 latitude
Tlon3 = 0 # Temp coordinate 3 longitude



# Let's fill the variables
def set_vars(lat1,lon1,lat2,lon2,lat3,lon3,Tlat3,Tlon3):
    # import stuff to variables here
    # Open arduino file
    arduino_file = open("mostrecentlog.txt", "r")
    # Go to last (most recent) line
    line = arduino_file.seek(0,2)
    # print last line
    print (line)

    # Cut up arduino output and put into variables
    

# Run haversine() to get total distance
    print (haversine(lat1, lon1, lat2, lon2))


# Now we'll be comparing the temp3 to working3
def run_check(lat3,lon3,Tlat3,Tlon3):
    while (lat3 == Tlat3) and (lon3 == Tlon3):
        pass #Do nothing should only run once
    else:
        # run our function with variable
        print (haversine(lat3, lon3, lat2, lon2))
        # update temp varaibles with the current location
        Tlat3 = lat3
        Tlon3 = lon3




