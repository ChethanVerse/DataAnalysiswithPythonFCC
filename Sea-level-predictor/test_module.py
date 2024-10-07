import unittest
import sea_level_predictor
import matplotlib as mpl


class LinePlotTestCase(unittest.TestCase):
    def setUp(self):
        """Set up the plot for testing."""
        self.ax = sea_level_predictor.draw_plot()

    def test_plot_title(self):
        """Test that the plot title is correctly set."""
        actual = self.ax.get_title()
        expected = "Rise in Sea Level"
        self.assertEqual(actual, expected, "Expected line plot title to be 'Rise in Sea Level'")

    def test_plot_labels(self):
        """Test that the x and y labels are correctly set."""
        actual_xlabel = self.ax.get_xlabel()
        expected_xlabel = "Year"
        self.assertEqual(actual_xlabel, expected_xlabel, "Expected line plot xlabel to be 'Year'")

        actual_ylabel = self.ax.get_ylabel()
        expected_ylabel = "Sea Level (inches)"
        self.assertEqual(actual_ylabel, expected_ylabel, "Expected line plot ylabel to be 'Sea Level (inches)'")

        actual_xticks = self.ax.get_xticks().tolist()
        expected_xticks = [1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0]
        self.assertEqual(actual_xticks, expected_xticks, "Expected x tick labels to be '1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0'")

    def test_plot_data_points(self):
        """Test that the data points in the plot are correct."""
        actual_data_points = self.ax.get_children()[0].get_offsets().data.tolist()
        expected_data_points = [
            [1880.0, 0.0], [1881.0, 0.220472441], [1882.0, -0.440944881], 
            # ... truncated for brevity ...
            [2012.0, 9.326771644], [2013.0, 8.980314951]
        ]
        self.assertEqual(actual_data_points, expected_data_points, "Expected different data points in scatter plot.")

    def test_plot_lines(self):
        """Test that the lines of best fit are correct."""
        actual_first_line = self.ax.get_lines()[0].get_ydata().tolist()
        expected_first_line = [
            # ... truncated for brevity ...
            10.049366089112283, 10.11241067312443
        ]
        self.assertEqual(actual_first_line, expected_first_line, "Expected different line for first line of best fit.")

        actual_second_line = self.ax.get_lines()[1].get_ydata().tolist()
        expected_second_line = [
            # ... truncated for brevity ...
            15.049588977701148, 15.216016251033011
        ]
        self.assertEqual(actual_second_line, expected_second_line, "Expected different line for second line of best fit.")

if __name__ == "__main__":
    unittest.main()
