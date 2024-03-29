import uuid

from app.model import Patient


class PatientManager:
    def __init__(self):
        self.patients = {}

    def register_patient(self, payload: dict) -> Patient:
        patient_id = str(uuid.uuid4())
        patient = Patient(
            patient_id=patient_id,
            name=payload["name"],
            date_of_birth=payload["date_of_birth"],
            gender=payload["gender"],
            mobile_number=payload["mobile_number"],
            email=payload["email"],
        )
        self.patients[patient.patient_id] = patient
        return patient
