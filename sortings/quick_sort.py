from .inversion_count_merge_sort import InversionCountMergeSort


def partition(target):
    start = 0
    end = len(target) - 1
    mid = int((start + end) / 2)
    larger = []
    smaller = []
    equal_to_pivot = []
    for i in range(start, end+1):
        if target[i] > target[mid]:
            larger.append(target[i])
        elif target[i] < target[mid]:
            smaller.append(target[i])
        else:
            equal_to_pivot.append(target[i])
    return smaller, equal_to_pivot, larger


class QuickSort(InversionCountMergeSort):
    def __init__(self):
        super().__init__()

    def internal_sort(self, **kwargs):
        if "sublist" not in kwargs:
            raise KeyError("sublist property is missing in QuickSort.internalSort")

        sublist = kwargs["sublist"]
        if len(sublist) <= 1:
            return sublist
        smaller, equal_to_pivot, larger = partition(sublist)
        smaller = self.internal_sort(sublist=smaller)
        larger = self.internal_sort(sublist=larger)
        return smaller + equal_to_pivot + larger
