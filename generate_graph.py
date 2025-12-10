import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

# Load the Kalman filter results
results = pd.read_csv('kalman_results.csv')

# Create high-quality figure
fig, ax = plt.subplots(figsize=(10, 6), dpi=300)

# Plot data with professional styling
ax.plot(results['Time'], results['Sensor_A_Close'], 
        color='#E67E22', linewidth=2.5, label='Sensor A (Close, 5cm)', alpha=0.9)
ax.plot(results['Time'], results['Sensor_B_Far'], 
        color='#3498DB', linewidth=2.5, label='Sensor B (Far, 15cm)', alpha=0.9)
ax.plot(results['Time'], results['Bulb_Estimate'], 
        color='#27AE60', linewidth=3.0, label='Kalman Filter Estimate', linestyle='-', alpha=0.95)

# Styling
ax.set_xlabel('Time (seconds)', fontsize=14, fontweight='bold')
ax.set_ylabel('Temperature (Celsius)', fontsize=14, fontweight='bold')
ax.set_title('Real Experimental Data: Kalman Filter Temperature Estimation', 
             fontsize=14, fontweight='bold', pad=15)
ax.legend(loc='upper right', fontsize=11, framealpha=0.95, edgecolor='black')
ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
ax.set_xlim(0, 600)
ax.set_ylim(28, 72)

# Add annotation for key result
bulb_value = results['Bulb_Estimate'].iloc[10]
annotation_text = f'KF Estimate at t=100s: {bulb_value:.1f}C'
ax.annotate(annotation_text,
            xy=(100, bulb_value), 
            xytext=(250, 60),
            fontsize=10, 
            bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.7),
            arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.3', color='black', lw=1.5))

plt.tight_layout()
plt.savefig('experimental_results.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()

print('Graph saved: experimental_results.png (300 DPI)')
