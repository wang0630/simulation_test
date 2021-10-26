import datetime
import math
from .sorting import Sorting


class InversionCountMergeSort(Sorting):
    def __init__(self):
        super().__init__()
        self.total_inversions_in_original_dataset = {
            "u": 3433672,
            "n": 74709253,
            "v": 74709253,
            "s": 871308557,
        }
        self.current_inversion_count = 0
        self.current_inversion_degree = None

    def time_to_sortness_sort(self, file_type_key):
        time_result = []
        self.read_data_to_ram(file_type_key)
        # Reversely sort list and make the degree 100
        self.data = sorted(self.data, reverse=True)
        self.current_inversion_degree = 100
        reversely_sorted_inversion_count = sum(range(len(self.data)))
        self.current_inversion_count = reversely_sorted_inversion_count
        # Get the data size from 5, 10,..., 100
        for degree in range(100, -1, -10):
            # List to store the running time of all 5 iterations for a given data size percentage
            self.create_inversion_list(degree, reversely_sorted_inversion_count)
            times = []
            for iteration in range(self.iteration_count):
                # Get a copy of data to manipulate
                # cur_degree_inversion_list contains the whole list which is in current degree
                cur_degree_inversion_list = self.data[:]
                start_time = datetime.datetime.now()
                # Partition cur_degree_inversion_list to several list to avoid max recursive
                self.partition_sort(cur_degree_inversion_list)
                time_delta = datetime.datetime.now() - start_time
                times.append(time_delta.total_seconds())
            # Compute the average time of all 5 iterations of a given data size percentage
            time_result.append(round(sum(times) / self.iteration_count, 4))
            print(f"{self.__class__.__name__} in {file_type_key} with {degree}%, time result: {time_result}")
        return time_result

    def partition_sort(self, cur_degree_inversion_list):
        self.reset()
        intervals = list(range(0, len(cur_degree_inversion_list), self.data_size_limit))
        if intervals[-1] < len(cur_degree_inversion_list):
            intervals.append(len(cur_degree_inversion_list))

        for index in range(1, len(intervals)):
            prev = intervals[index-1]
            cur = intervals[index]
            # Partition to avoid max recursive calls
            self.current_data_to_be_sorted = cur_degree_inversion_list[prev:cur]
            # Do sorting
            self.internal_sort_wrapper()

        # k-way merge self.dataset_result
        self.k_way_merge()

    def create_inversion_list(self, degree, reversely_sorted_inversion_count):
        self.reset()
        self.current_inversion_degree = degree
        # If list is reversely sorted, then the total inversion count is (n-1) + (n-2) +... + 1
        lower_bound = math.floor(reversely_sorted_inversion_count * (degree / 100))
        # Use modified version of merge sort to sort the data and record the inversion count
        self.inversion_merge_sort(start_index=0, end_index=len(self.data) - 1, lower_bound=lower_bound)

    def inversion_merge_sort(self, **kwargs):
        if "start_index" not in kwargs:
            raise KeyError("start_index is missing in Inversion_count_merge_sort.merge_sort")
        if "end_index" not in kwargs:
            raise KeyError("end_index is missing in Inversion_count_merge_sort.merge_sort")

        start_index = kwargs["start_index"]
        end_index = kwargs["end_index"]
        lower_bound = kwargs["lower_bound"]
        if self.current_inversion_count <= lower_bound:
            return
        if start_index >= end_index:
            return
        mid = int((start_index + end_index) / 2)
        self.inversion_merge_sort(start_index=start_index, end_index=mid, lower_bound=lower_bound)
        self.inversion_merge_sort(start_index=mid + 1, end_index=end_index, lower_bound=lower_bound)
        self.inversion_merge(start_index, mid, mid + 1, end_index, lower_bound)

    def inversion_merge(self, start1, end1, start2, end2, lower_bound):
        if self.current_inversion_count <= lower_bound:
            return

        result = []
        i = start1
        j = start2
        while i <= end1 and j <= end2:
            if self.data[i] > self.data[j]:
                result.append(self.data[j])
                j += 1
                # Count inversion
                self.current_inversion_count -= (end1 - i + 1)
                if self.current_inversion_count <= lower_bound:
                    break
            else:
                result.append(self.data[i])
                i += 1

        if i <= end1:
            for k in range(i, end1 + 1):
                result.append(self.data[k])
        if j <= end2:
            for k in range(j, end2 + 1):
                result.append(self.data[k])

        for k in range(start1, end2 + 1):
            self.data[k] = result[k - start1]

    def internal_sort(self, **kwargs):
        pass
