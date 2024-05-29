from sqlalchemy import Boolean, Column, Date, DefaultClause, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.types import DateTime

from core_app.models import Base
from core_app.models.look_up.lu_gender import LuGender  # noqa
from core_app.models.look_up.lu_relationship import LuRelationship  # noqa


class BeneficiaryModel(Base):
    __tablename__ = "beneficiary"

    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    gender_id = Column(Integer, ForeignKey("lu_gender.id"))
    relationship_id = Column(Integer, ForeignKey("lu_relationship.id"))
    date_of_birthday = Column(Date)

    is_active = Column(Boolean, DefaultClause("1"), nullable=False)
    created_at = Column(DateTime, DefaultClause(func.now()), nullable=True)
    updated_at = Column(
        DateTime, DefaultClause(func.now(), for_update=True), nullable=True
    )

    gender = relationship("LuGender")
    relationship_beneficiary = relationship("LuRelationship")
