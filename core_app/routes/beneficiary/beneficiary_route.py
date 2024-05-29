from flask import request
from flask_restful import Resource

from core_app.models import session
from core_app.models.beneficiary.beneficiary_model import BeneficiaryModel


class Beneficiary(Resource):
    def post(self):
        payload = request.get_json()

        full_name = payload.get("fullname")
        gender_id = payload.get("genderId")
        relationship_id = payload.get("relationshipId")
        date_of_birthday = payload.get("dateOfBirthday")

        beneficiary = BeneficiaryModel(
            full_name=full_name,
            gender_id=gender_id,
            relationship_id=relationship_id,
            date_of_birthday=date_of_birthday,
        )

        session.add(beneficiary)
        session.commit()

        return {
            "id": beneficiary.id,
            "fullName": beneficiary.full_name,
            "dateOfBirthday": str(beneficiary.date_of_birthday),
            "gender": {
                "id": beneficiary.gender_id,
                "gender": beneficiary.gender.gender,
            },
            "relationship": {
                "id": beneficiary.relationship_id,
                "relationship": beneficiary.relationship_beneficiary.relationship,
            },
            "isActive": beneficiary.is_active,
            "createdAt": str(beneficiary.created_at),
        }
