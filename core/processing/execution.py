import copy
from uuid import UUID

import numpy as np
from scipy.spatial.transform import Rotation

from core.model import SimulationProcess
from core.model import WaypointPath
from core.model.robot import RobotConfiguration
from core.processing import storage


def process_part(parts: list, index: int, num_iter: int, current_position, current_vector, conf: list, results: list):
    """
    Process part by index

    :param parts: List of parts
    :param index: Index of part to process
    :param num_iter: Number of iterations
    :param current_position: Current position of point
    :param current_vector: Current direction vector
    :param conf: Current configuration of parts
    :param results: List of resulting point
    :return:
    """
    # No more parts to get
    if index >= len(parts):
        results.append({'position': current_position, 'configuration': conf})
        return
    part = parts[index]
    # Part type
    if part.type == "Tip" or part.type == "BasicTip":
        results.append({'position': current_position, 'configuration': conf})
        return

    # Apply rotation Y to part
    if part.rotation_y is not None and part.rotation_y != 0:
        r = Rotation.from_euler('z', part.rotation_y, degrees=True)
        current_vector = r.apply(current_vector)

    # Decide what to do
    if part.type == "Beam":
        some_position = current_position + np.multiply(current_vector, part.length)
        process_part(parts, index + 1, num_iter, some_position, copy.deepcopy(current_vector), copy.deepcopy(conf),
                     results)
        return
    elif part.type == "RotaryJoint":
        for i in range(num_iter):
            angle = part.min_angle + (part.max_angle - part.min_angle) * i / (num_iter - 1)
            r = Rotation.from_euler('x', (180.0 - angle), degrees=True)
            some_vector = r.apply(current_vector)

            conf.append({'id': part.id, 'type': part.type, 'angle': angle})
            # Apply rotation Y to part
            if part.rotation_y is not None and part.rotation_y != 0:
                r = Rotation.from_euler('z', -part.rotation_y, degrees=True)
                some_vector = r.apply(some_vector)

            process_part(parts, index + 1, num_iter, copy.deepcopy(current_position), some_vector, copy.deepcopy(conf),
                         results)
        return
    elif part.type == "RevoluteJoint":
        for i in range(num_iter):
            angle = part.min_angle + (part.max_angle - part.min_angle) * i / (num_iter - 1)
            r = Rotation.from_euler('z', (180.0 - angle), degrees=True)
            some_vector = r.apply(current_vector)
            process_part(parts, index + 1, num_iter, copy.deepcopy(current_position), some_vector, copy.deepcopy(conf),
                         results)
        return


def possible_positions(robot: RobotConfiguration, num_iter: int) -> list:
    """
    Generate all possible positions of robot tip

    :param robot: Configuration of robot
    :param num_iter:
    :return:
    """
    # Initial position in root
    current_position = np.array([0.0, 0.0, 0.0])
    # Vector3.up
    current_vector = np.array([0.0, 0.0, 1.0])
    # List of resulting points
    results = []
    process_part(robot.items, 0, num_iter, current_position, current_vector, [], results)
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
    possible_positions(design.robot, 40)
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
