import uuid


class Speciality:
    def __init__(self, name: str):
        self.speciality_id = str(uuid.uuid4())
        self.name = name
