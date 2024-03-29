import uuid

from app.model import Doctor


class DoctorManager:
    def __init__(self):
        self.doctors = {}

    def register_doctor(self, payload: dict) -> Doctor:
        doctor_id = str(uuid.uuid4())
        doctor = Doctor(
            doctor_id,
            payload["name"],
            payload["mobile_number"],
            payload["email"],
            payload["speciality"],
        )
        self.doctors[doctor_id] = doctor
        return doctor

    def get_doctor(self, doctor_id: str) -> Doctor:
        return self.doctors[doctor_id]
