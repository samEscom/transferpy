from core_app.models.transfer.transfer_model import TransferModel
from core_app.queries.base import BaseQueryBuilder


class TransferQueries(BaseQueryBuilder):
    __model__ = TransferModel
