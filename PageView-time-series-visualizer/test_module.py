import unittest
import time_series_visualizer
import matplotlib as mpl

class DataCleaningTestCase(unittest.TestCase):
    def test_data_cleaning(self):
        actual = int(time_series_visualizer.df.count())
        expected = 1238
        self.assertEqual(actual, expected, "Expected DataFrame count after cleaning to be 1238.")

class LinePlotTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = time_series_visualizer.draw_line_plot()
        self.ax = self.fig.axes[0]

    def test_line_plot_title(self):
        actual = self.ax.get_title()
        expected = "Daily freeCodeCamp Forum Page Views 5/2016-12/2019"
        self.assertEqual(actual, expected)

    def test_line_plot_labels(self):
        self.assertEqual(self.ax.get_xlabel(), "Date")
        self.assertEqual(self.ax.get_ylabel(), "Page Views")

    def test_line_plot_data_quantity(self):
        actual = len(self.ax.lines[0].get_ydata())
        expected = 1238
        self.assertEqual(actual, expected)

class BarPlotTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = time_series_visualizer.draw_bar_plot()
        self.ax = self.fig.axes[0]

    def test_bar_plot_legend_labels(self):
        actual = [label.get_text() for label in self.ax.get_legend().get_texts()]
        expected = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        self.assertEqual(actual, expected)

    def test_bar_plot_labels(self):
        self.assertEqual(self.ax.get_xlabel(), "Years")
        self.assertEqual(self.ax.get_ylabel(), "Average Page Views")
        actual = [label.get_text() for label in self.ax.get_xaxis().get_majorticklabels()]
        expected = ['2016', '2017', '2018', '2019']
        self.assertEqual(actual, expected)

    def test_bar_plot_number_of_bars(self):
        actual = len([rect for rect in self.ax.patches if isinstance(rect, mpl.patches.Rectangle)])
        expected = 48  # 4 years * 12 months
        self.assertEqual(actual, expected)

class BoxPlotTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = time_series_visualizer.draw_box_plot()
        self.ax1 = self.fig.axes[0]
        self.ax2 = self.fig.axes[1]

    def test_box_plot_titles(self):
        self.assertEqual(self.ax1.get_title(), "Year-wise Box Plot (Trend)")
        self.assertEqual(self.ax2.get_title(), "Month-wise Box Plot (Seasonality)")

    def test_box_plot_labels(self):
        self.assertEqual(self.ax1.get_xlabel(), "Year")
        self.assertEqual(self.ax1.get_ylabel(), "Page Views")
        self.assertEqual(self.ax2.get_xlabel(), "Month")
        self.assertEqual(self.ax2.get_ylabel(), "Page Views")

    def test_box_plot_number_of_boxes(self):
        # Check number of boxes in Year-wise plot (should be 4 years)
        actual = len(self.ax1.patches) // 6  # Each box consists of 6 elements
        expected = 4
        self.assertEqual(actual, expected, "Expected four boxes in box plot 1")

        # Check number of boxes in Month-wise plot (should be 12 months)
        actual = len(self.ax2.patches) // 6  # Each box consists of 6 elements
        expected = 12
        self.assertEqual(actual, expected, "Expected 12 boxes in box plot 2")


if __name__ == "__main__":
    unittest.main()
