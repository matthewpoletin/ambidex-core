from uuid import UUID


class PartData:
    """Information about part"""

    def __init__(self, id: UUID,
                 part_type: str,
                 rotation_y: float = 0.0,
                 min_angle: float = 0.0,
                 max_angle: float = 360.0,
                 initial_angle: float = 180.0,
                 length: float = 1.0,
                 diameter: float = 1.0
                 ):
        self.id = id
        self.type = part_type
        self.rotation_y = rotation_y
        self.min_angle = min_angle
        self.max_angle = max_angle
        self.initial_angle = initial_angle
        self.length = length
        self.diameter = diameter


class RobotConfiguration:
    """Configuration of robot"""

    def __init__(self, items: list):
        self.items = items
        pass

    @classmethod
    def from_data(cls, data: list):
        parts = []
        for item in data:
            part_object = PartData(
                id=UUID(item['id']),
                part_type=item['type'],
                min_angle=item.get('minAngle'),
                max_angle=item.get('maxAngle'),
                initial_angle=item.get('initialAngle'),
                rotation_y=item.get('rotationY'),
                length= item.get('length'),
                diameter=item.get('diameter'),
            )
            parts.append(part_object)
        return cls(parts)
