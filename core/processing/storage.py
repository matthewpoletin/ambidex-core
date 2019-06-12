from uuid import UUID

from core.model import Design

_designs = {}


def add_design(design_id: UUID, design: Design):
    """
    Add design into storage

    :param design_id: Id of design
    :param design: Design
    :return: Design representation
    """
    _designs[design_id] = design
    return get_design(design_id)


def get_design(design_id: UUID) -> Design:
    """
    Get design from storage

    :param design_id: Id of design
    :return: Design
    """
    if design_id not in _designs:
        return None
    return _designs[design_id]
