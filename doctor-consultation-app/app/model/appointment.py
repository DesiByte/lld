from datetime import datetime

from app.model import Slot


class Appointment:
    def __init__(
        self,
        appointment_id: str,
        doctor_id: str,
        patient_id: str,
        slot: Slot,
        created_at: datetime,
        status: str,
    ):
        self.appointment_id = appointment_id
        self.doctor_id = doctor_id
        self.patient_id = patient_id
        self.slot = slot
        self.created_at = created_at
        self.status = status

    def update_status(self, status: str):
        self.status = status
