import math
import datetime
import resource
from abc import ABC, abstractmethod
from concurrent.futures import ThreadPoolExecutor
from os import path
from min_heap import *
from memory_monitor import *


class Sorting(ABC):
    def __init__(self):
        self.data = []
        self.current_data_to_be_sorted = []
        self.dataset_result = []
        self.data_size_limit = 700
        self.iteration_count = 5

        self.file_types_map = {
            "u": (path.abspath(path.join(path.dirname(__file__), "..", "uniform_distribution.txt"))),
            "n": (path.abspath(path.join(path.dirname(__file__), "..", "normal_distribution.txt"))),
            "v": (path.abspath(path.join(path.dirname(__file__), "..", "vehicles.txt"))),
            "s": (path.abspath(path.join(path.dirname(__file__), "..", "sales.txt"))),
        }
        self.file_line_counts_map = {
            "u": 20000,
            "n": 20000,
            "v": 426800,
            "s": 5000000,
        }

    def read_data_to_ram(self, file_type_key):
        # Read data to RAM
        with open(self.file_types_map[file_type_key]) as f:
            for number in f:
                self.data.append(float(number))

    def memory_to_size_sort(self, file_type_key):
        memory_usage_result = []
        self.read_data_to_ram(file_type_key)
        for percentage in range(5, 101, 5):
            mems = []
            for iteration in range(self.iteration_count):
                with ThreadPoolExecutor() as executor:
                    memory_monitor = MemoryMonitor()
                    memory_monitor_thread = executor.submit(memory_monitor.memory_usage)
                    sort_thread = executor.submit(self.sort, percentage, file_type_key)
                    # Block the main thread execution
                    result = sort_thread.result()
                    memory_monitor.should_continue_measuring = False
                    mems.append(memory_monitor_thread.result())

            # Compute the average memory usage of all 5 iterations of a given data size percentage
            memory_usage_result.append(round((sum(mems) / self.iteration_count) / 10**6, 3))
            print(f"{self.__class__.__name__} {percentage}%, memory usage: {memory_usage_result} MB")
        return memory_usage_result

    def time_to_size_sort(self, file_type_key):
        time_result = []
        self.read_data_to_ram(file_type_key)
        # Get the data size from 5, 10,..., 100
        for percentage in range(5, 101, 5):
            # List to store the running time of all 5 iterations for a given data size percentage
            times = []
            for iteration in range(self.iteration_count):
                start_time = datetime.datetime.now()
                self.sort(percentage, file_type_key)
                time_delta = datetime.datetime.now() - start_time
                times.append(time_delta.total_seconds())
            # Compute the average time of all 5 iterations of a given data size percentage
            time_result.append(round(sum(times) / self.iteration_count, 4))
            print(f"{self.__class__.__name__} {percentage}%, time result: {time_result}")
        return time_result

    def sort(self, percentage, file_type_key):
        self.reset()
        line_count = self.file_line_counts_map[file_type_key]
        upper_bound = math.floor(line_count * (percentage / 100))
        for data_index, data in enumerate(self.data):
            if data_index == upper_bound:
                break
            self.current_data_to_be_sorted.append(data)
            # Not exceed the limit, proceed to keep pushing data to the array
            if len(self.current_data_to_be_sorted) < self.data_size_limit:
                continue
            # Do sorting
            self.internal_sort_wrapper()

        if self.current_data_to_be_sorted:
            self.internal_sort_wrapper()
        # k-way merge self.dataset_result
        self.k_way_merge()
        # return 0

    def internal_sort_wrapper(self):
        k = self.internal_sort(
            sublist=self.current_data_to_be_sorted,
            start_index=0,
            end_index=len(self.current_data_to_be_sorted) - 1,
        )
        if k:
            self.current_data_to_be_sorted = k
        self.dataset_result.append(self.current_data_to_be_sorted[:])
        self.current_data_to_be_sorted = []

    def k_way_merge(self):
        result = []
        if not self.dataset_result:
            return
        min_heap = MinHeap(len(self.dataset_result))
        for index, sorted_list in enumerate(self.dataset_result):
            if not sorted_list:
                continue
            min_heap.insert({
                "value": sorted_list.pop(0),
                "head_index": index,
            })
        while not min_heap.is_empty():
            # Find the smallest item
            smallest = min_heap.pop()
            head_index = smallest["head_index"]
            result.append(smallest["value"])
            if len(self.dataset_result[head_index]) == 0:
                continue
            min_heap.insert({
                "value": self.dataset_result[head_index].pop(0),
                "head_index": head_index,
            })

    def reset(self):
        self.current_data_to_be_sorted = []
        self.dataset_result = []

    @abstractmethod
    def internal_sort(self, **kwargs):
        pass
