import sea_level_predictor
from unittest import main

def run_plot():
    """Function to run the plot."""
    sea_level_predictor.draw_plot()

if __name__ == "__main__":
    run_plot()
    # Run unit tests automatically (optional, could also be in a separate test script)
    main(module='test_module', exit=False)