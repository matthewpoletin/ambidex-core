_designs = {}


def add_design(design_id, design):
    """
    Add design into storage
    :param design_id:
    :param design:
    :return:
    """
    _designs[design_id] = design
    return get_design(design_id)


def get_design(design_id):
    """
    Get design from storage
    :type design_id: UUID
    :param design_id:
    :rtype: Design
    :return:
    """
    if design_id not in _designs:
        return None
    return _designs[design_id]
