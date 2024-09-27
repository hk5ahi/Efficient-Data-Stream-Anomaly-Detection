import random
import time
import numpy as np

def generate_continuous_data_stream(amplitude, frequency, seasonality, noise_level, interval):
    """
    Generate a continuous data stream with a regular pattern, seasonal pattern, and random noise.

    Parameters:
        amplitude (float): Amplitude of the regular pattern (in the same unit as the data).
        frequency (float): Frequency of the regular pattern (in Hz).
        seasonality (int): Period of the seasonal pattern (in seconds).
        noise_level (float): Maximum amplitude of the random noise (in the same unit as the data).
        interval (int): Time interval between data points (in seconds).

    Yields:
        float: The next data point in the continuous data stream.

    Raises:
        ValueError: If any of the input parameters are invalid.
    """

    # Validate the input parameters
    if not isinstance(amplitude, (int, float)) or amplitude <= 0:
        raise ValueError("Amplitude must be a positive number")
    if not isinstance(frequency, (int, float)) or frequency <= 0:
        raise ValueError("Frequency must be a positive number")
    if not isinstance(seasonality, int) or seasonality <= 0:
        raise ValueError("Seasonality must be a positive integer")
    if not isinstance(noise_level, (int, float)) or noise_level < 0:
        raise ValueError("Noise level must be a non-negative number")
    if not isinstance(interval, (int, float)) or interval <= 0:
        raise ValueError("Interval must be a positive number")

    while True:
        try:
            # Get the current time in seconds
            current_time = time.time()

            # Calculate the regular pattern using a sine function
            regular_pattern = amplitude * np.sin(2 * np.pi * frequency * current_time)

            # Calculate the seasonal pattern using a sine function
            seasonal_pattern = amplitude * np.sin(2 * np.pi * (current_time % seasonality) / seasonality)

            # Generate random noise within the specified range
            noise = random.uniform(-noise_level, noise_level)

            # Combine the regular pattern, seasonal pattern, and noise to get the data point
            data_point = regular_pattern + seasonal_pattern + noise

            # Yield the data point for visualization or further processing
            yield data_point

            # Sleep for half the interval to maintain the desired data rate
            time.sleep(interval / 2)

        except Exception as exception:
            print(f"Error generating data: {exception}")
            # If an error occurs
            raise exception
