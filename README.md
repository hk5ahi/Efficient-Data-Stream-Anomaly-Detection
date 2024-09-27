from src.Constants.constants import NOISE_LEVELfrom src.Constants.constants import AMPLITUDE

# Efficient Data Stream Anomaly Detection

As part of the project, a continuous stream of floating-point values will be generated to mimic real-time measurements. An anomaly detection algorithm will be implemented to find anomalies in the data, and real-time results will be visualized that provide user interaction and robust error handling.

## Requirements

Make sure you have the following Python packages installed:

- `matplotlib`
- `numpy`

You can install the required packages using `pip`:

```sh
pip install -r requirements.txt
```
---
### Sliding Window Z-Score Method: Algorithm Overview

Using the most recent data points in a continuous stream, the Sliding Window Z-Score Method is an anomaly detection technique that looks for odd patterns. This method successfully emphasizes deviations from typical behavior in real-time by computing the Z-score based on the mean and standard deviation of a fixed-size window of data. The algorithm then compares the Z-score of the latest data point to a predefined threshold to determine if it is an anomaly. If the Z-score exceeds the threshold, the data point is flagged as an anomaly, indicating a significant deviation from the norm.

### Optimization of Speed and Efficiency

By concentrating on a small subset of data points inside a sliding window, this approach excels in speed and efficiency and enables fast updates to the mean and standard deviation. It greatly reduces computing overhead by only making adjustments to these statistics when new data becomes available, as opposed to recalculating them for the whole dataset. Because of its incremental approach, the algorithm can quickly adjust to shifting patterns in data without requiring a lot of computation, which makes it perfect for real-time applications where anomaly detection in real time is critical.

Furthermore, compared to more complex algorithms like Isolation Forest or deep learning-based techniques, the Sliding Window Z-Score Method is simpler and more effective. These substitutes typically demand comprehensive training on huge datasets, resulting in increased computing expenses and extended processing durations. On the other hand, the Z-Score approach requires fewer external libraries for implementation, which allows its seamless integration into current systems. Because of its capacity to detect idea drift, quickly execute, and need minimal resources, the Sliding Window Z-Score Method is a better option when it comes to identifying anomalies in continuous data streams.

---

## Parameter Selection for Sliding Window Z-Score Method
The data stream's parameters, which can represent a variety of metrics, such as financial transactions or system performance indicators, or real-time sequences of floating-point values, are as follows:

### 1. **Window Size**
- Recommended Value: **100 to 200 data points**
- Rationale: This range captures seasonal variations effectively while smoothing the effects of random noise in real-time sequences.

### 2. **Threshold**
- Recommended Value: **2.5 to 3**
- Rationale: A threshold of **3** minimizes false positives for stable patterns, while **2.5** may be used for slightly more sensitivity to detect anomalies in volatile metrics.

### 3. **Drift Sensitivity**
- Recommended Value: **0.01**
- Rationale: This sensitivity is appropriate for adapting to gradual changes in the data stream while allowing the algorithm to adjust to concept drift effectively.

---
## How to Run the Data Stream Anomaly Detection
You can run the data stream anomaly detection algorithm by first installing the requirements as mentioned above and then executing the following command in your project's terminal:
```sh
python main.py
```
---
## Change Parameters for Data Stream Anomaly Detection
You can modify the parameters of the data stream anomaly detection algorithm or the continuous data stream generation by providing values through the command line. If no values are provided, the default parameters will be used. Here’s an example of how to pass the parameters via the command line:

```sh
python main.py --amplitude 15 --window_size 5 --noise_level 3.0
```
OR

You can modify the parameters of the data stream anomaly detection algorithm or continuous data stream generation by changing the values in the `src/Constants/constants.py` file. Here is an example of how you can adjust the parameters:

```python
# Parameters for Data Stream Anomaly Detection Algorithm
WINDOW_SIZE = 150
# Parameters for Continuous Data Stream Generation
NOISE_LEVEL = 5
```