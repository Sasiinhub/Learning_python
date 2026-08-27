

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 1. Create a figure and tell it to use 3D projection
fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111, projection='3d')

# 2. Set the slightly darker graph paper colors
# Matplotlib 3D has separate 'panes' for background walls
blueprint_bg = '#C8E6C9'    # Slightly darker pastel green
grid_line_color = '#81C784' # Deep green for grid lines

ax.xaxis.set_pane_color(blueprint_bg)
ax.yaxis.set_pane_color(blueprint_bg)
ax.zaxis.set_pane_color(blueprint_bg)

# 3. Lock all three axes exactly from 0 to 50
ax.set_xlim3d(0, 50)
ax.set_ylim3d(0, 50)
ax.set_zlim3d(0, 50)

# Style the grid lines for all 3 axes
ax.xaxis._axinfo["grid"].update({"color": grid_line_color, "linewidth": 1.2})
ax.yaxis._axinfo["grid"].update({"color": grid_line_color, "linewidth": 1.2})
ax.zaxis._axinfo["grid"].update({"color": grid_line_color, "linewidth": 1.2})

# Label the dimensions
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')

# 4. Define the 3D lines to build a Cube (from coordinate 15 to 35)
# In 3D, we plot lines by passing: [All X coordinates], [All Y], [All Z]
# Lower square base of the cube
ax.plot([15], [15], [15], color='black', linewidth=2)

# Upper square top of the cube
#ax.plot([30], [30], [30], color='black', linewidth=2)

# Vertical pillars connecting base to top
#ax.plot([15, 15], [15, 15], [15, 35], color='black', linewidth=2)
#ax.plot([35, 35], [15, 15], [15, 35], color='black', linewidth=2)
#ax.plot([35, 35], [35, 35], [15, 35], color='black', linewidth=2)
#ax.plot([15, 15], [35, 35], [15, 35], color='black', linewidth=2)

# 5. Display the interactive 3D grid
plt.show()

