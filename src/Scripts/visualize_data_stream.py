import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')  # Use the Tkinter backend for interactive plotting
import numpy as np
from src.Scripts.generate_continuous_data_stream import generate_continuous_data_stream
from src.Scripts.sliding_window_zScore_detector import SlidingWindowZScoreDetector


def visualize_data_stream(amplitude, frequency, seasonality, noise_level, interval, max_points, window_size, threshold, drift_sensitivity):
    """
    Visualizes a continuous data stream with anomalies in real-time using Matplotlib.

    Parameters:
        amplitude (float): Amplitude of the regular pattern in the data stream.
        frequency (float): Frequency of the regular pattern in the data stream.
        seasonality (int): Seasonality of the regular pattern in the data stream.
        noise_level (float): Noise level in the data stream.
        interval (int): Time interval between data points in seconds.
        max_points (int): Maximum number of data points to visualize.
        threshold (float): Z-score threshold for anomaly detection.
        window_size (int): Number of data points to include in the sliding window.
        drift_sensitivity (float): Sensitivity to concept drift for adjusting the mean.

    Raises:
        ValueError: If any of the input parameters are invalid.
    """
    # Validate the input parameters
    if not isinstance(max_points, int) or max_points <= 0:
        raise ValueError("Maximum points must be a positive integer")

    # Initialize the data points and anomaly flags
    data_points = np.zeros(max_points)  # Preallocate space for max_points
    anomaly_flags = np.zeros(max_points, dtype=bool)  # Boolean array to mark anomalies
    # A circular buffer is used to efficiently manage a fixed-size buffer for storing data points.
    index = 0  # Index for circular buffer which stores the data points

    # Create the generator for continuous data stream
    generator = generate_continuous_data_stream(amplitude, frequency, seasonality, noise_level, interval)

    # Create the anomaly detector
    detector = SlidingWindowZScoreDetector(window_size, threshold, drift_sensitivity)

    # Create the plot
    plt.ion()  # Enable interactive mode for real-time plotting
    fig, ax = plt.subplots(figsize=(10, 6))
    # Adjust subplot position
    plt.subplots_adjust(right=0.71)  # Adjust left margin
    # Set the window title for the plot
    fig.canvas.manager.set_window_title('Real-Time Data Stream with Anomalies')
    line, = ax.plot(range(max_points), data_points, 'b-', label='Data Stream')  # Initialize data plot
    # Calculate 20% of the amplitude
    offset = amplitude * 0.2
    ax.set_ylim(-amplitude * 2 - offset, amplitude * 2 + offset)  # Set initial y-axis limits with 20% offset
    ax.set_xlim(0, max_points)  # Initial x-axis limits
    ax.set_xlabel('Time (s)') # Set x-axis label
    ax.set_ylabel('Data Value') # Set y-axis label
    ax.set_title('Real-Time Data Stream with Anomalies') # Set plot title
    # Display parameter values on the plot
    param_text = (
        f"Window Size: {window_size}\n"
        f"Noise Level: {noise_level}\n"
        f"Amplitude: {amplitude}\n"
        f"Interval : {interval}\n"
        f"Threshold : {threshold}"
    )
    # Place the text outside the graph (adjust x and y coordinates as needed)
    text_box = ax.text(1.1, 1, param_text, transform=ax.transAxes, fontsize=10,
                       bbox=dict(boxstyle='round', facecolor='white', alpha=0.8),
                       verticalalignment='top', ha='left')
    # Update the parameter text position dynamically
    text_box.set_text(param_text)  # Update the displayed text with the current values
    # Initialize the anomaly plot and red dot is used for anomalies
    anomaly_line, = ax.plot(range(max_points), np.full(max_points, np.nan), 'ro',
                            label='Anomalies', zorder=2)
    # Create a box to display the last detected anomaly
    last_anomaly_box = ax.text(1.03, 0.5, 'Last Anomaly Detected: None', transform=ax.transAxes, fontsize=10,
                               bbox=dict(boxstyle='square,pad=0.3', facecolor='white', edgecolor='black', alpha=0.8),
                               verticalalignment='center', ha='left')
    ax.legend()
    max_y_value = amplitude  # Initialize the max y-value for setting limits
    last_anomaly_value = None  # Variable to store the last anomaly value

    while True:
        try:
            # Get the next data point from the generator
            data_point = next(generator)
            # Detect if the new data point is an anomaly
            is_anomaly = detector.detect_anomaly(data_point)

            # Store the new data point in array
            data_points[index] = data_point
            anomaly_flags[index] = is_anomaly  # Mark whether the point is an anomaly

            # Update the index for the circular buffer
            index = (index + 1) % max_points # Wrap around to the start if end is reached

            # Prepare data for plotting
            plot_data = np.roll(data_points, -index)  # Shift the array for correct plotting
            anomaly_data = np.where(np.roll(anomaly_flags, -index), plot_data, np.nan)  # Mark anomalies for plotting

            # Update the line and anomaly plot in the plot
            line.set_ydata(plot_data)  # Update Y values for regular data points
            anomaly_line.set_ydata(anomaly_data)  # Update Y values for anomalies

            # Update the max y value if necessary
            current_max = np.max(np.abs(plot_data))
            max_y_value = max(max_y_value, current_max)  # Update max y value
            ax.set_ylim(-max_y_value - offset, max_y_value + offset)  # Set new y-limits with offset
            # If an anomaly is detected, update the anomaly box
            if is_anomaly:
                last_anomaly_value = data_point
                last_anomaly_index = index
                # Update the last anomaly text dynamically with the value and index
                last_anomaly_box.set_text(
                    f'Last Anomaly Detected: ({last_anomaly_index}, {last_anomaly_value:.2f})')
            elif last_anomaly_value is None:
                # If no anomalies have been detected, display 'None'
                last_anomaly_box.set_text('Last Anomaly Detected: None')

            # Redraw the plot
            fig.canvas.draw()
            plt.pause(interval / 2)  # Pause for half the interval to allow for smooth visualization

        except Exception as exception:
            print(f"Error during visualization: {exception}")
            break  # Exit the loop on error

        except KeyboardInterrupt:
            print("Plotting stopped by the user.")
            break # Exit the loop on user interrupt


