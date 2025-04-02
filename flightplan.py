class FlightPlan:
    def __init__(self):
        self.name = ""
        self.waypoints = []

def ShowFlightPlan(flight_plan):
    print('name: {0}, waypoints: {1}'
    .format (
    flight_plan.name,
    flight_plan.waypoints,
    ))
    

def AddWaypoint(flight_plan, waypoint):
    flight_plan.waypoints.append(waypoint)

plan = FlightPlan()
plan.name = "My Flight"
AddWaypoint(plan, "WP1")
AddWaypoint(plan, "WP2")
ShowFlightPlan(plan)