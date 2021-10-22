from .sorting import Sorting


class BubbleSort(Sorting):
    def __init__(self):
        super().__init__()

    def internal_sort(self, **kwargs):
        if len(self.current_data_to_be_sorted) <= 1:
            return
        any_swap = True
        while any_swap:
            any_swap = False
            for i in range(1, len(self.current_data_to_be_sorted)):
                if self.current_data_to_be_sorted[i-1] > self.current_data_to_be_sorted[i]:
                    self.current_data_to_be_sorted[i-1], self.current_data_to_be_sorted[i] =\
                        self.current_data_to_be_sorted[i], self.current_data_to_be_sorted[i-1]
                    any_swap = True

