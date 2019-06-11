from core.model.design import Design


class Position:
    """Point position in 3D space"""

    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z


class Waypoint:
    """Waypoint"""

    def __init__(self, position: Position):
        self.position = position


class WaypointPath:
    """Waypoint path information"""

    def __init__(self):
        # List of waypoints
        self.waypoints = []

    def simulate(self, design: Design):
        pass
