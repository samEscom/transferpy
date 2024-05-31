from core_app.models.user.user_model import UserModel
from core_app.queries.base import BaseQueryBuilder


class UserAppQueries(BaseQueryBuilder):
    __model__ = UserModel
