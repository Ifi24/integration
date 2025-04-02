from waypoint import Waypoint
from flightplan import FlightPlan, ShowFlightPlan

myPlan = FlightPlan("myPlan")

w1 = Waypoint ('Camp Nou', 41.381623923229995, 2.122853541678448)
w2 = Waypoint ('Santiago Bernabeu', 40.453030507454244, -3.6883551609249308)
w3 = Waypoint ('Balaidos', 42.211904178262195, -8.739772189675971)
w4 = Waypoint ('Sanchez Pizjuan', 37.38276157689335, -5.971691936532935)
waypoints = [w1, w2, w3, w4]


for wp in waypoints:
    myPlan.AddWaypoint(wp)

ShowFlightPlan(myPlan)