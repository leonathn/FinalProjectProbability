import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import matplotlib
matplotlib.use('Agg')

fig, ax = plt.subplots(figsize=(12, 8), dpi=300)
ax.set_xlim(-2, 12)
ax.set_ylim(-4, 7)
ax.axis('off')

# Physical System (top box)
physical_box = FancyBboxPatch((1, 4), 3, 2, boxstyle='round,pad=0.1', 
                              edgecolor='black', facecolor='white', linewidth=2)
ax.add_patch(physical_box)
ax.text(2.5, 5.3, 'Physical', ha='center', fontsize=12, weight='bold')
ax.text(2.5, 4.7, 'System', ha='center', fontsize=12, weight='bold')

# Mathematical Model (bottom left box)
model_box = FancyBboxPatch((1, 0.5), 3, 2, boxstyle='round,pad=0.1',
                           edgecolor='black', facecolor='#E3F2FD', linewidth=2)
ax.add_patch(model_box)
ax.text(2.5, 1.8, 'Mathematical', ha='center', fontsize=11, weight='bold')
ax.text(2.5, 1.2, 'model', ha='center', fontsize=11, weight='bold')

# Mathematical Model on right (for comparison)
model_box2 = FancyBboxPatch((7.5, 1.5), 2.5, 1.5, boxstyle='round,pad=0.1',
                            edgecolor='black', facecolor='white', linewidth=2)
ax.add_patch(model_box2)
ax.text(8.75, 2.5, 'Mathematical', ha='center', fontsize=9, weight='bold')
ax.text(8.75, 2, 'model', ha='center', fontsize=9, weight='bold')

# Observer Gain K (bottom box)
k_box = FancyBboxPatch((1.8, -1.5), 1.4, 0.8, boxstyle='round,pad=0.05',
                       edgecolor='black', facecolor='white', linewidth=2)
ax.add_patch(k_box)
ax.text(2.5, -1.1, 'K', ha='center', fontsize=14, weight='bold')

# K gain on right
k_box2 = FancyBboxPatch((6, 2), 0.8, 0.6, boxstyle='round,pad=0.05',
                        edgecolor='black', facecolor='white', linewidth=2)
ax.add_patch(k_box2)
ax.text(6.4, 2.3, 'K', ha='center', fontsize=12, weight='bold')

# Comparator circles
circle1 = Circle((5, 5), 0.35, edgecolor='black', facecolor='white', linewidth=2)
ax.add_patch(circle1)
ax.plot([4.65, 5.35], [5, 5], 'k-', linewidth=2)
ax.plot([5, 5], [4.65, 5.35], 'k-', linewidth=2)
ax.text(5, 5, '+', ha='center', va='center', fontsize=14, weight='bold')

circle2 = Circle((11, 3), 0.35, edgecolor='black', facecolor='white', linewidth=2)
ax.add_patch(circle2)
ax.plot([10.65, 11.35], [3, 3], 'k-', linewidth=2)
ax.plot([11, 11], [2.65, 3.35], 'k-', linewidth=2)
ax.text(11, 3, '+', ha='center', va='center', fontsize=14, weight='bold')

# Arrows - Left side (Physical system inputs/outputs)
arrow1 = FancyArrowPatch((-1, 5.5), (1, 5.5), arrowstyle='->', mutation_scale=20, 
                        linewidth=2, color='black')
ax.add_patch(arrow1)
ax.text(0, 5.8, r'{fuel}$', ha='center', fontsize=10)

arrow2 = FancyArrowPatch((4, 5.5), (5.5, 5.5), arrowstyle='->', mutation_scale=20,
                        linewidth=2, color='black')
ax.add_patch(arrow2)
ax.text(4.75, 5.8, r'{ext}$', ha='center', fontsize=10)

arrow3 = FancyArrowPatch((2.5, 4), (2.5, 2.8), arrowstyle='->', mutation_scale=20,
                        linewidth=2, color='red')
ax.add_patch(arrow3)
ax.text(3.2, 3.4, r'{in}$', ha='center', fontsize=10, color='red')
ax.text(3, 3.8, '', ha='center', fontsize=20, color='red', weight='bold')

# Arrows from model inputs
arrow4 = FancyArrowPatch((-1, 2), (1, 2), arrowstyle='->', mutation_scale=20,
                        linewidth=2, color='black')
ax.add_patch(arrow4)

arrow5 = FancyArrowPatch((-1, 1), (1, 1), arrowstyle='->', mutation_scale=20,
                        linewidth=2, color='black')
ax.add_patch(arrow5)

# Arrow from model to T_in_hat
arrow6 = FancyArrowPatch((2.5, 0.5), (2.5, -0.3), arrowstyle='->', mutation_scale=20,
                        linewidth=2, color='black')
ax.add_patch(arrow6)
ax.text(2.5, -0.6, r'$\hat{T}_{in}$', ha='center', fontsize=10, 
        bbox=dict(boxstyle='circle,pad=0.3', facecolor='lightblue', edgecolor='blue', linewidth=2))

# Arrow to K and feedback
arrow7 = FancyArrowPatch((2.5, -0.7), (2.5, -1.5), arrowstyle='->', mutation_scale=20,
                        linewidth=2, color='black')
ax.add_patch(arrow7)

arrow8 = FancyArrowPatch((1.8, -1.1), (-1, -1.1), arrowstyle='->', mutation_scale=20,
                        linewidth=2, color='black')
ax.add_patch(arrow8)
ax.add_patch(FancyArrowPatch((-1, -1.1), (-1, 1), arrowstyle='->', mutation_scale=20,
                            linewidth=2, color='black'))

# Arrow from comparator to physical system
arrow9 = FancyArrowPatch((5, 5.35), (5, 4.8), arrowstyle='->', mutation_scale=20,
                        linewidth=2, color='black')
ax.add_patch(arrow9)

# Right side arrows
arrow10 = FancyArrowPatch((5.5, 2.3), (6, 2.3), arrowstyle='->', mutation_scale=20,
                         linewidth=2, color='black')
ax.add_patch(arrow10)
ax.text(5.75, 2.6, 'e', ha='center', fontsize=10, style='italic')

arrow11 = FancyArrowPatch((6.8, 2.3), (7.5, 2.3), arrowstyle='->', mutation_scale=20,
                         linewidth=2, color='black')
ax.add_patch(arrow11)
ax.text(7.15, 2.6, r'{fuel}$', ha='center', fontsize=9)

arrow12 = FancyArrowPatch((10, 2.3), (10.65, 3), arrowstyle='->', mutation_scale=20,
                         linewidth=2, color='black')
ax.add_patch(arrow12)
ax.text(10.5, 2.6, r'$\hat{T}_{ext}$', ha='center', fontsize=9)

arrow13 = FancyArrowPatch((11.35, 3), (11.7, 3), arrowstyle='->', mutation_scale=20,
                         linewidth=2, color='black')
ax.add_patch(arrow13)
ax.text(11.9, 3, r'{ext}$', ha='center', fontsize=9)

# Feedback arrow from output back
ax.add_patch(FancyArrowPatch((11, 3.35), (11, 4.5), arrowstyle='->', mutation_scale=20,
                            linewidth=2, color='green'))
ax.add_patch(FancyArrowPatch((11, 4.5), (5.5, 4.5), arrowstyle='->', mutation_scale=20,
                            linewidth=2, color='green'))
ax.add_patch(FancyArrowPatch((5.5, 4.5), (5.5, 5.35), arrowstyle='->', mutation_scale=20,
                            linewidth=2, color='green'))

# Checkmarks
ax.text(-0.5, 6.3, '', ha='center', fontsize=24, color='green', weight='bold')
ax.text(4.5, 6.3, '', ha='center', fontsize=24, color='green', weight='bold')
ax.text(2.5, -0.15, '', ha='center', fontsize=20, color='green', weight='bold')

# Error equation
ax.text(5.75, 1.2, r' = error = T_{ext} - \hat{T}_{ext}$', ha='center', 
        fontsize=11, style='italic')

# Title
ax.text(2.5, -3, 'STATE OBSERVER', ha='center', fontsize=16, 
        weight='bold', color='#1565C0')

plt.tight_layout()
plt.savefig('state_observer_diagram.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()

print('State observer diagram saved: state_observer_diagram.png')
