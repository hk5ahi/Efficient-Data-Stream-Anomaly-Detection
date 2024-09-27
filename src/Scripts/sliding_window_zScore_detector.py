import numpy as np

class SlidingWindowZScoreDetector:
    def __init__(self, window_size, threshold, drift_sensitivity):
        """
        Initialize the sliding window Z-score anomaly detector.

        Parameters:
        - window_size (int): Number of data points to include in the sliding window.
        - threshold (float): Z-score threshold for anomaly detection.
        - drift_sensitivity (float): Sensitivity to concept drift for adjusting the mean.

        Raises:
        ValueError: If any of the input parameters are invalid.
        """
        # Validate input parameters
        if not isinstance(window_size, int) or window_size <= 0:
            raise ValueError("Window size must be a positive integer")
        if not isinstance(threshold, (int, float)):
            raise ValueError("Threshold must be a number")
        if not isinstance(drift_sensitivity, (int, float)):
            raise ValueError("Drift sensitivity must be a number.")

        # Initialize instance variables
        self.window_size = window_size
        self.threshold = threshold
        self.drift_sensitivity = drift_sensitivity
        self.window = []
        # Initialize mean and standard deviation to None which is used to indicate that the mean and standard deviation are not calculated yet
        self.mean = None
        self.std_dev = None

    def update_window(self, new_value):
        """
        Update the sliding window with a new data point.

        Parameters:
        - new_value (float): The new data point to be added to the window.

        Raises:
        ValueError: If the new_value is not a number.
        """
        if not isinstance(new_value, (int, float)):
            raise ValueError("New value must be a number")

        # Add the new value to the window
        if len(self.window) < self.window_size:
            self.window.append(new_value)
        else:
            # Remove the oldest value and add the new one
            self.window.pop(0)
            self.window.append(new_value)

    def calculate_statistics(self):
        """
        Calculate the mean and standard deviation of the current window.
        """
        # Check if the window is empty
        if len(self.window) == 0:
            raise ValueError("Window is empty. Cannot calculate statistics")

        # Calculate mean and standard deviation of the current window
        self.mean = np.mean(self.window)
        self.std_dev = np.std(self.window)

    def detect_anomaly(self, new_value):
        """
        Detect anomalies in the data stream using the sliding window Z-score method.

        Parameters:
        - new_value (float): The new data point to be checked for anomalies.

        Returns:
        - bool: True if the new value is an anomaly, False otherwise.

        Raises:
        ValueError: If the new_value is not a number.
        """
        # Validate input parameter
        if not isinstance(new_value, (int, float)):
            raise ValueError("New value must be a number")

        # Update window with the new value first
        self.update_window(new_value)

        if len(self.window) < self.window_size:
            # Not enough data to calculate statistics
            return False

        # Calculate mean and standard deviation of the current window
        self.calculate_statistics()

        # Adjust mean for concept drift
        drift_adjusted_mean = self.mean + self.drift_sensitivity * len(self.window)

        # Calculate Z-score
        if self.std_dev > 0:
            z_score = (new_value - drift_adjusted_mean) / self.std_dev
        else:
            z_score = 0

        # Return True if the Z-score exceeds the threshold (anomaly)
        return abs(z_score) > self.threshold
