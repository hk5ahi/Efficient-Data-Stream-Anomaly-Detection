import argparse

from src.Constants.constants import AMPLITUDE, FREQUENCY, SEASONALITY, NOISE_LEVEL, INTERVAL, MAX_POINTS, WINDOW_SIZE, \
    THRESHOLD, DRIFT_SENSITIVITY
from src.Scripts.visualize_data_stream import visualize_data_stream

def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description="Visualize a data stream with anomalies.")

    # Add the script arguments with default values
    parser.add_argument("--amplitude", type=float, default=AMPLITUDE, help="Amplitude of the signal (default: 10.0)")
    parser.add_argument("--frequency", type=float, default=FREQUENCY, help="Frequency of the signal (default: 0.1)")
    parser.add_argument("--seasonality", type=int, default=SEASONALITY, help="Seasonality of the signal (default: 24)")
    parser.add_argument("--noise_level", type=float, default=NOISE_LEVEL, help="Noise level of the signal (default: 2.0)")
    parser.add_argument("--interval", type=int, default=INTERVAL, help="Interval between data points in seconds (default: 1)")
    parser.add_argument("--max_points", type=int, default=MAX_POINTS, help="Maximum number of points to visualize (default: 100)")
    parser.add_argument("--window_size", type=int, default=WINDOW_SIZE, help="Window size for anomaly detection (default: 25)")
    parser.add_argument("--threshold", type=float, default=THRESHOLD, help="Threshold for anomaly detection (default: 2.5)")
    parser.add_argument("--drift_sensitivity", type=float, default=DRIFT_SENSITIVITY, help="Drift sensitivity for anomaly detection (default: 0.01)")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Visualize the data stream with anomalies
    visualize_data_stream(
        amplitude=args.amplitude,
        frequency=args.frequency,
        seasonality=args.seasonality,
        noise_level=args.noise_level,
        interval=args.interval,
        max_points=args.max_points,
        window_size=args.window_size,
        threshold=args.threshold,
        drift_sensitivity=args.drift_sensitivity
    )

if __name__ == "__main__":
    main()
