# 🌡️ Indirect Temperature Estimation Using Kalman Filter (Two Sensors)

An academic research project demonstrating **Bayesian inference through Kalman Filter** for indirect temperature measurement in building environment simulations. This project solves the challenge of estimating hidden bulb temperature (200-300°C) using two complementary air temperature sensors.

![Project Status](https://img.shields.io/badge/Status-Complete-success)
![Academic](https://img.shields.io/badge/Type-Academic%20Research-blue)
![Probability](https://img.shields.io/badge/Course-Probability%20Fall%202025-orange)

## 👥 Authors
- **Tran Hoai Nhan**
- **Le Hong Nhat Tan**

**Course:** Probability Course Fall 2025  
**Professor:** Tran Vinh Linh

## 🎯 Project Overview

In Computational Fluid Dynamics (CFD) simulations of building environments, accurate boundary conditions are critical. Dr. Nguyen Hop Minh's experimental setup requires precise knowledge of a hot bulb's surface temperature (200–300°C) to validate CFD models. However, direct measurement is impractical—sensors would melt at such temperatures.

### The Solution
We developed an **indirect measurement approach** using two air temperature sensors positioned at different distances from the heat source, combining their readings through a **Kalman Filter** to estimate the bulb's temperature via **sequential Bayesian inference**.

## 🔬 Methodology

### Sensor Configuration
- **Sensor A (Close):** d_A = 5 cm, R_A = 2.0 (higher signal, more noise)
- **Sensor B (Far):** d_B = 15 cm, R_B = 0.5 (lower signal, stable)

### Mathematical Framework
The Kalman Filter implements optimal Bayesian estimation with Gaussian distributions:

**Prior Belief:** p(x) = N(x; x̂, P)  
**Likelihood:** p(z|x) = N(z; Hx, R)  
**Posterior:** p(x|z) ∝ p(z|x) · p(x)

### Key Results
- **Bulb Estimate:** Mean = 67.2°C, Std = 2.2°C (over 600s)
- **Sensor Fusion:** Optimally combines proximity advantage with stability
- **Adaptive Weighting:** Kalman Gain dynamically adjusts based on uncertainty

## ✨ Features

### 📊 Interactive Simulation Tool
- Configure true bulb temperature (100-400°C)
- Adjust sensor distances and noise levels
- Set process noise (Q) for system uncertainty
- Real-time Kalman Filter visualization
- Statistical analysis of results

### 📈 Real Experimental Data
- 600 seconds of continuous measurements
- Sensor A: Mean = 36.4°C, Std = 2.1°C
- Sensor B: Mean = 30.5°C, Std = 0.6°C
- Live comparison graphs

### 📐 Mathematical Rigor
- Complete Bayesian framework equations
- Prediction step (prior propagation)
- Update step (posterior via Bayes)
- Observation model with explicit coefficients

## 📐 Mathematical Framework

### Heat Diffusion Model
```
z_A = H_A × x + v_A,  where H_A = 0.75
z_B = H_B × x + v_B,  where H_B = 0.25
```
- `x` = True bulb temperature (hidden state)
- `z_A, z_B` = Sensor measurements
- `H_A, H_B` = Observation coefficients (distance-based)
- `v_A ~ N(0, R_A)`, `v_B ~ N(0, R_B)` = Gaussian noise

### Kalman Filter Algorithm

**Prediction Step (Prior Propagation):**
```
x̂_pred = x̂_prev          (propagate mean)
P_pred = P_prev + Q       (increase uncertainty)
```

**Update Step (Posterior via Bayes):**

*Sequential Fusion with Sensor A:*
```
K_A = P_pred / (P_pred + R_A)                    (Bayes weight)
x̂_A = x̂_pred + K_A(z_A - H_A × x̂_pred)         (posterior mean)
P_A = (1 - K_A × H_A) × P_pred                   (posterior variance)
```

*Sequential Fusion with Sensor B:*
```
K_B = P_A / (P_A + R_B)                          (Bayes weight)
x̂_new = x̂_A + K_B(z_B - H_B × x̂_A)             (final posterior)
P_new = (1 - K_B × H_B) × P_A                    (final variance)
```

## 🎲 Probability Concepts

| Concept | Application |
|---------|-------------|
| **Gaussian Distributions** | Prior p(x) = N(x; x̂, P), Likelihood p(z\|x) = N(z; Hx, R) |
| **Bayes' Rule** | Posterior p(x\|z) ∝ p(z\|x) · p(x) |
| **Sequential Inference** | Update belief with each new measurement |
| **Optimal Fusion** | Kalman Gain minimizes mean squared error |
| **Uncertainty Quantification** | Variance P tracks estimation confidence |

## 🚀 Live Demo

**Website:** [https://leonathn.github.io/FinalProjectProbability](https://leonathn.github.io/FinalProjectProbability)

### Features:
- Real experimental setup photos and diagrams
- Interactive simulation tool with adjustable parameters
- Real-time Kalman Filter visualization
- Downloadable data and analysis files

## 📁 Repository Structure

```
FinalProjectProbability/
├── README.md                      # Project documentation
├── index.html                     # Main website with interactive tool
├── poster_landscape.pdf           # Academic poster
├── SensorPlacement.png            # Real experimental setup photo
├── SensorPlacementDiagram.png     # Schematic diagram
├── experimental_results.png       # Results visualization
├── temperature_data.csv           # Raw sensor measurements
├── kalman_results.csv             # Kalman Filter outputs
└── Temperature_Analysis.xlsx      # Statistical analysis
```

## 🛠️ Technologies

- **HTML5/CSS3/JavaScript** - Interactive web interface with Canvas API
- **Python** - Data analysis and graph generation (matplotlib, pandas, numpy)
- **LaTeX (TikZposter)** - Academic poster design
- **GitHub Pages** - Hosting and deployment

## 📊 Data Files

All experimental data is available for download:
- **temperature_data.csv** - 61 data points over 600 seconds
- **kalman_results.csv** - Filtered estimates and sensor readings
- **Temperature_Analysis.xlsx** - Complete statistical analysis

## 🎓 Key Takeaways

- **Indirect Measurement:** Infer hidden states from observable quantities using domain knowledge
- **Sensor Fusion:** Multiple imperfect sensors provide complementary information
- **Bayesian Approach:** Model uncertainty explicitly for optimal estimation
- **Real-World Validation:** Method tested on actual experimental data from building environment research

## 📖 References

1. Kalman, R. E. (1960). "A New Approach to Linear Filtering and Prediction Problems." *Journal of Basic Engineering*, 82(D): 35-45.
2. Welch, G., & Bishop, G. (2006). "An Introduction to the Kalman Filter." *UNC Chapel Hill*, TR 95-041.
3. Simon, D. (2006). *Optimal State Estimation: Kalman, H∞, and Nonlinear Approaches*. Wiley-Interscience.

## 📧 Contact

For questions or collaboration opportunities:
- **GitHub:** [@leonathn](https://github.com/leonathn)
- **Course:** Probability Fall 2025, Professor Tran Vinh Linh

---

© 2025 Tran Hoai Nhan & Le Hong Nhat Tan | Probability Course Fall 2025

## 🙏 Acknowledgments

- Rudolf E. Kálmán - Creator of the Kalman Filter (1960)
- Dr. Tran Vinh Linh
- Various online resources for understanding Kalman Filter applications

---

⭐ **If you found this helpful, please give it a star!** ⭐
