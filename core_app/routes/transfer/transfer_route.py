from typing import Optional
from flask import request
from flask_restful import Resource

from core_app.models.transfer.transfer_model import TransferModel
from core_app.utils.constants import TRANSFER_STATUS_DEFAULT
from core_app.models import session


class Transfer(Resource):

    def post(self, id: Optional[int] = None):
        payload = request.get_json()

        if id is not None:
            raise RuntimeError("No operation allowed")

        user = payload.get("userId")
        beneficiary = payload.get("beneficiaryId")
        amount = payload.get("amount")
        transfer_date = payload.get("transferDate")

        transfer = TransferModel(
            user_id=user,
            beneficiary_id=beneficiary,
            status_id=TRANSFER_STATUS_DEFAULT,
            amount=amount,
            date_of_transfer=transfer_date
        )
        session.add(transfer)
        session.commit()

        return {
            "id": transfer.id,
            "createdAt": str(transfer.created_at),
            "amount": str(transfer.amount),
            "dateToTransfer": str(transfer.date_of_transfer),
            "status": transfer.status_id,
        }

    def get(self, id: Optional[int] = None):

        if id is not None:
            return "in process"

        all_transfer = session.query(TransferModel).all()

        return [
            {
                "id": transfer.id,
                "amount": str(transfer.amount),
                "status": transfer.status_id,
                "createdAt": str(transfer.created_at),
                "dateToTransfer": str(transfer.date_of_transfer),
                "beneficiary": {
                    "id": transfer.beneficiary.id,
                    "fullname": transfer.beneficiary.full_name,
                },
                "userOrigin": {
                    "id": transfer.user.user_id,
                    "email": transfer.user.user_email,
                }

            }
            for transfer in all_transfer
        ]

    def patch(self, id: Optional[int] = None):

        if id is not None:
            raise RuntimeError("Operation not allowed")

        return 1

    def delete(self, id: Optional[int] = None):

        if id is not None:
            raise RuntimeError("Operation not allowed")

        return 1