# 📊 Kalman Filter - Interactive Probability Visualization

An interactive educational web application that demonstrates the **Kalman Filter** algorithm with real-world data examples. This project helps students understand how probability theory applies to signal processing and estimation.

![Kalman Filter Demo](https://img.shields.io/badge/Demo-Live-brightgreen)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)

## 🎯 Project Overview

This project was created as a **Final Project for Probability Course** to demonstrate how theoretical probability concepts apply to real-world applications.

### What is the Kalman Filter?

The Kalman Filter is an algorithm that estimates the true state of a system from noisy measurements. It's used in:
- 📱 **GPS Navigation** - Smoothing location data
- 🚗 **Self-driving Cars** - Sensor fusion
- 📈 **Stock Market** - Trend analysis
- 🌡️ **Weather Stations** - Temperature filtering
- 🤖 **Robotics** - Position estimation

## ✨ Features

### 📈 Before vs After Comparison
- Side-by-side visualization of raw noisy data vs Kalman filtered output
- Clear visual proof that the filter reduces noise while preserving trends

### 🔄 Multiple Data Sources
Switch between different real-world data patterns:
- ₿ **Bitcoin Price** - Cryptocurrency volatility
- 🌡️ **Temperature** - Weather sensor readings
- 📈 **Stock Market** - Financial index movements
- 📡 **Sensor Data** - Accelerometer readings
- 📍 **GPS Track** - Location coordinates

### 🎛️ Interactive Controls
- Adjust **Measurement Noise (R)** - How noisy your sensor is
- Adjust **Process Noise (Q)** - How much the system changes
- Real-time visualization updates

### 📚 Educational Content
- **Probability Connection** - How Kalman relates to Gaussian distributions, Bayes' theorem, and variance
- **Simple Math Explanation** - Just 3 easy steps with examples
- **Intuitive Analogies** - No-math explanations anyone can understand

### 🧮 Interactive Calculator
- Input your own values
- Step-by-step calculation breakdown
- Understand each part of the algorithm

### 📊 Statistical Validation
- Variance reduction percentage
- Noise level comparison bars
- Trend preservation correlation

## 🔢 The Math (Simplified!)

The Kalman Filter works in **3 simple steps**:

### Step 1: Calculate Trust Factor (Kalman Gain)
```
K = P / (P + R)
```
- `K` = How much to trust the measurement (0 to 1)
- `P` = Our current uncertainty
- `R` = Measurement noise

### Step 2: Update Estimate
```
New Estimate = Old Estimate + K × (Measurement - Old Estimate)
```
This is just a **weighted average**!

### Step 3: Update Uncertainty
```
P_new = (1 - K) × P_old
```
Uncertainty decreases after each measurement.

## 🎲 Probability Concepts Used

| Concept | How It's Used |
|---------|---------------|
| **Gaussian Distribution** | Measurements assumed to follow normal distribution |
| **Variance (σ²)** | P represents uncertainty/spread of our estimate |
| **Weighted Average** | Combining prediction and measurement |
| **Bayes' Theorem** | Updating beliefs based on new evidence |
| **Conditional Probability** | P(true state \| measurements) |
| **Expected Value** | The weighted average formula |

## 🚀 Getting Started

### Option 1: Open Locally
Simply open `kalman-realdata.html` in any modern web browser.

### Option 2: View Online
Visit the GitHub Pages site: [Live Demo](https://YOUR_USERNAME.github.io/FinalProjectProbability/)

## 📁 Project Structure

```
FinalProjectProbability/
├── README.md                 # This file
├── kalman-realdata.html      # Main interactive visualization
└── index.html                # (Optional) Landing page
```

## 🛠️ Technologies Used

- **HTML5** - Structure and Canvas API for charts
- **CSS3** - Modern styling with gradients and animations
- **JavaScript** - Kalman Filter implementation and interactivity
- **No external dependencies** - Runs entirely in the browser!

## 📖 How to Use

1. **Select a Data Source** - Click on Bitcoin, Temperature, Stock, etc.
2. **View Before/After** - See the raw noisy data vs filtered result
3. **Adjust Parameters** - Use sliders to change R (measurement noise) and Q (process noise)
4. **Read the Explanation** - Scroll down to understand the math
5. **Try the Calculator** - Input your own values to see step-by-step calculations

## 🎓 Learning Objectives

After using this visualization, you will understand:
- ✅ How noise affects measurements
- ✅ Why averaging improves estimates
- ✅ How the Kalman Gain balances trust between prediction and measurement
- ✅ How uncertainty decreases with more data
- ✅ Real-world applications of probability theory

## 📸 Screenshots

### Main Visualization
*Before/After comparison showing noise reduction*

### Interactive Calculator
*Step-by-step Kalman Filter calculation*

### Probability Explanation
*Simple math with intuitive examples*

## 👨‍💻 Author

**Your Name**  
Final Project - Probability and Statistics Course  
December 2025

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Rudolf E. Kálmán - Creator of the Kalman Filter (1960)
- Probability and Statistics course instructors
- Various online resources for understanding Kalman Filter applications

---

⭐ **If you found this helpful, please give it a star!** ⭐
