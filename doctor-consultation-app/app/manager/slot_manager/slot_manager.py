import uuid

from app.constants import SlotStatus
from app.manager import DoctorManager
from app.model import Slot


class SlotManager:
    def __init__(self, doctor_manager: DoctorManager, slot_sorting_strategy) -> None:
        self.slots = {}
        self.doctor_manager = doctor_manager
        self.slot_sorting_strategy = slot_sorting_strategy

    def add_slot(self, payload: dict) -> Slot:
        slot_id = str(uuid.uuid4())
        doctor = self.doctor_manager.get_doctor(doctor_id=payload["doctor_id"])
        slot = Slot(
            slot_id,
            payload["start_time"],
            payload["end_time"],
            doctor,
            SlotStatus.AVAILABLE.value,
        )
        self.slots[slot_id] = slot
        return slot

    def search_slot(self, specialty_name: str) -> list:
        filtered_slots = []
        for slot in self.slots.values():
            if (
                specialty_name == slot.doctor.speciality
                and slot.status == SlotStatus.AVAILABLE.value
            ):
                filtered_slots.append(slot)
        return self.slot_sorting_strategy.sort_slots(filtered_slots)

    def get_slot(self, slot_id: str) -> Slot:
        return self.slots.get(slot_id)
