class Doctor:
    def __init__(
        self,
        doctor_id: str,
        name: str,
        mobile_number: str,
        email: str,
        speciality: str,
    ):
        self.doctor_id = doctor_id
        self.name = name
        self.mobile_number = mobile_number
        self.email = email
        self.speciality = speciality
