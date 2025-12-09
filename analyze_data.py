import numpy as np
import pandas as pd

# Load data
data = pd.read_csv('temperature_data.csv')
time = data['Time'].values
sensor_a = data['Middle_Heat_Source'].values  # Close to heat source
sensor_b = data['Air_Tube_Output'].values     # Farther from heat source

# Kalman Filter parameters (simulating bulb temperature estimation)
# True bulb temperature would be higher than both measurements
Q = 0.1  # Process noise
R_A = 2.0  # Sensor A noise (more noisy, closer)
R_B = 0.5  # Sensor B noise (less noisy, farther)

# Distance factors (heat diffusion model)
d_A = 5.0  # cm, close to bulb
d_B = 15.0  # cm, farther from bulb

# Initialize
x_est = 45.0  # Initial bulb temperature estimate
P = 10.0  # Initial uncertainty

# Store results
bulb_estimates = []

# Kalman Filter loop
for i in range(len(time)):
    # Prediction step
    x_pred = x_est
    P_pred = P + Q
    
    # Update with Sensor A (accounting for distance)
    H_A = 1.0 / (1 + d_A/10)  # Observation model (heat decreases with distance)
    innovation_A = sensor_a[i] - H_A * x_pred
    S_A = H_A * P_pred * H_A + R_A
    K_A = P_pred * H_A / S_A
    x_est = x_pred + K_A * innovation_A
    P = (1 - K_A * H_A) * P_pred
    
    # Update with Sensor B
    H_B = 1.0 / (1 + d_B/10)  # Heat decreases more with distance
    innovation_B = sensor_b[i] - H_B * x_est
    S_B = H_B * P * H_B + R_B
    K_B = P * H_B / S_B
    x_est = x_est + K_B * innovation_B
    P = (1 - K_B * H_B) * P
    
    bulb_estimates.append(x_est)

# Save results
results = pd.DataFrame({
    'Time': time,
    'Sensor_A_Close': sensor_a,
    'Sensor_B_Far': sensor_b,
    'Bulb_Estimate': bulb_estimates
})
results.to_csv('kalman_results.csv', index=False)

# Calculate statistics
print('=== Temperature Statistics ===')
print(f'Sensor A (Close): Mean={sensor_a.mean():.2f}C, Std={sensor_a.std():.2f}C')
print(f'Sensor B (Far): Mean={sensor_b.mean():.2f}C, Std={sensor_b.std():.2f}C')
print(f'Bulb Estimate: Mean={np.mean(bulb_estimates):.2f}C, Std={np.std(bulb_estimates):.2f}C')
print(f'\nAt t=100s: Sensor A={sensor_a[10]:.1f}C, Sensor B={sensor_b[10]:.1f}C, Estimate={bulb_estimates[10]:.1f}C')
print(f'At t=300s: Sensor A={sensor_a[30]:.1f}C, Sensor B={sensor_b[30]:.1f}C, Estimate={bulb_estimates[30]:.1f}C')
print(f'At t=600s: Sensor A={sensor_a[60]:.1f}C, Sensor B={sensor_b[60]:.1f}C, Estimate={bulb_estimates[60]:.1f}C')
