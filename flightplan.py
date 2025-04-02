from waypoint import Waypoint, ShowWaypoint

class FlightPlan:
    def __init__(self, name):
        self.name = name
        self.waypoints = []

    def AddWaypoint(self, waypoint):
        self.waypoints.append(waypoint)

def ShowFlightPlan(flight_plan):
    print(f"Flight Plan: {flight_plan.name}")
    for wp in flight_plan.waypoints:
        ShowWaypoint(wp)
