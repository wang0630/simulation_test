import datetime
from random import uniform
from os import path
from pympler import asizeof
import csv
import sortings as s
import plot as pt


def generate_uniform_distribution():
    for i in range(20001):
        base_path = path.dirname(__file__)
        file_path = (path.abspath(path.join(base_path, "data/uniform_distribution.txt")))
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
    pictures_path = (path.abspath(path.join(path.dirname(__file__), "pictures")))
    sorting_list = [
        s.BubbleSort,
        s.SelectionSort,
        s.InsertionSort,
        s.QuickSort,
        s.MergeSort,
    ]
    fmt_list = ["o-g", "o-b", "o-m", "o-y", "o-r"]
    file_list = ["u", "n", "v", "s"]
    plt = pt.Plot()
    # Time to data size
    figure_type = "t_to_ds"
    for index, file_name in enumerate(file_list):
        time_results = []
        for s in sorting_list:
            time_result = s.time_to_size_sort(file_name)
            time_results.append({
                "result": time_result,
                "sorting_name": s.__class__.__name__
            })
        plt.make_subplot(figure_type, file_name, range(5, 101, 5), time_results, fmt_list)
        plt.save_figure(figure_type, f"{pictures_path}/t-to-ds-{datetime.datetime.today().strftime('%m-%d-%H-%M')}.png", bbox_inches='tight')

    # Memory to data size
    figure_type = "m_to_ds"
    for index, file_name in enumerate(file_list):
        memory_results = []
        for s in sorting_list:
            sort_instance = s()
            memory_result = sort_instance.memory_to_size_sort(file_name)
            # Remove memory used by plt object
            for i, m in enumerate(memory_result):
                memory_result[i] -= (asizeof.asizeof(plt) / 10**6)
            memory_results.append({
                "result": memory_result,
                "sorting_name": sort_instance.__class__.__name__
            })
        plt.make_subplot(figure_type, file_name, range(5, 101, 5), memory_results, fmt_list)
        plt.save_figure(figure_type, f"{pictures_path}/memory-to-ds-{datetime.datetime.today().strftime('%m-%d-%H-%M')}.png", bbox_inches='tight')

    # Time to degree of sortness
    figure_type = "t_to_dos"
    for index, file_name in enumerate(file_list):
        time_results = []
        for s in sorting_list:
            time_result = s.time_to_sortness_sort(file_name)
            time_result.reverse()
            time_results.append({
                "result": time_result,
                "sorting_name": s.__class__.__name__
            })
        plt.make_subplot(figure_type, file_name, range(0, 101, 10), time_results, fmt_list)
        plt.save_figure(figure_type, f"{pictures_path}/{figure_type}-{datetime.datetime.today().strftime('%m-%d-%H-%M')}.png", bbox_inches='tight')

    # Memory to data size
    figure_type = "m_to_dos"
    for index, file_name in enumerate(file_list):
        memory_results = []
        for s in sorting_list:
            sort_instance = s()
            memory_result = sort_instance.memory_to_sortness_sort(file_name)
            # Remove memory used by plt object
            for i, m in enumerate(memory_result):
                memory_result[i] -= (asizeof.asizeof(plt) / 10**6)
            memory_results.append({
                "result": memory_result,
                "sorting_name": sort_instance.__class__.__name__
            })
        plt.make_subplot(figure_type, file_name, range(0, 101, 10), memory_results, fmt_list)
        plt.save_figure(figure_type, f"{pictures_path}/{figure_type}-{datetime.datetime.today().strftime('%m-%d-%H-%M')}.png", bbox_inches='tight')
