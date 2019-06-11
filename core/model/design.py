from uuid import UUID

from flask import jsonify

from core.anfis.network import AnfisNetwork


class Design:
    """Design data"""

    def __init__(self, data):
        self.id = UUID(data['id'])
        self.name = data['name']
        self.author = data['author']
        self.description = data['description']
        self.network = None

    def train(self):
        # Create network
        self.network = AnfisNetwork(4, 16, 0.01)
        pass

    def serialize(self):
        """
        Create serialization for design

        :return: Json variant of design
        """
        return jsonify({
            'id': self.id,
            'name': self.name,
            'author': self.author,
            'description': self.description,
        })
