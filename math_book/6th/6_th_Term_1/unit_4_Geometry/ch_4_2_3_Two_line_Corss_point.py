

import matplotlib.pyplot as plt

def find_intersection(line1_start, line1_end, line2_start, line2_end):
    """Calculates the exact (X, Y) intersection point of two lines."""
    x1, y1 = line1_start
    x2, y2 = line1_end
    x3, y3 = line2_start
    x4, y4 = line2_end
    
    denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if denominator == 0:
        return None 
        
    intersect_x = ((x1*y2 - y1*x2)*(x3 - x4) - (x1 - x2)*(x3*y4 - y3*x4)) / denominator
    intersect_y = ((x1*y2 - y1*x2)*(y3 - y4) - (y1 - y2)*(x3*y4 - y3*x4)) / denominator
    return intersect_x, intersect_y

# Define the point coordinate tuples
line_a_start_point = (5, 10)
line_a_end_point   = (45, 40)

line_b_start_point = (5, 45)
line_b_end_point   = (40, 5)

# Setup graph sheet
fig, ax = plt.subplots(figsize=(7, 7))
ax.set_facecolor('#C8E6C9') 
ax.set_xlim(0, 50)
ax.set_ylim(0, 50)
ax.grid(True, color='#81C784', linewidth=1.2)

# 1. Draw Line 1 (Points A to B)
ax.plot([line_a_start_point[0], line_a_end_point[0]], 
        [line_a_start_point[1], line_a_end_point[1]], 
        color='blue', marker='o', markersize=6)

# 2. Draw Line 2 (Points C to D)
ax.plot([line_b_start_point[0], line_b_end_point[0]], 
        [line_b_start_point[1], line_b_end_point[1]], 
        color='purple', marker='o', markersize=6)

# 3. Add visible labels for A, B, C, and D with a small visual offset (+1)
ax.text(line_a_start_point[0] + 1, line_a_start_point[1] + 1, "A", fontsize=12, fontweight='bold', color='blue')
ax.text(line_a_end_point[0] + 1,   line_a_end_point[1] + 1,   "B", fontsize=12, fontweight='bold', color='blue')

ax.text(line_b_start_point[0] + 1, line_b_start_point[1] + 1, "C", fontsize=12, fontweight='bold', color='purple')
ax.text(line_b_end_point[0] + 1,   line_b_end_point[1] + 1,   "D", fontsize=12, fontweight='bold', color='purple')

# 4. Automatically find and label intersection point 'O'
cross_point = find_intersection(line_a_start_point, line_a_end_point, line_b_start_point, line_b_end_point)

if cross_point:
    # Draw the red cross point dot
    ax.scatter(cross_point[0], cross_point[1], color='red', s=120, zorder=5)
    
    # Label the cross point as 'O'
    ax.text(cross_point[0] + 1, cross_point[1] + 1, "O", fontsize=14, fontweight='bold', color='red')

plt.show()




'''import matplotlib.pyplot as plt

def find_intersection(line1_start, line1_end, line2_start, line2_end):
    """Calculates the exact (X, Y) intersection point of two lines."""
    x1, y1 = line1_start
    x2, y2 = line1_end
    x3, y3 = line2_start
    x4, y4 = line2_end
    
    denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if denominator == 0:
        return None 
        
    intersect_x = ((x1*y2 - y1*x2)*(x3 - x4) - (x1 - x2)*(x3*y4 - y3*x4)) / denominator
    intersect_y = ((x1*y2 - y1*x2)*(y3 - y4) - (y1 - y2)*(x3*y4 - y3*x4)) / denominator
    return intersect_x, intersect_y

# Define the coordinate tuples
line_A_start_point, line_A_end_point = (5, 10), (45, 40)
line_B_start_point, line_B_end_point = (5, 45), (40, 5)

# Setup graph sheet
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_facecolor('#C8E6C9') 
ax.set_xlim(0, 50)
ax.set_ylim(0, 50)
ax.grid(True, color='#81C784', linewidth=1.2)

# --- FIXED DRAWING CODE USING INDEXING ---
# Line A: [x1, x2], [y1, y2] here this funcion takes like this, not direct tuple 
ax.plot([line_A_start[0], line_A_end[0]], [line_A_start[1], line_A_end[1]], color='blue', marker='o')

# Line B: [x3, x4], [y3, y4]
ax.plot([line_B_start[0], line_B_end[0]], [line_B_start[1], line_B_end[1]], color='purple', marker='o')


#Add visible labels for A, B, C, and D with a small visual offset (+1)
ax.text(line_a_start_point[0] + 1, line_a_start_point[1] + 1, "A", fontsize=12, fontweight='bold', color='blue')
ax.text(line_a_end_point[0] + 1,   line_a_end_point[1] + 1,   "B", fontsize=12, fontweight='bold', color='blue')

ax.text(line_b_start_point[0] + 1, line_b_start_point[1] + 1, "C", fontsize=12, fontweight='bold', color='purple')
ax.text(line_b_end_point[0] + 1,   line_b_end_point[1] + 1,   "D", fontsize=12, fontweight='bold', color='purple')





# Find intersection automatically
cross_point = find_intersection(line_A_start, line_A_end, line_B_start, line_B_end)



if cross_point:
    # cross_point[0] is X, cross_point[1] is Y
    ax.scatter(cross_point[0], cross_point[1], color='red', s=150, zorder=5)

    # Label the cross point as 'O'
    ax.text(cross_point[0] + 1, cross_point[1] + 1, "O", fontsize=14, fontweight='bold', color='red')


plt.show()
'''


