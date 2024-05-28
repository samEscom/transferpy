from flask import request
from flask_jwt_extended import create_access_token
from flask_restful import Resource

from core_app.models import session
from core_app.models.user.user_model import UserModel
from core_app.utils.users import str_to_hash


class Login(Resource):
    def post(self):
        payload = request.get_json()

        email = payload.get("email")
        password = str_to_hash(payload.get("password"))

        user: UserModel = (
            session.query(UserModel)
            .filter(UserModel.user_email == email, UserModel.user_password == password)
            .first()
        )

        if user is None:
            return "error on user or password"

        access_token = create_access_token(identity=user.user_id)
        return {
            "token": access_token,
        }
