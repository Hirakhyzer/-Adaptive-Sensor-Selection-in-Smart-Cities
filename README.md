# -Adaptive-Sensor-Selection-in-Smart-Cities
Synthetic Sensor Dataset for Adaptive Sensor Selection in Smart Cities
This dataset supports research on adaptive sensor selection in smart city environments, specifically focusing on energy-efficient, real-time traffic monitoring and safety. It is used in the study "Adaptive AIoT Framework with Dynamic Sensor Group Selection for Real-Time Traffic Monitoring and Energy Efficiency."

  1. Table of Contents
  2. Overview
  3. Dataset Description
  4. File Structure
  5. Features
  6. Usage Instructions
  7. Analysis Workflow
  8. Citation
     
# Overview
Efficient management of urban traffic demands real-time adaptability and energy-efficient sensor operations. This dataset is synthetically generated to simulate a variety of urban traffic conditions such as weather variations, traffic density, and time of day. It facilitates experiments on dynamic sensor group selection, energy management, and latency optimization in smart city applications.

# Dataset Description
The dataset comprises 10,000 samples, evenly distributed across 10 distinct combinations of traffic and environmental conditions. Each sample describes a scenario that influences optimal sensor selection, energy consumption, and system responsiveness.

# Scenarios Covered:
1. Clear weather with low traffic
2. Foggy conditions with high traffic
3. Night-time with varying visibility
4. High-density traffic in rain
5. Sparse traffic with clear weather
6.Rush hour with medium visibility
7. Extreme weather with low visibility
8. Peak traffic during daylight
9. Off-peak hours with good weather
10. Holiday traffic with mixed weather conditions
# File Structure
synthetic_sensor_data.csv: The main dataset file.
adaptive_sensor_readme.md: This documentation file.
# Features
The dataset contains the following columns:

**Scenario_ID:** Unique identifier for the scenario.
**Time_of_Day:** Numerical representation (e.g., 1=Morning, 2=Afternoon, 3=Evening).
**Traffic_Density:** Numerical value representing vehicles per unit area.
**Weather_Condition:** Encoded value for weather (e.g., 1=Clear, 2=Rainy, 3=Foggy).
**Visibility:** Numerical score (1-10) for visibility levels.
**Optimal_Sensors:** Array indicating active sensors (e.g., [1, 0, 1, 0] for four sensors).
**Energy_Consumption:** Estimated energy usage for the optimal configuration.
**Response_Latency:** Expected latency (in milliseconds) for real-time response.
# Usage Instructions
## Prerequisites:
Python 3.7 or higher.
Install dependencies: pandas, numpy, scikit-learn, matplotlib.
## Load the Dataset:

import pandas as pd
data = pd.read_csv("synthetic_sensor_data.csv")
print(data.head())
Dataset Exploration: Use statistical and visualization tools to explore features such as traffic density distributions or sensor activation patterns.

Sensor Selection Training: Train a Decision Tree Classifier to predict optimal sensor groups:

## python

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

X = data[['Time_of_Day', 'Traffic_Density', 'Weather_Condition', 'Visibility']]
y = data['Optimal_Sensors']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = DecisionTreeClassifier(max_depth=5)
clf.fit(X_train, y_train)
print(f"Model accuracy: {clf.score(X_test, y_test)}")
Analysis Workflow

## Data Preprocessing:
Handle missing values and encode categorical data if applicable.

## Feature Engineering:
Create new metrics such as average traffic per hour or sensor prioritization scores.

## Performance Metrics:
Compare energy consumption and latency across configurations.

## Visualization:
Plot energy savings and sensor activation rates:
import matplotlib.pyplot as plt

plt.plot(data['Energy_Consumption'], label='Energy Consumption')
plt.legend()
plt.show()

## Citation
Coming Soon.

