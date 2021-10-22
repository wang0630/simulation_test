from random import uniform
from os import path
import csv
import sortings as s
import plot as pt
import memory_monitor as mm


def generate_uniform_distribution():
    for i in range(20001):
        base_path = path.dirname(__file__)
        file_path = (path.abspath(path.join(base_path, "uniform_distribution.txt")))
        with open(file_path, "a") as f:
            f.write(f"{uniform(-20, 100): .2f}\n")


def parseCsvToTxt(file_name, column_to_be_chosen):
    base_path = path.dirname(__file__)
    file_path = (path.abspath(path.join(base_path, f"{file_name}.csv")))
    write_file_path = (path.abspath(path.join(base_path, f"{file_name}.txt")))
    with open(file_path, newline='') as csv_file:
        with open(write_file_path, "a") as write_file:
            reader = csv.reader(csv_file)
            for line_no, row in enumerate(reader):
                if line_no == 0:
                    continue
                write_file.write(f"{row[column_to_be_chosen]}\n")


if __name__ == '__main__':
    sorting_list = [
        # s.BubbleSort(),
        s.SelectionSort(),
        # s.InsertionSort(),
        # s.QuickSort(),
        s.MergeSort(),
    ]
    fmt_list = ["o-g", "o-b", "o-m", "o-y", "o-r"]
    file_list = ["u", "n", "v", "s"]
    plt = pt.Plot()
    for index, file in enumerate(file_list):
        time_results = []
        # Time to data size
        # for s in sorting_list:
        #     time_result = s.time_to_size_sort(file)
        #     time_results.append({
        #         "time_result": time_result,
        #         "sorting_name": s.__class__.__name__
        #     })
        # plt.make_subplot(file, index, range(5, 101, 5), time_results, fmt_list)
        # plt.figures[file].show()

        memory_results = []
        # Memory usage to data size
        for s in sorting_list:
            memory_result = s.memory_to_size_sort(file)
            memory_results.append({
                "time_result": memory_result,
                "sorting_name": s.__class__.__name__
            })

