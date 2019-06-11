from enum import Enum, auto


class PartType(Enum):
    """Types of parts"""
    UNDEFINED = 0

    ROTARY_JOINT = auto()
    REVOLUTE_JOINT = auto()

    BEAM = auto()
    TIP = auto()


class PartData:
    """Definition of part"""

    def __init__(self, part_type: PartType):
        """
        :type part_type: PartType
        """
        self.type = part_type
