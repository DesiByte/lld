from enum import Enum


class ErrorMessages(Enum):
    SLOT_NOT_AVAILABLE = "The slot is not available."
    SLOT_OVERLAPPING = "Slots overlap detected."
