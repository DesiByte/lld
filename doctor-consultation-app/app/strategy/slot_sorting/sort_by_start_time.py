from .slot_sorting_strategy import SlotSortingStrategy


class SortByStartTime(SlotSortingStrategy):
    def sort_slots(self, slots):
        return sorted(slots, key=lambda slot: slot.start_time)
