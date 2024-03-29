from enum import Enum


class AppointmentStatus(Enum):
    SCHEDULED = "scheduled"
    CONFIRMED = "confirmed"
    CANCELLED_BY_PATIENT = "cancelled_by_patient"
    CANCELLED_BY_DOCTOR = "cancelled_by_doctor"
    COMPLETED = "completed"
