from core_app.models.beneficiary.beneficiary_model import BeneficiaryModel
from core_app.queries.base import BaseQueryBuilder


class BeneficiaryQueries(BaseQueryBuilder):
    __model__ = BeneficiaryModel
