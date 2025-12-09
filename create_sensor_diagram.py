import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Circle, FancyBboxPatch, FancyArrowPatch
import matplotlib
matplotlib.use('Agg')

fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
ax.set_xlim(-2, 20)
ax.set_ylim(-2, 8)
ax.axis('off')

# Hot bulb (center)
bulb = Circle((8, 4), 0.8, color='#FF4500', edgecolor='black', linewidth=2)
ax.add_patch(bulb)
ax.text(8, 4, 'Hot\nBulb', ha='center', va='center', fontsize=10, weight='bold', color='white')
ax.text(8, 2, '200-300°C', ha='center', fontsize=9, style='italic')

# Sensor A (close)
sensor_a = FancyBboxPatch((3, 3.5), 1.5, 1, boxstyle='round,pad=0.1', 
                          edgecolor='black', facecolor='#E67E22', linewidth=2)
ax.add_patch(sensor_a)
ax.text(3.75, 4, 'Sensor A', ha='center', fontsize=9, weight='bold', color='white')
ax.text(3.75, 1.5, 'Close\nd_A = 5 cm\nR_A = 2.0', ha='center', fontsize=8)

# Sensor B (far)
sensor_b = FancyBboxPatch((13.5, 3.5), 1.5, 1, boxstyle='round,pad=0.1',
                          edgecolor='black', facecolor='#3498DB', linewidth=2)
ax.add_patch(sensor_b)
ax.text(14.25, 4, 'Sensor B', ha='center', fontsize=9, weight='bold', color='white')
ax.text(14.25, 1.5, 'Far\nd_B = 15 cm\nR_B = 0.5', ha='center', fontsize=8)

# Distance arrows
arrow_a = FancyArrowPatch((4.5, 4), (7.2, 4), arrowstyle='<->', mutation_scale=20,
                          linewidth=2, color='black')
ax.add_patch(arrow_a)
ax.text(5.85, 4.5, '5 cm', ha='center', fontsize=9, weight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='black'))

arrow_b = FancyArrowPatch((8.8, 4), (13.5, 4), arrowstyle='<->', mutation_scale=20,
                          linewidth=2, color='black')
ax.add_patch(arrow_b)
ax.text(11.15, 4.5, '15 cm', ha='center', fontsize=9, weight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='black'))

# Heat radiation waves
for i in range(3):
    circle = Circle((8, 4), 1.5 + i*0.7, fill=False, edgecolor='#FF6347', 
                   linewidth=1.5, linestyle='--', alpha=0.5-i*0.1)
    ax.add_patch(circle)

# Title
ax.text(10, 7, 'Two-Sensor Temperature Measurement Setup', ha='center', 
        fontsize=14, weight='bold')

# Add legend box
legend_box = FancyBboxPatch((0.5, 5.5), 3.5, 1.5, boxstyle='round,pad=0.1',
                            edgecolor='black', facecolor='#f0f0f0', linewidth=1.5)
ax.add_patch(legend_box)
ax.text(2.25, 6.5, 'Measurement Strategy:', ha='center', fontsize=9, weight='bold')
ax.text(2.25, 6.1, 'Indirect estimation via', ha='center', fontsize=8)
ax.text(2.25, 5.8, 'Kalman Filter fusion', ha='center', fontsize=8)

plt.tight_layout()
plt.savefig('SensorPlacement.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()

print('Sensor placement diagram saved: SensorPlacement.png')
