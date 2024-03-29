from datetime import datetime, timedelta

from app.manager import (AppointmentManager, DoctorManager, PatientManager,
                         SlotManager)
from app.strategy import SortByStartTime

patient_payload = {
    "name": "John Doe",
    "date_of_birth": "1990-01-01",
    "gender": "Male",
    "mobile_number": "1234567890",
    "email": "john@example.com",
}

doctor_payload = {
    "name": "Dr. John Smith",
    "mobile_number": "9876543210",
    "speciality": "cardiologist",
    "email": "john@example.com",
}
patient_manager = PatientManager()
patient = patient_manager.register_patient(patient_payload)
doctor_manager = DoctorManager()
doctor = doctor_manager.register_doctor(doctor_payload)
doctor_payload = {
    "name": "Dr. John Smith",
    "mobile_number": "9876543210",
    "speciality": "cardiologist",
    "email": "john@example.com",
}
doctor1 = doctor_manager.register_doctor(doctor_payload)
slot_manager = SlotManager(doctor_manager, slot_sorting_strategy=SortByStartTime())
slot = slot_manager.add_slot(
    {
        "doctor_id": doctor.doctor_id,
        "start_time": datetime.now(),
        "end_time": datetime.now() + timedelta(minutes=30),
    }
)
slot1 = slot_manager.add_slot(
    {
        "doctor_id": doctor1.doctor_id,
        "start_time": datetime.now(),
        "end_time": datetime.now() + timedelta(minutes=30),
    }
)
appointment_manager = AppointmentManager(slot_manager)
appointment = appointment_manager.create_appointment({
    "doctor_id": doctor.doctor_id,
    "patient_id": patient.patient_id,
    "slot_id": slot.slot_id,
})
appointment_manager.cancelled_appointment(appointment.appointment_id)
appointment = appointment_manager.create_appointment({
    "doctor_id": doctor.doctor_id,
    "patient_id": patient.patient_id,
    "slot_id": slot.slot_id,
})
