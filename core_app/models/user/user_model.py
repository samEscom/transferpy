from sqlalchemy import Boolean, Column, DefaultClause, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.types import DateTime

from core_app.models import Base
from core_app.models.user.user_info import UserInfoModel  # noqa


class UserModel(Base):
    __tablename__ = "user_app"

    user_id = Column("id", Integer, primary_key=True)
    user_name = Column("name", String)
    user_email = Column("email", String)
    user_password = Column("password", String)
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)
    created_at = Column(DateTime, DefaultClause(func.now()), nullable=True)
    updated_at = Column(
        DateTime, DefaultClause(func.now(), for_update=True), nullable=True
    )

    user_info = relationship("UserInfoModel")
