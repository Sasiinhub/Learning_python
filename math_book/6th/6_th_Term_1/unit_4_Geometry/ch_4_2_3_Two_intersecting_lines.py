import matplotlib.pyplot as plt

# 1. Create a figure window
fig, ax = plt.subplots(figsize=(6, 6))

# 2. Set the background color (a muted, slightly darker graph paper green)
ax.set_facecolor('#C8E6C9') 

# 3. Lock the axes limits exactly from 0 to 50
ax.set_xlim(0, 50)
ax.set_ylim(0, 50)

# 4. Force grid lines to show up at every single number interval
ax.set_xticks(range(0, 51, 5))  # Major lines every 5 units
ax.set_yticks(range(0, 51, 5))

# 5. Style the grid lines (darker green lines so they pop on the background)
ax.grid(True, color='#81C784', linestyle='-', linewidth=1.2)

# 6. Optional: Let's draw a sample line on our new 50x50 grid!
# Line goes from (10, 10) to (40, 45)
ax.plot([10, 35], [10, 35], color='black', linewidth=3, label="Sample Line")
ax.plot([10, 35], [35, 10], color='black', linewidth=3, label="Sample Line")

# 7. Display the graph sheet
plt.show()
