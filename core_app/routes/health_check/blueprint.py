from flask import Blueprint
from flask_restful import Api

from core_app.routes.health_check.health_check_route import HealthCheck

health_blueprint = Blueprint("health", __name__, url_prefix="/health-check")
health_api = Api(health_blueprint)

health_api.add_resource(HealthCheck, "")

