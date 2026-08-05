# Publication Readiness Plan

This document outlines how the project could be framed as an academic research artifact.

## Possible paper framing

**Title idea:** Adaptive AIoT Sensor Group Selection for Energy-Efficient Smart-City Traffic Monitoring

The project can be framed as a transparent synthetic benchmark for evaluating whether dynamic sensor selection can reduce energy consumption and response latency while preserving monitoring coverage under changing traffic, weather, visibility, and time-of-day conditions.

## Research questions

1. How does adaptive sensor group selection affect energy consumption compared with always-on sensing?
2. Which traffic and weather conditions require richer sensor coverage?
3. How much latency can be reduced while preserving coverage and safety proxies?
4. Which model or rule-based policy gives the most interpretable selection behavior?
5. Do energy-saving policies create risk in low-visibility or high-density scenarios?

## Suggested baseline comparisons

| Baseline | Purpose |
|---|---|
| Always-on sensors | Maximum coverage, high energy baseline |
| Minimal sensor policy | Lowest energy baseline with possible safety loss |
| Rule-based selector | Transparent scenario-driven policy |
| Decision tree classifier | Explainable supervised baseline |
| Random forest classifier | Stronger supervised baseline |
| Cost-aware selector | Explicit energy-latency trade-off policy |

## Evidence to include

- Dataset generation and scenario definitions.
- Sensor encoding and target-label definition.
- Train/test split and random seeds.
- Accuracy and confusion analysis for sensor groups.
- Energy-consumption comparison.
- Response-latency comparison.
- Scenario-level safety or coverage review.
- Limitations and synthetic-data boundary.

## Reviewer concerns to address

- Synthetic data cannot prove deployment performance.
- Sensor costs and latency assumptions must be transparent.
- Real deployment requires calibration and hardware validation.
- Smart-city sensing requires privacy and equity governance.
- Model accuracy alone is not enough for safety-critical use.
