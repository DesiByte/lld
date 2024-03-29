from abc import ABC, abstractmethod


class SlotSortingStrategy(ABC):
    @abstractmethod
    def sort_slots(self, slots):
        pass
