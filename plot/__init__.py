from matplotlib import pyplot as pp


class Plot:
    def __init__(self):
        self.figures = {}
        self.ax_list_map = {}
        self.file_name_map = {
            "u": "Uniform Distribution",
            "n": "Normal Distribution",
            "r": "Ranking Of Video Games Wins",
            "v": "Price of Vehicles",
        }

    def make_subplot(self, file_type_key, subplot_index, x_axis, time_results, fmt):
        if file_type_key not in self.figures:
            fig, ((ax1, ax2), (ax3, ax4)) = pp.subplots(2, 2)
            self.figures[file_type_key] = fig
            self.ax_list_map[file_type_key] = [ax1, ax2, ax3, ax4]

        fig = self.figures[file_type_key]
        subplot = self.ax_list_map[file_type_key][subplot_index]
        fig.suptitle(self.file_name_map[file_type_key])

        for index, time_result in enumerate(time_results):
            subplot.plot(x_axis, time_result["time_result"], fmt[index], label=time_result["sorting_name"])
            subplot.legend()
