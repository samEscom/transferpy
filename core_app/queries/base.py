from typing import ClassVar, Generic, Optional, Type, TypeVar, Union

from core_app.models import Base as BaseModel
from core_app.models import session

BASE_MODEL_TYPE = TypeVar("BASE_MODEL_TYPE", bound=BaseModel)
T = TypeVar("T", bound=BaseModel)
Simple_PK = Union[int, str]


class BaseQueryBuilder(Generic[T]):
    __model__: ClassVar = Type[BaseModel]

    @classmethod
    def get(cls, primary_key: Simple_PK) -> Optional[T]:
        return session.query(cls.__model__).get(primary_key)

    @classmethod
    def add_record(cls, record: T) -> T:
        session.add(record)

        if cls.__in_transaction():
            return record

        session.commit()

        return record

    @classmethod
    def update(cls, record: T) -> T:
        session.merge(record)

        if cls.__in_transaction():
            return record

        session.commit()

        return record

    @classmethod
    def __in_transaction(cls) -> bool:
        return session.info.get("in_transaction", False)

    @classmethod
    def find(cls, filter_input, field_order=None, desc=False, first=False):
        query = session.query(cls.__model__)

        if filter_input:
            query = query.filter(*filter_input)
        if field_order and desc:
            query = query.order_by(field_order.desc())
        if field_order and not desc:
            query = query.order_by(field_order)
        if first:
            return query.first()

        return query
