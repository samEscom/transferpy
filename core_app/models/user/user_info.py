from sqlalchemy import Boolean, Column, DefaultClause, ForeignKey, Integer, String
from sqlalchemy.sql import func
from sqlalchemy.types import DateTime

from core_app.models import Base


class UserInfoModel(Base):
    __tablename__ = "user_info"

    user_info_id = Column("id", Integer, primary_key=True)

    user_app_id = Column(Integer, ForeignKey("user_app.id"))
    user_info_fullname = Column("full_name", String)
    user_info_address = Column("address", String)
    user_info_phone_number = Column("phone_number", String)
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)
    created_at = Column(DateTime, DefaultClause(func.now()), nullable=True)
    updated_at = Column(
        DateTime, DefaultClause(func.now(), for_update=True), nullable=True
    )
