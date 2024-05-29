from sqlalchemy import Boolean, Column, DefaultClause, Integer, String
from sqlalchemy.sql import func
from sqlalchemy.types import DateTime

from core_app.models import Base


class LuRelationship(Base):
    __tablename__ = "lu_relationship"

    id = Column(Integer, primary_key=True)
    relationship = Column(String)
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)
    created_at = Column(DateTime, DefaultClause(func.now()), nullable=True)
    updated_at = Column(
        DateTime, DefaultClause(func.now(), for_update=True), nullable=True
    )
