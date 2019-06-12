from uuid import UUID

from flask import Flask, jsonify, request, abort

from core.model import Design
from core.model.process import custom_process
from core.processing import storage, execution

app = Flask(__name__)


def run_server(port: int, debug: bool):
    """
    Start http server
    :param port: Operational port
    :param debug: Debug mode on
    :return:
    """
    app.run(host="0.0.0.0", port=port, debug=True)


@app.route('/designs', methods=['POST'])
def create_design():
    """Create design
    """
    design_request = Design(request.get_json())
    design_response = storage.add_design(design_request.id, design_request)
    return design_response.serialize()


@app.route('/designs/<string:design_id>', methods=['GET'])
def get_design_id(design_id: str):
    """Get design by it's id
    :param design_id: Id of design
    :return:
    """
    design = storage.get_design(UUID(design_id))
    if design is None:
        abort(400)
    return design.serialize()


@app.route('/designs/<string:design_id>/model', methods=['POST'])
def model_design_id(design_id):
    """
    Run design model
    :param design_id: Id of design
    :return:
    """
    existing_design = storage.get_design(UUID(design_id))
    if existing_design is None:
        abort(400)
    # Train new design
    # TODO: Train and return result
    # execution.model(data)
    return ""


@app.route('/designs/<string:design_id>/simulation', methods=['POST'])
def simulate_design_id(design_id):
    """
    Simulate waypoints path
    :param design_id: Id of design
    :return:
    """
    # Get design
    existing_design = storage.get_design(UUID(design_id))
    if existing_design is None:
        abort(400)
    # Generate process
    # TODO: Generate process
    return jsonify(custom_process)
