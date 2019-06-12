import numpy as np

from core.model.design import RobotConfiguration
from core.processing.execution import possible_positions

items_two_upwards = [
    {
        'id': '14c8a148-a6c4-472d-a662-27d1845eee18',
        'type': 'Beam',
        'length': 1.0
    },
    {
        'id': 'd3263a6d-85b1-4687-b056-0a32b9cdac71',
        'type': 'RotaryJoint',
        'minAngle': 180.0,
        'maxAngle': 180.0,
        'initialAngle': 180.0,
        'rotationY': 0.0,
    },
    {
        'id': 'd5d9a46e-963a-4171-a7c9-47a064eb86f6',
        'type': 'Beam',
        'length': 1.0
    },
]


def test_possible_positions_two_num_iter():
    # Arrange
    rc = RobotConfiguration.from_data(items_two_upwards)
    num_iter = 2

    # Act
    result = possible_positions(rc, num_iter)

    # Assert
    assert len(result) == num_iter


def test_possible_positions_two_upward():
    # Arrange
    rc = RobotConfiguration.from_data(items_two_upwards)

    # Act
    result = possible_positions(rc, 2)

    # Assert
    assert np.array_equal(result[0], np.array([0.0, 0.0, 2.0]))


items_three_upward = [
    {
        'id': '14c8a148-a6c4-472d-a662-27d1845eee18',
        'type': 'Beam',
        'length': 1.0
    },
    {
        'id': 'd3263a6d-85b1-4687-b056-0a32b9cdac71',
        'type': 'RotaryJoint',
        'minAngle': 180.0,
        'maxAngle': 180.0,
        'initialAngle': 180.0,
        'rotationY': 0.0,
    },
    {
        'id': 'd5d9a46e-963a-4171-a7c9-47a064eb86f6',
        'type': 'Beam',
        'length': 1.0
    },
    {
        'id': 'dd64bd90-70fe-4613-a53f-a3bbbed351b4',
        'type': 'RotaryJoint',
        'minAngle': 180.0,
        'maxAngle': 180.0,
        'initialAngle': 180.0,
        'rotationY': 0.0,
    },
    {
        'id': '0420f0e8-2550-4dcf-b6a2-504f6065275f',
        'type': 'Beam',
        'length': 1.0
    },
]


def test_possible_positions_three_upward():
    # Arrange
    rc = RobotConfiguration.from_data(items_three_upward)

    # Act
    result = possible_positions(rc, 2)

    # Assert
    assert np.array_equal(result[0], np.array([0.0, 0.0, 3.0]))


items_three = [
    {
        'id': '14c8a148-a6c4-472d-a662-27d1845eee18',
        'type': 'Beam',
        'length': 1.0
    },
    {
        'id': 'd3263a6d-85b1-4687-b056-0a32b9cdac71',
        'type': 'RotaryJoint',
        'minAngle': 90.0,
        'maxAngle': 270.0,
        'initialAngle': 180.0,
        'rotationY': 0.0,
    },
    {
        'id': 'd5d9a46e-963a-4171-a7c9-47a064eb86f6',
        'type': 'Beam',
        'length': 1.0
    },
    {
        'id': 'dd64bd90-70fe-4613-a53f-a3bbbed351b4',
        'type': 'RotaryJoint',
        'minAngle': 90.0,
        'maxAngle': 270.0,
        'initialAngle': 180.0,
        'rotationY': 0.0,
    },
    {
        'id': '0420f0e8-2550-4dcf-b6a2-504f6065275f',
        'type': 'Beam',
        'length': 1.0
    },
]


def test_possible_positions_three_num_iter():
    # Arrange
    rc = RobotConfiguration.from_data(items_three)
    num_iter = 2

    # Act
    result = possible_positions(rc, num_iter)

    # Assert
    assert len(result) == pow(num_iter, 2)
