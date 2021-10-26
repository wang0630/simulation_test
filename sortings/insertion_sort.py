from .inversion_count_merge_sort import InversionCountMergeSort


class InsertionSort(InversionCountMergeSort):
    def __init__(self):
        super().__init__()

    def internal_sort(self, **kwargs):
        if "end_index" not in kwargs:
            raise KeyError("end_index is missing in InsertionSort.internal_sort")

        end_index = kwargs["end_index"]
        if end_index == 0:
            return
        self.internal_sort(end_index=end_index-1)
        self.insert(end_index)

    def insert(self, b):
        for i in range(b):
            if self.current_data_to_be_sorted[i] > self.current_data_to_be_sorted[b]:
                target = self.current_data_to_be_sorted[b]
                prev = self.current_data_to_be_sorted[i]
                for j in range(i, b):
                    current = self.current_data_to_be_sorted[j+1]
                    self.current_data_to_be_sorted[j+1] = prev
                    prev = current
                self.current_data_to_be_sorted[i] = target
                return
