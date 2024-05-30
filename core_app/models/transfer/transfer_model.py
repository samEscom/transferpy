from sqlalchemy import (
    Column,
    Date,
    DefaultClause,
    ForeignKey,
    Integer,
    Numeric,
    SmallInteger,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.types import DateTime

from core_app.models import Base
from core_app.models.beneficiary.beneficiary_model import BeneficiaryModel  # noqa
from core_app.models.look_up.lu_transfer_status import LuTransferStatus  # noqa
from core_app.models.user.user_model import UserModel  # noqa


class TransferModel(Base):
    __tablename__ = "transfer"

    id = Column(Integer, primary_key=True)
    user_id = Column("user_app_id", Integer, ForeignKey("user_app.id"))
    beneficiary_id = Column(Integer, ForeignKey("beneficiary.id"))
    status_id = Column(Integer, ForeignKey("lu_transfer_status.id"))
    amount = Column(Numeric)
    date_of_transfer = Column(Date)

    is_active = Column(SmallInteger, DefaultClause("1"), nullable=False)
    created_at = Column(DateTime, DefaultClause(func.now()), nullable=True)
    updated_at = Column(
        DateTime, DefaultClause(func.now(), for_update=True), nullable=True
    )

    status = relationship("LuTransferStatus")
    user = relationship("UserModel")
    beneficiary = relationship("BeneficiaryModel")
