from flask import request
from flask_restful import Resource

from core_app.models import session
from core_app.models.user.user_model import UserModel
from core_app.utils.users import str_to_hash


class Register(Resource):
    def post(self):
        payload = request.get_json()

        name = payload.get("name")
        email = payload.get("email")
        password = str_to_hash(payload.get("password"))

        user = UserModel(user_name=name, user_email=email, user_password=password)
        session.add(user)
        session.commit()

        return {
            "id": user.user_id,
            "name": user.user_name,
            "email": user.user_email,
        }
