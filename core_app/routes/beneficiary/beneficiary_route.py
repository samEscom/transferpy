from flask import request
from flask_restful import Resource

from core_app.models import session


class Beneficiary(Resource):
    def post(self):
        payload = request.get_json()

        return payload
