from typing import List, Optional

from flask import request
from flask_restful import Resource

from core_app.models.transfer.transfer_model import TransferModel
from core_app.queries.transfer import TransferQueries
from core_app.utils.constants import TRANSFER_STATUS_DEFAULT
from flask_jwt_extended import jwt_required, get_jwt_identity


class Transfer(Resource):

    @jwt_required()
    def post(self, id: Optional[int] = None):
        payload = request.get_json()

        if id is not None:
            raise RuntimeError("No operation allowed")

        user_id = get_jwt_identity()
        beneficiary = payload.get("beneficiaryId")
        amount = payload.get("amount")
        transfer_date = payload.get("transferDate")

        transfer: TransferModel = TransferQueries.add_record(
            TransferModel(
                user_id=user_id,
                beneficiary_id=beneficiary,
                status_id=TRANSFER_STATUS_DEFAULT,
                amount=amount,
                date_of_transfer=transfer_date,
            )
        )

        return {
            "id": transfer.id,
            "createdAt": str(transfer.created_at),
            "amount": str(transfer.amount),
            "dateToTransfer": str(transfer.date_of_transfer),
            "status": transfer.status_id,
        }

    @jwt_required()
    def get(self, id: Optional[int] = None):

        if id is not None:
            transfer: TransferModel = TransferQueries.get(id)
            return {
                "id": transfer.id,
                "amount": str(transfer.amount),
                "status": {
                    "id": transfer.status_id,
                    "desc": transfer.status.status,
                },
                "createdAt": str(transfer.created_at),
                "dateToTransfer": str(transfer.date_of_transfer),
                "beneficiary": {
                    "id": transfer.beneficiary.id,
                    "fullname": transfer.beneficiary.full_name,
                },
                "userOrigin": {
                    "id": transfer.user.user_id,
                    "email": transfer.user.user_email,
                },
                "isActive": transfer.is_active,
            }

        all_transfer: List[TransferModel] = TransferQueries.find(None).all()

        return [
            {
                "id": transfer.id,
                "amount": str(transfer.amount),
                "status": {
                    "id": transfer.status_id,
                    "desc": transfer.status.status,
                },
                "createdAt": str(transfer.created_at),
                "dateToTransfer": str(transfer.date_of_transfer),
                "beneficiary": {
                    "id": transfer.beneficiary.id,
                    "fullname": transfer.beneficiary.full_name,
                },
                "userOrigin": {
                    "id": transfer.user.user_id,
                    "email": transfer.user.user_email,
                },
                "isActive": transfer.is_active,
            }
            for transfer in all_transfer
        ]

    @jwt_required()
    def patch(self, id: Optional[int] = None):

        if id is None:
            raise RuntimeError("Operation not allowed")

        transfer: TransferModel = TransferQueries.get(int(id))

        payload = request.get_json()

        beneficiary = payload.get("beneficiaryId")
        amount = payload.get("amount")
        transfer_date = payload.get("transferDate")
        status_id = payload.get("statusId")

        if beneficiary is not None:
            transfer.beneficiary_id = beneficiary

        if amount is not None:
            transfer.amount = amount

        if transfer_date is not None:
            transfer.date_of_transfer = transfer_date

        if status_id is not None:
            transfer.status_id = status_id

        transfer_updated: TransferModel = TransferQueries.update(transfer)
        return {
            "id": transfer_updated.id,
            "amount": str(transfer_updated.amount),
            "status": {
                "id": transfer_updated.status_id,
                "desc": transfer_updated.status.status,
            },
            "createdAt": str(transfer_updated.created_at),
            "dateToTransfer": str(transfer_updated.date_of_transfer),
            "beneficiary": {
                "id": transfer_updated.beneficiary.id,
                "fullname": transfer_updated.beneficiary.full_name,
            },
            "userOrigin": {
                "id": transfer_updated.user.user_id,
                "email": transfer_updated.user.user_email,
            },
            "isActive": transfer_updated.is_active,
        }

    @jwt_required()
    def delete(self, id: Optional[int] = None):

        if id is None:
            raise RuntimeError("Operation not allowed")

        transfer: TransferModel = TransferQueries.get(int(id))
        transfer.is_active = 0

        return {"isActive": TransferQueries.update(transfer).is_active}
