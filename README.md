
# Efficient Data Stream Anomaly Detection  

## Overview  
This project implements a Python-based solution for detecting anomalies in a continuous data stream. It simulates real-time data, applies a sliding window approach for processing batches, and uses the Isolation Forest algorithm to identify anomalies. The anomalies are highlighted visually in the output and summarized in a final static plot.  

---

## Features  
1. **Data Stream Simulation**  
   - Generates data with **seasonal patterns**, **concept drift**, **random noise**, and **anomalies** to emulate real-world streams.  
   - Customizable parameters like drift rate and anomaly probability for flexible simulations.  

2. **Real-Time Anomaly Detection**  
   - Sliding window mechanism to analyze data continuously in overlapping batches.  
   - Anomalies are detected using the **Isolation Forest** algorithm, a tree-based method designed for unsupervised anomaly detection.  

3. **Visualization**  
   - Real-time console output highlights anomalies in **red** while showing normal data points.  
   - A static **scatter plot** summarizes the stream, with anomalies clearly marked.  

---

## Why Isolation Forest?  
The **Isolation Forest** algorithm isolates anomalies instead of profiling normal behavior. It works by:  
- Building random decision trees to split data points.  
- Identifying points that are easily isolated (few splits required) as anomalies.  

### Advantages:  
- **Scalable**: Handles large datasets efficiently.  
- **Robust**: Adapts well to streaming data with dynamic distributions.  
- **Unsupervised**: No labeled data required for training.  

This makes it suitable for handling **concept drift** (gradual change in data distribution) and **seasonal patterns** inherent in the simulated stream.  

---

## Sliding Window Approach  
To mimic real-time processing, the data stream is processed in overlapping windows:  
- **Batch Size**: 100 points are analyzed in each batch.  
- **Slide Size**: 40 points are retained between batches to ensure continuity.  

### Why this approach?  
- Ensures recent context is preserved while keeping computational load manageable.  
- Allows anomalies to be detected specifically in newer data points, avoiding redundancy.  

---

## Visualization  
The project includes two visualization mechanisms:  
1. **Real-Time Console Output**  
   - Each streamed value is printed with anomalies marked in **red** for immediate feedback.  
2. **Static Plot**  
   - Plots the entire stream after processing:
     - Normal points in **blue**.  
     - Anomalies in **red**.  

---

## Usage Instructions  

### Prerequisites  
- Python 3.x  
- Required Libraries:  
  ```bash  
  pip install numpy matplotlib scikit-learn termcolor  
  ```  

### Running the Script  
1. Clone the repository.  
   ```bash  
   git clone https://github.com/<your-repo-name>/data-stream-anomaly-detection.git  
   cd data-stream-anomaly-detection  
   ```  
2. Run the script.  
   ```bash  
   python anomaly_detection.py  
   ```  

### Customizing Parameters  
- **Data Stream**: Modify the `generate_data_stream` function to adjust:  
  - `length`: Total number of data points.  
  - `drift_rate`: Rate of concept drift.  
  - `anomaly_probability`: Frequency of anomalies.  

- **Anomaly Detection**: Adjust `batch_size` and `slide_size` in the `sliding_window_anomaly_detection_with_visualization` function.  

---

## File Structure  
- `anomaly_detection.py`: Main Python script.  
- `requirements.txt`: List of required Python libraries.  

---

## Example Output  

### Console Output  
- **Normal Data**: Displayed normally.  
- **Anomalies**: Highlighted in **red** for quick identification.  

### Final Plot  
- **Blue Points**: Normal data.  
- **Red Points**: Detected anomalies.  

---

## Conclusion  
This project demonstrates an efficient approach to anomaly detection in data streams. The combination of Isolation Forest, sliding windows, and real-time visualization ensures both accuracy and clarity. This framework can be extended to various real-world scenarios such as system monitoring, financial transactions, or IoT data streams.  

---  
For any queries, feel free to reach out at **ayush.jaiswal.cse20@itbhu.ac.in**.
