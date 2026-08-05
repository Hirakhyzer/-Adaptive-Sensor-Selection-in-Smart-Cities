# Reproducibility Playbook

This playbook defines how to run, document, and report experiments from the **Adaptive Sensor Selection in Smart Cities** project.

## 1. Minimum run record

Every experiment should record:

| Field | Example |
|---|---|
| Run name | `adaptive_sensor_seed_42_decision_tree` |
| Dataset type | synthetic smart-city sensor scenarios |
| Number of samples | `10000` or current dataset size |
| Scenario set | traffic, weather, visibility, time-of-day combinations |
| Random seed | `42` |
| Sensor set | camera, radar, LiDAR, loop, acoustic, weather or configured sensors |
| Model or policy | decision tree, rules, random forest, cost-aware policy |
| Metrics | accuracy, energy, latency, coverage, safety proxy |
| Output directory | `outputs/` |
| Boundary statement | synthetic decision-support results only, not real city performance |

## 2. Recommended command

```bash
python scripts/run_sensor_selection_baseline.py --seed 42
```

## 3. Evidence bundle

A complete run should include:

```text
outputs/results/sensor_selection_metrics.csv
outputs/results/sensor_selection_predictions.csv
outputs/results/scenario_summary.csv
outputs/reports/sensor_selection_report.md
outputs/figures/energy_latency_tradeoff.png
outputs/figures/sensor_activation_patterns.png
outputs/figures/scenario_performance.png
```

## 4. Interpretation rules

- Report energy, latency, and safety/coverage together.
- Do not claim real-world traffic-monitoring performance from synthetic data.
- State which sensors are included and how each sensor is encoded.
- Preserve any train/test split and random seed in the report.
- Explain whether the method is rule-based, supervised learning, or optimization-based.
- Clearly distinguish model accuracy from operational safety.

## 5. Checklist before sharing results

- [ ] Dataset version recorded.
- [ ] Random seed and train/test split recorded.
- [ ] Model or policy settings documented.
- [ ] Energy-latency-safety trade-off reported.
- [ ] Synthetic-data boundary stated clearly.
- [ ] No real infrastructure deployment claim is made.
