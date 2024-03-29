import uuid
from collections import defaultdict
from datetime import datetime

from app.constants import AppointmentStatus, ErrorMessages, SlotStatus
from app.manager import SlotManager
from app.model import Appointment


class AppointmentManager:
    def __init__(self, slot_manager: SlotManager):
        self.appointments = {}
        self.patient_wise_appointments = defaultdict(list)
        self.doctor_wise_appointments = defaultdict(list)
        self.slot_manager = slot_manager

    def _is_valid_slot(self, slot):
        return slot.status in [SlotStatus.AVAILABLE.value, SlotStatus.CANCELLED.value]

    def _is_slot_overlap(self, slot1, slot2):
        return (slot1.start_time < slot2.end_time) and (
            slot2.start_time < slot1.end_time
        )

    def _check_valid_appointment(self, slot, patient_id):
        appointments = self.patient_wise_appointments.get(patient_id, [])
        if not self._is_valid_slot(slot):
            raise Exception(ErrorMessages.SLOT_NOT_AVAILABLE.value)

        for appointment in appointments:
            if (
                self._is_slot_overlap(slot, appointment.slot)
                and appointment.status != AppointmentStatus.CANCELLED_BY_PATIENT.value
            ):
                raise Exception(ErrorMessages.SLOT_OVERLAPPING.value)
        return True

    def create_appointment(self, payload):
        appointment_id = str(uuid.uuid4())
        patient_id = payload["patient_id"]
        slot = self.slot_manager.get_slot(payload["slot_id"])
        self._check_valid_appointment(slot, patient_id)
        slot.update_slot_status(SlotStatus.BOOKED.value)
        appointment = Appointment(
            appointment_id,
            payload["doctor_id"],
            payload["patient_id"],
            slot,
            datetime.now(),
            AppointmentStatus.SCHEDULED.value,
        )
        self.appointments[appointment_id] = appointment
        self.patient_wise_appointments[patient_id].append(appointment)
        self.doctor_wise_appointments[patient_id].append(appointment)
        return appointment

    def cancelled_appointment(self, appointment_id: str):
        appointment = self.appointments[appointment_id]
        appointment.update_status(AppointmentStatus.CANCELLED_BY_PATIENT.value)
        appointment.slot.update_slot_status(SlotStatus.AVAILABLE.value)
