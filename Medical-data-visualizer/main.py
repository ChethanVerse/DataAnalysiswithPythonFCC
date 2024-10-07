import medical_data_visualizer
from unittest import main

# Test your function by calling it here
if __name__ == "__main__":
    # Draw and save the categorical plot
    medical_data_visualizer.draw_cat_plot()

    # Draw and save the heatmap
    medical_data_visualizer.draw_heat_map()

    # Run unit tests automatically
    main(module='test_module', exit=False)
