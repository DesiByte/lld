class Payment:
    def __init__(self, payment_id: str, amount: int, appointment_id: str, status: str):
        self.payment_id = payment_id
        self.amount = amount
        self.appointment_id = appointment_id
        self.status = status
