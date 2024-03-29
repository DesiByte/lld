from enum import Enum


class SlotStatus(Enum):
    AVAILABLE = "available"
    RESERVED = "reserved"
    BOOKED = "booked"
    ON_GOING = "on_going"
    CANCELLED = "cancelled"
    COMPLETED = "completed"
