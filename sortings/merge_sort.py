from .sorting import Sorting


class MergeSort(Sorting):
    def __init__(self):
        super().__init__()

    def internal_sort(self, **kwargs):
        if "start_index" not in kwargs:
            raise KeyError("start_index is missing in MergeSort.internal_sort")
        if "end_index" not in kwargs:
            raise KeyError("end_index is missing in MergeSort.internal_sort")

        start_index = kwargs["start_index"]
        end_index = kwargs["end_index"]

        if start_index >= end_index:
            return
        mid = int((start_index + end_index) / 2)
        self.internal_sort(start_index=start_index, end_index=mid)
        self.internal_sort(start_index=mid+1, end_index=end_index)
        self.merge(start_index, mid, mid+1, end_index)

    def merge(self, start1, end1, start2, end2):
        result = []
        i = start1
        j = start2
        while i <= end1 and j <= end2:
            if self.current_data_to_be_sorted[i] >= self.current_data_to_be_sorted[j]:
                result.append(self.current_data_to_be_sorted[j])
                j += 1
            else:
                result.append(self.current_data_to_be_sorted[i])
                i += 1

        if i <= end1:
            for k in range(i, end1+1):
                result.append(self.current_data_to_be_sorted[k])
        if j <= end2:
            for k in range(j, end2+1):
                result.append(self.current_data_to_be_sorted[k])

        for k in range(start1, end2+1):
            self.current_data_to_be_sorted[k] = result[k-start1]
