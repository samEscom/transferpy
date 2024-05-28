from flask import request
from flask_restful import Resource


class HealthCheck(Resource):
    def get(self):
        return {
            'status': 'OK'
        }
