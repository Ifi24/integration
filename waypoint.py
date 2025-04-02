class Waypoint:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon
    
    #def __str__(self):
    #    return f"({self.name}, {self.lat}, {self.lon})"

def ShowWaypoint(waypoint):
    print('Nombre:{0}, lat:{1}, lon:{2}'
    .format (
    waypoint.name,
    waypoint.lat,
    waypoint.lon
    ))
    
import math
def HaversineDistance(lat1, lon1, lat2, lon2):
    dLat = (lat2 - lat1) * (math.pi/180)
    dLon = (lon2 - lon1) * (math.pi/180)
    lat1 = lat1 * (math.pi/180)
    lat2 = lat2 * (math.pi/180)
    a = pow(math.sin(dLat/2), 2)
    b = pow(math.sin(dLon/2), 2)
    raiz = math.sqrt((a + (math.cos(lat1)) * (math.cos(lat2)) * b))
    c = 2 * math.asin(raiz)
    R = 6371000 #Earths's radius in meters
    return c * R