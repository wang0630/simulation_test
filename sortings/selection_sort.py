from .sorting import Sorting


class SelectionSort(Sorting):
    def __init__(self):
        super().__init__()

    def internal_sort(self, **kwargs):
        if "end_index" not in kwargs:
            raise KeyError("end_index is missing in SelectionSort.internal_sort")

        end_index = kwargs["end_index"]
        if end_index < 0:
            return
        self.internal_sort(end_index=end_index - 1)
        self.find_min_and_concat(end_index)

    def find_min_and_concat(self, start):
        # start is the start of the unsorted part
        smallest_index = start
        for i in range(start+1, len(self.current_data_to_be_sorted)):
            if self.current_data_to_be_sorted[i] < self.current_data_to_be_sorted[smallest_index]:
                smallest_index = i

        self.current_data_to_be_sorted[start], self.current_data_to_be_sorted[smallest_index] =\
            self.current_data_to_be_sorted[smallest_index], self.current_data_to_be_sorted[start]
    # U(A[a,...b,...c]) =  U(a,...b-1,...c) | find_min(A[b,...c]) = T(n-1) + dn
