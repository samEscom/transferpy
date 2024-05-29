from flask import Blueprint
from flask_restful import Api

from core_app.routes.beneficiary.beneficiary_route import Beneficiary

beneficiary_blueprint = Blueprint("beneficiary", __name__, url_prefix="/beneficiary")
beneficiary_api = Api(beneficiary_blueprint)

beneficiary_api.add_resource(Beneficiary, "")
