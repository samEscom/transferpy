from core_app.models.user.user_info import UserInfoModel
from core_app.queries.base import BaseQueryBuilder


class UserInfoQueries(BaseQueryBuilder):
    __model__ = UserInfoModel
