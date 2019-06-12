import uuid

from core.model import Design


def test_deserialize_correct():
    # Arrange
    data = {
        'id': 'a5346c0c-95f4-44c7-8389-33ac1ec21018',
        'name': 'Design name',
        'description': 'Design description',
        'author': 'John Doe',
    }

    # Act
    design = Design(data)

    # Assert
    assert design.id == uuid.UUID("a5346c0c-95f4-44c7-8389-33ac1ec21018")
    assert design.name == 'Design name'
    assert design.description == 'Design description'
    assert design.author == 'John Doe'


def test_serialize_correct():
    # Arrange
    data = {
        'id': 'a5346c0c-95f4-44c7-8389-33ac1ec21018',
        'name': 'Design name',
        'description': 'Design description',
        'author': 'John Doe',
    }
    design = Design(data)
    expected_string = ""

    # Act
    deserialized_string = ""

    # Assert
    assert deserialized_string == expected_string
