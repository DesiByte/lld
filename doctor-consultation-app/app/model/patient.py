class Patient:
    def __init__(
        self,
        patient_id: str,
        name: str,
        date_of_birth: str,
        gender: str,
        mobile_number: str,
        email: str,
    ):
        self.patient_id = patient_id
        self.name = name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.mobile_number = mobile_number
        self.email = email
