"""Run a small synthetic adaptive sensor-selection baseline.

The script intentionally uses fictional data. It is a reproducible smoke test and
research scaffold, not a real smart-city deployment model.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


def make_synthetic_sensor_data(samples: int, seed: int) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    time_of_day = rng.integers(0, 4, samples)  # 0 night, 1 morning, 2 afternoon, 3 evening
    traffic_density = rng.uniform(5, 100, samples)
    weather = rng.integers(0, 4, samples)  # 0 clear, 1 rain, 2 fog, 3 storm
    visibility = np.clip(10 - weather * 2.1 - rng.normal(0, 1.2, samples), 1, 10)

    # Fictional sensors: camera, radar, lidar, loop detector, acoustic, weather station.
    camera = ((visibility >= 5) & (traffic_density > 25)).astype(int)
    radar = ((weather >= 1) | (traffic_density > 55)).astype(int)
    lidar = ((visibility < 5) | (traffic_density > 78)).astype(int)
    loop = (traffic_density > 18).astype(int)
    acoustic = ((time_of_day == 0) | (weather >= 2)).astype(int)
    weather_station = (weather >= 1).astype(int)

    active_count = camera + radar + lidar + loop + acoustic + weather_station
    energy = 12 + camera * 7 + radar * 9 + lidar * 15 + loop * 4 + acoustic * 5 + weather_station * 3
    latency = np.clip(38 + active_count * 8 + weather * 5 + traffic_density * 0.12, 35, 180)

    sensor_label = [f"{c}{r}{l}{lo}{a}{w}" for c, r, l, lo, a, w in zip(camera, radar, lidar, loop, acoustic, weather_station)]

    return pd.DataFrame(
        {
            "Scenario_ID": np.arange(samples),
            "Time_of_Day": time_of_day,
            "Traffic_Density": traffic_density.round(2),
            "Weather_Condition": weather,
            "Visibility": visibility.round(2),
            "Optimal_Sensors": sensor_label,
            "Energy_Consumption": energy.round(2),
            "Response_Latency": latency.round(2),
        }
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Synthetic adaptive sensor-selection baseline")
    parser.add_argument("--samples", type=int, default=1000)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--output-dir", default="outputs")
    args = parser.parse_args()

    data = make_synthetic_sensor_data(args.samples, args.seed)
    features = ["Time_of_Day", "Traffic_Density", "Weather_Condition", "Visibility"]
    x_train, x_test, y_train, y_test = train_test_split(
        data[features], data["Optimal_Sensors"], test_size=0.25, random_state=args.seed, stratify=data["Weather_Condition"]
    )

    model = DecisionTreeClassifier(max_depth=6, random_state=args.seed)
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    accuracy = accuracy_score(y_test, predictions)

    output_dir = Path(args.output_dir)
    results_dir = output_dir / "results"
    reports_dir = output_dir / "reports"
    results_dir.mkdir(parents=True, exist_ok=True)
    reports_dir.mkdir(parents=True, exist_ok=True)

    data.to_csv(results_dir / "synthetic_sensor_scenarios.csv", index=False)
    pd.DataFrame({"actual": y_test, "predicted": predictions}).to_csv(results_dir / "sensor_selection_predictions.csv", index=False)
    metrics = pd.DataFrame(
        [
            {
                "samples": args.samples,
                "seed": args.seed,
                "model": "DecisionTreeClassifier(max_depth=6)",
                "accuracy": round(float(accuracy), 4),
                "mean_energy": round(float(data["Energy_Consumption"].mean()), 4),
                "mean_latency": round(float(data["Response_Latency"].mean()), 4),
            }
        ]
    )
    metrics.to_csv(results_dir / "sensor_selection_metrics.csv", index=False)

    report = f"""# Synthetic Adaptive Sensor Selection Report

- Samples: {args.samples}
- Seed: {args.seed}
- Model: DecisionTreeClassifier(max_depth=6)
- Accuracy: {accuracy:.4f}
- Mean energy: {data['Energy_Consumption'].mean():.2f}
- Mean latency: {data['Response_Latency'].mean():.2f} ms

Boundary: fictional synthetic data only; not real smart-city performance.
"""
    (reports_dir / "sensor_selection_report.md").write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
