import math
import random
import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from termcolor import colored  # For highlighting anomalies in terminal


def generate_data_stream(length=300, drift_start=0, drift_rate=0.04, anomaly_probability=0.05):
    """
    Generates a stream of data with seasonal patterns, concept drift, noise, and anomalies.

    Args:
    - length (int): Total number of data points to generate.
    - drift_start (int): Point in the stream where concept drift begins.
    - drift_rate (float): Rate at which the mean value drifts after drift_start.
    - anomaly_probability (float): Probability of an anomaly at any given point.

    Yields:
    - tuple: (timestamp, value) - A timestamp and the corresponding generated value.
    """
    t = 0  # Time counter
    baseline = 50  # Starting mean value
    amplitude = 10  # Amplitude of seasonal variation
    frequency = 0.1  # Frequency of seasonal pattern
    noise_level = 5  # Level of random noise

    while t < length:
        # Seasonal component
        seasonal = amplitude * math.sin(2 * math.pi * frequency * t)

        # Noise component
        noise = random.uniform(-noise_level, noise_level)

        # Drift component (starts after drift_start)
        drift = 0
        if t >= drift_start:
            drift = drift_rate * (t - drift_start)

        # Anomaly injection with a given probability
        if random.random() < anomaly_probability:
            anomaly = random.uniform(20, 50) * random.choice([-1, 1])
        else:
            anomaly = 0

        # Final value calculation
        value = baseline + seasonal + noise + drift + anomaly

        # Simulate a timestamp
        timestamp = time.time() + t

        yield (timestamp, value)

        t += 1
       


def sliding_window_anomaly_detection_with_final_plot(stream, batch_size=100, slide_size=40):
    """
    Processes a data stream, detects anomalies, and generates a final plot with anomalies highlighted.

    Args:
    - stream: A generator producing (timestamp, value) tuples.
    - batch_size (int): Number of data points in each window for anomaly detection.
    - slide_size (int): Number of data points to slide the window after each detection.

    Returns:
    - None: The function prints the data stream with anomalies highlighted and generates a final plot.
    """
    window = []  # Holds the current batch of data
    all_values = []  # All processed values for plotting
    all_anomalies = []  # Anomalies for plotting

    for data_point in stream:
        # Extract only the value from the generated data and add it to the window
        _, value = data_point
        window.append(value)

        # Wait until the window has enough data for processing
        if len(window) < batch_size:
            continue

        # Trim the window to ensure it contains only the latest batch_size points
        if len(window) > batch_size:
            window = window[-batch_size:]

        # Prepare data for Isolation Forest
        values = np.array(window).reshape(-1, 1)

        # Train Isolation Forest on the current window
        model = IsolationForest(contamination=0.1, random_state=42)
        model.fit(values)

        # Predict anomalies in the window (-1 indicates an anomaly, 1 indicates normal)
        predictions = model.predict(values)

        # Process the current batch
        for idx in range(batch_size - slide_size, batch_size):
            value = values[idx][0]
            all_values.append(value)  # Store all values for plotting
            if predictions[idx] == -1:  # If it's an anomaly
                all_anomalies.append((len(all_values) - 1, value))  # Store anomaly index and value
                print(colored(f"{value:.2f} (Anomaly)", "red"))
            else:
                print(f"{value:.2f}")

            # Add a small delay to simulate real-time streaming
            time.sleep(0.05)

        # Slide the window by removing the oldest data points
        window = window[slide_size:]

    # Plot the final results
    plt.figure(figsize=(10, 6))
    plt.title("Final Data Stream with Anomalies Highlighted")
    plt.xlabel("Data Point Index")
    plt.ylabel("Value")
    plt.plot(range(len(all_values)), all_values, 'bo', label='Normal Data')  # Plot normal data as blue dots
    if all_anomalies:  # If anomalies exist, plot them in red
        anomaly_indices, anomaly_values = zip(*all_anomalies)
        plt.plot(anomaly_indices, anomaly_values, 'ro', label='Anomalies')
    plt.legend()
    plt.show()


# Generate a real-time data stream with anomalies and concept drift
stream = generate_data_stream(length=300, drift_start=100, drift_rate=0.02, anomaly_probability=0.1)

# Run the sliding window anomaly detection with a final plot
sliding_window_anomaly_detection_with_final_plot(stream)
