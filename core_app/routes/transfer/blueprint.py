from flask import Blueprint
from flask_restful import Api

from core_app.routes.transfer.transfer_route import Transfer

transfer_blueprint = Blueprint("transfer", __name__, url_prefix="/transfer")
transfer_api = Api(transfer_blueprint)

transfer_api.add_resource(Transfer, "", "/<int:id>", endpoint="transfer")
