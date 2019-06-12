from uuid import UUID

import numpy as np
from scipy.spatial.transform import Rotation as R

from core.model import SimulationProcess
from core.model import WaypointPath
from core.model.robot import RobotConfiguration
from core.processing import storage


def possible_positions(robot: RobotConfiguration, num_iter: int) -> list:
    """
    Generate all possible positions of robot tip

    :param robot: Configuration of robot
    :param num_iter:
    :return:
    """
    joints = []
    # Get all joints to work later with
    for part in robot.items:
        if part.type == "RotaryJoint":
            joints.append(part.id)

    results = []
    for i in range(num_iter):
        # Initial position in root
        current_position = np.array([0.0, 0.0, 0.0])
        # Vector3.up
        current_vector = np.array([0.0, 0.0, 1.0])

        # Go through all items in configuration
        for part in robot.items:
            # Part type
            if part.type == "Beam":
                current_position += np.multiply(current_vector, part.length)
            elif part.type == "RotaryJoint":
                angle = part.min_angle + (part.max_angle - part.min_angle) * i / (num_iter - 1)
                r = R.from_euler('x', (180.0 - angle), degrees=True)
                current_vector = r.apply(current_vector)
            elif part.type == "RevoluteJoint":
                angle = part.min_angle + (part.max_angle - part.min_angle) * i / (num_iter - 1)
                r = R.from_euler('z', (180.0 - angle), degrees=True)
                current_vector = r.apply(current_vector)
                pass

            # TODO: Apply rotation on Y (z) axis
            # Apply rotation Y to part
            # if part.rotation_y is not None and part.rotation_y != 0:
            #     r = R.from_euler('z', part.rotation_y, degrees=True)
            #     current_vector = r.apply(current_vector)
            #     pass

        results.append(current_position)
    return results


def model(design_id: UUID) -> bool:
    """
    Model design

    :param design_id:
    :return:
    """
    # Get design by id
    design = storage.get_design(design_id)
    if design is None:
        return False

    # Generate possible positions
    possible_positions(design.robot, 1)
    # Create anfis network
    # TODO: ?
    return True


def simulate(design_id: int, waypoints: WaypointPath) -> SimulationProcess:
    """
    Execute simulation of design

    :param design_id:
    :param waypoints:
    :return:
    """
    return SimulationProcess()
