from datetime import datetime

from app.model import Doctor


class Slot:
    def __init__(
        self,
        slot_id: str,
        start_time: datetime,
        end_time: datetime,
        doctor: Doctor,
        status: str,
    ):
        self.slot_id = slot_id
        self.start_time = start_time
        self.end_time = end_time
        self.doctor = doctor
        self.status = status

    def update_slot_status(self, status):
        self.status = status
