from matplotlib import pyplot as pp, ticker


class Plot:
    def __init__(self):
        self.figures = {}
        self.figure_name_map = {
            "t_to_ds": "Time to data size",
            "m_to_ds": "Memory to data size",
        }
        self.xlabel_map = {
            "t_to_ds": "Data size",
            "m_to_ds": "Data size",
        }
        self.ylabel_map = {
            "t_to_ds": "Time",
            "m_to_ds": "Memory",
        }
        self.ylabel_unit = {
            "t_to_ds": ticker.FormatStrFormatter('%.3fs'),
            "m_to_ds": ticker.FormatStrFormatter('%.3fMB'),
        }
        self.xlabel_unit = {
            "t_to_ds": ticker.FormatStrFormatter('%d%%'),
            "m_to_ds": ticker.FormatStrFormatter('%d%%'),
        }
        self.subplot_name_map = {
            "u": "Uniform Distribution",
            "n": "Normal Distribution",
            "v": "Price of Vehicles",
            "s": "Sales record",
        }

    def make_subplot(self, figure_type, file_name, x_axis, results, fmt):
        if figure_type not in self.figures:
            fig, ((ax1, ax2), (ax3, ax4)) = pp.subplots(2, 2)
            fig.set_size_inches(18.5, 10.5)
            fig.suptitle(self.figure_name_map[figure_type])
            self.figures[figure_type] = {
                "figure": fig,
                "u": ax1,
                "n": ax2,
                "v": ax3,
                "s": ax4
            }

        subplot = self.figures[figure_type][file_name]
        for index, result in enumerate(results):
            subplot.plot(x_axis, result["result"], fmt[index], label=result["sorting_name"])
            subplot.title.set_text(self.subplot_name_map[file_name])
            subplot.set(xlabel=self.xlabel_map[figure_type], ylabel=self.ylabel_map[figure_type])
            subplot.xaxis.set_major_formatter(self.xlabel_unit[figure_type])
            subplot.yaxis.set_major_formatter(self.ylabel_unit[figure_type])
            subplot.legend()

    def get_figure(self, figure_type):
        return self.figures[figure_type]["figure"]
